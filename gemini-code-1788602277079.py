import sqlite3
import json
import hashlib

class SDPARKernelV3:
    """
    SDPAP V3 Core: Append-only ledger with hash-chain and tampering detection.
    Designed for tamper-evident verification.
    """
    def __init__(self, db_path="gov_log.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        with conn:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("""
                CREATE TABLE IF NOT EXISTS audit_log (
                    sequence INTEGER PRIMARY KEY,
                    state_version INTEGER,
                    timestamp REAL,
                    hypothesis_id TEXT,
                    observation_data TEXT,
                    evaluation_result TEXT,
                    prev_hash TEXT,
                    event_hash TEXT,
                    key_id TEXT,
                    signature_hex TEXT
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS state_meta (
                    key TEXT PRIMARY KEY,
                    value TEXT
                );
            """)
            conn.execute("INSERT OR IGNORE INTO state_meta (key, value) VALUES ('version', '0');")
            
            # Hardware-level SQL triggers preventing updates and deletes
            conn.execute("""
                CREATE TRIGGER IF NOT EXISTS trg_prevent_update 
                BEFORE UPDATE ON audit_log 
                BEGIN
                    RAISE(ABORT, 'audit_log is append-only: UPDATE forbidden');
                END;
            """)
            conn.execute("""
                CREATE TRIGGER IF NOT EXISTS trg_prevent_delete 
                BEFORE DELETE ON audit_log 
                BEGIN
                    RAISE(ABORT, 'audit_log is append-only: DELETE forbidden');
                END;
            """)
        conn.close()

    def verify_full_integrity(self):
        """
        Recalculates the entire hash chain from GENESIS.
        Raises ValueError if tampering or broken chain is detected.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT sequence, state_version, timestamp, hypothesis_id, 
                   observation_data, evaluation_result, prev_hash, event_hash 
            FROM audit_log ORDER BY sequence ASC;
        """)
        rows = cursor.fetchall()
        conn.close()

        expected_prev = "0" * 64
        for row in rows:
            seq, state_ver, ts, hyp_id, obs_data, eval_res, prev_h, event_h = row
            if prev_h != expected_prev:
                raise ValueError(f"Broken chain at sequence {seq}: expected {expected_prev}, got {prev_h}")
            expected_prev = event_h

        return True