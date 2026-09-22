#!/usr/bin/env python3
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

# --- КОНФИГУРАЦИЯ ЭПИЗОДА SDPAP-V3 ---
EPISODE_ID = "EP-2026-HEROY-BI-001"
EPISODE_TITLE = "Forensic Audit: Herbo / Herøy to BI Oslo Infrastructure Transition"
EVIDENCE_DIR = Path("./evidence")
OUTPUT_MANIFEST = Path("./manifest.json")
OUTPUT_README = Path("./README.md")


def calculate_sha256(file_path: Path) -> str:
    """Вычисление канонического SHA-256 хэша файла блоками по 64 КБ."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def compute_merkle_root(hashes: list[str]) -> str:
    """Расчет Merkle Root из списка SHA-256 хэшей артефактов."""
    if not hashes:
        return hashlib.sha256(b"").hexdigest()

    current_level = sorted(hashes)
    while len(current_level) > 1:
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        next_level = []
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i + 1]
            next_level.append(hashlib.sha256(combined.encode("utf-8")).hexdigest())
        current_level = next_level

    return current_level[0]


def generate_readme(data: dict) -> str:
    """Генерация автономного отчета в формате Markdown."""
    meta = data["episode_metadata"]
    readme_content = f"""# SDPAP-v3 Audit Log: {meta['episode_id']}

## {meta['title']}

**Системный статус:** Immutable Audit Record  
**Время сборки (UTC):** `{meta['timestamp_utc']}`  
**Merkle Root (Корневой хэш):** `{meta['merkle_root']}`  
**Всего доказательных артефактов:** `{meta['total_artifacts']}`  

---

### 1. Субъекты и институциональные связи

* **Субъект:** Анастасия Гайдай (*Anastasiia Haidai*)
* **Первичный узел:** *Herbo* / *Herøy Kommune* (Нурланн, Норвегия) — фиксация увольнения/выхода в 2024 г.
* **Вторичный узел:** *BI Norwegian Business School* / *AI Mission Hub* (Осло, Норвегия) — должность *Care and Support Coordinator* (август 2026 г.).

---

### 2. Реестр криптографических отпечатков артефактов (SHA-256)

| Относительный путь | Имя файла | Размер (Bytes) | SHA-256 Контрольная сумма |
| :--- | :--- | :--- | :--- |
"""
    for item in data["artifacts"]:
        readme_content += f"| `{item['relative_path']}` | `{item['filename']}` | {item['size_bytes']} | `{item['sha256']}` |\n"

    readme_content += """
---

### 3. Инструкция по независимой проверке (Verification)

Для проверки неизменности и целостности всех файлов запустите локальный скрипт проверки:

```bash
python3 verify.py
