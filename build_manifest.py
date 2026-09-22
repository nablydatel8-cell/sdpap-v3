git add .
git commit -m "EP-2026-HEROY-BI-001 | Sync 27 downloaded evidence files and script logs"
git push origin main
git add .
git commit -m "EP-2026-HEROY-BI-001 | Sync 27 downloaded evidence files and script logs"
git push origin main
python3 build_manifest.py
python3 build_manifest.py
# 1. Переходим в директорию проекта sdpap-v3
cd sdpap-v3

# 2. Создаем директорию для доказательств, если её ещё нет
mkdir -p evidence

# 3. Перемещаем файлы .eml и артефакты доказательств в папку evidence
mv ~/название_файлов.eml ./evidence/ 2>/dev/null || true
mv ~/*.eml ./evidence/ 2>/dev/null || true
mv ~/*.pdf ./evidence/ 2>/dev/null || true

# 4. Перемещаем вспомогательные скрипты (если они среди скачанных) в корень проекта
mv ~/gemini-code-*.py ./ 2>/dev/null || true
mv ~/code_art*.py ./ 2>/dev/null || true
# 1. Переходим в директорию проекта sdpap-v3
cd sdpap-v3

# 2. Создаем директорию для доказательств, если её ещё нет
mkdir -p evidence

# 3. Перемещаем файлы .eml и артефакты доказательств в папку evidence
mv ~/название_файлов.eml ./evidence/ 2>/dev/null || true
mv ~/*.eml ./evidence/ 2>/dev/null || true
mv ~/*.pdf ./evidence/ 2>/dev/null || true

# 4. Перемещаем вспомогательные скрипты (если они среди скачанных) в корень проекта
mv ~/gemini-code-*.py ./ 2>/dev/null || true
mv ~/code_art*.py ./ 2>/dev/null || true
git add manifest.json README.md
git commit -m "Update Merkle Root with 2026-09-22 EML evidence artifacts"
git push origin main
git add manifest.json README.md
git commit -m "Update Merkle Root with 2026-09-22 EML evidence artifacts"
git push origin main
python3 build_manifest.py
python3 build_manifest.py
git pull origin main
git pull origin main
Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp12699898rwb;
        Tue, 22 Sep 2026 04:28:32 -0700 (PDT)
X-Received: by 2002:a05:690e:1c1d:b0:671:58f2:fb68 with SMTP id 956f58d0204a3-672c29710dcmr1164236d50.11.1790076511821;
        Tue, 22 Sep 2026 04:28:31 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1790076511; cv=pass;
        d=google.com; s=arc-20260327;
        b=LvtSU8S/0DAAi/j1WfWNuGB7GtVkWHjmedhnfQLkxLoaZJGAyqy3z91aUHh1YtyKTi
         Md7kHhP4C5+bz++200rmCB0Phfm6uwYxMyb5yTWK1T6xAAHgHisclIDUJhHl87ZflViZ
         3pCtK4SMkAEk58JjmYXiSBUFgSdiYpRGRt9bS1Bcd17NLemCus0CrgqcwnK5J2mZbotO
         SEHhzQRpkqykNB6ZsQ8zUoO0SAfd1yRRcAj07ggieMsq7mqe0LUzjn8c1/YN+nUAowTJ
         /sEgMHcYj60YjCzn7UjrA+qEDLd8tcMn4IdFQ+IKHr774thcFXYQxOU57PsMNaLi84tU
         gFWw==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=fc8P6SQrTR7KY+MUvB67dlKuC6ObvX4uIMoSdSDm41A=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=SbbMYPnj/q2rcqKEAEmnxJEHWrnIIeJHgDRQlkKhhqwUAaw1KturMDH6bAiztKpnjH
         Mou7Cd+9LEEQOy0JepIvUwCvPEjd35pAAkaxajdGnshKr75ygNEuEGWPoYgKgFR0MOSs
         QDYKhQeE/nuvGzxRLOmNvxec/DS5l9XktHXDbXtPoW5eY85oslpxcIZvY3ETFZ8EPfx2
         wmwWBHkCC+DwtIEMusWwcuOAklIe2PNxPwt9vi+YRdiLh6AnNSE8o3NjNxeiLTt6VN+B
         /4Nwurh7pZkm3ZllfEMcfz4pN5B0DBmWSgJzAUrpFj7TiqPtbMpCgI+5NJq9yA3aY/26
         g9tQ==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b="j+n/g0pj";
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 956f58d0204a3-672c7719625sor733487d50.8.2026.09.22.04.28.31
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Tue, 22 Sep 2026 04:28:31 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b="j+n/g0pj";
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1790076511; cv=none;
        d=google.com; s=arc-20260327;
        b=PsG27/xkQvJLreLRHPe6xp3x1l1OX2BSpW0j/zds62VSTNhI6ubPtLRy1Gq7XCZx4O
         qQmkXEIjAPSDkiPPogcy/MGzDFAs8BDOq1Lu9ztpDn514Tgb+zPYTe74zYPBhcAfbcQw
         F0YF+Sq+n/pwGqg83Kxobw+gCFDgEWuuAtILKP2nqZpzEuDsi/luDI3E4BOxWCosHbJm
         ymnQzW9yAualrH/O7Hy/yoYmY8/som4+wLI6M6YKWH2B7qKuqj7Scf9ZMYTyx2rRAeoq
         +BTO+s++1cRieh6VDTeKa9hCfFoe3vbF6I/vcAX9HizBjOZnHFYDCx833Tj10wM1FFAS
         Pp6g==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=fc8P6SQrTR7KY+MUvB67dlKuC6ObvX4uIMoSdSDm41A=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=diGctChpRZJtX5wywgn6DZn4TfzLt5jt+JwRPi7P7yXlXPO2xSE2L+WSFtdK7iYLR9
         x5dlS7JclQYdW8RqJ8ubPMc0OBJYFlP3VzQxqi4aXTnK+X4+45fF9sWU4hZpBro/yYg8
         SGaSuhbTt9pGbKvNfombt+7VoY2zS6RzQZoJZn8R/fjcaWajDGB9bnBstJ6+vqm7VKIH
         3xhSX5Pqc9JcVSus9Bu+HwFWcV41a1p6otmBLGUGUZBaupiqsnBnOpKIRjcHWQLuAHqi
         gr7NnRmluXGqIq4my7hggff8Fw5/v+3jHUctaAkMO4OdSKL1wJ1Pm0RbnZE6s3GVTpf5
         HL7g==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1790076511; x=1790681311; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=fc8P6SQrTR7KY+MUvB67dlKuC6ObvX4uIMoSdSDm41A=;
        b=j+n/g0pjSKPZs3MJfsu0ZAyXhatS6P3Ww05JZWPjb1IW8r+QJin69uNMj5gexoFdyC
         jfR2/WG0WaliZVJAVSrcF2YyshVKlJnFWRXaxKO3cjHmsKZ3ccteduErgAZFlZpJrL0Y
         Qw97zfkV6MUfb4OWJAu6/wIwIAZDHV2n00C8DtNSjCa4N52Bx4kVnwSN146k1zOLDYTq
         8wxmGnEv73U5sczW7A1SI8K8WoFRZmFPhaEJiwrQUBKk5SLTx/FRekTsJUM9iCy/J0dy
         x7akkYfNyKtKlfKDQ/uJIXXMSmAZUYdikTOccy0ioiufCylGv+2W0boc/VmWsk9jsg6E
         H+3g==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1790076511; x=1790681311;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=fc8P6SQrTR7KY+MUvB67dlKuC6ObvX4uIMoSdSDm41A=;
        b=DbW/qQoqhdeqnkwcVgC1GLI1QLlObQQSgZu4E5QDWvnslGZ1TY+qHRJeq69ieAds5b
         BnqkE/m6Il2vLjB2icew9zrOj1ErLw5AMSZF3RXvhCIm5S4oxzJ5YFW3vPV+T4IuhCqM
         wjK7+aeEI2X+T1g+BkZ4LQgF+XDlj33GkEqpGz7QNGCJJhwtYvFQ5NMEDS65YqqAxwnI
         J1jIY0yoIdGL7AFkVc1Diq3dh3G3A2HXZ2elamY+YnkL+AGx/fM4cKIGkw1SOev/+zoY
         1ezVjaIuhzzvZt8zNaGjQ7ayTdl77Ienu1Kb4pZ6NZ54zTbYEUNAJyHeDkuCyQRYpH3+
         cBOQ==
X-Gm-Message-State: AFuF++lcaMnUlo0Rvy5C6J9okuyf5JBI5mVrTQJInHbOgPrm/vBovz+u
	pF5qSfOrRgOL4DW8o2a1VPDqhR0shWnpLyZZNSYRmAt9+Be9fT57OXC29mvjs8t7/yySzkzzQq/
	ayIVJni1aCLR83gdsC0dKgsdimhPqRcReFIMe
X-Gm-Gg: AYBFou1ElSFw1u6THr3B5wmrd9/ppnU7Z3CKGVUUoQYTMWvyLmdlaBwGln+tLv2wOqL
	vU3bdu0V5E8oGYYymGH0oynPvlZexUoysy5s6+uEe3JR11Xa0Waj8EzGCxmILOK2j8LqFHB4vOj
	xUpqj5QaxtZAspSkd3N81g6PEfEoWuAbjqB7g5WpJwdVWmqMACx5J30/fz2Ze1Z577m7iinY8jI
	YgmrqeeEclE+gdv19AFgpmJT4wLXJOmzpAocNmAm4ZviyIzqir5JJwO4lHFoeA7PTyL9EaoaZzT
	XOHdxkA5F6fpNYD0rukhTDXQPfBh1AOhtBT6EFRJjU9UQEnOqtVSF8JJWC8nh3+cpw==
X-Received: by 2002:a05:690e:16a1:b0:671:2b90:7b82 with SMTP id
 956f58d0204a3-672c2bbc17emr993461d50.47.1790076511490; Tue, 22 Sep 2026
 04:28:31 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7011:4b18:b0:54d:f762:679e with HTTP; Tue, 22 Sep 2026
 04:28:31 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Tue, 22 Sep 2026 04:28:31 -0700
X-Gm-Features: AcwNN1U-WWv-I0dQF7cRig1k1whXVJ81zXPcxVqyd92cw2iUsxaRAPL9mN_14Wg
Message-ID: <CAM0o817SZB_T1sSs82E9_yd1uEOVVv5LUmnj__BVYBwiXe+Vhg@mail.gmail.com>
Subject: =?UTF-8?B?0LrQvtC80LXQvdGC0LrQt9Cw0LPQvtC70L7QstC60YM=?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="000000000000969675065c10aa37"

--000000000000969675065c10aa37
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: base64

Rm9yZW5zaWMgQXVkaXQ6IEhlcmJvIC8gSGVyw7h5IHRvIEJJIE9zbG8gLSBmcm9tIFZJUlRVQUwg
RklTSCB0byBSRUFMIE1PTkVZDQppbXByaW50IFtTVFJJUFBFRCA3MyBieXRlc106IEh1YXdlaSBD
aHJvbWVib29rIGd1ZXN0IC8gc3F1YXJlcyAtPiBtYWlsIC0+DQpEb3dubG9hZCBsZXR0ZXIgLT4g
R2l0SHViDQo0IGFydGlmYWN0cyB2ZXJpZmllZCB2aWEgdmVyaWZ5LnB5IC8gRlJFRSBGT1IgQUxM
IFdJVEhPVVQgVkVORE9SIExPQ0stSU4NCtCc0KvQodCb0Jgg0JzQkNCi0JXQoNCY0JDQm9Cs0J3Q
qyDQndCQIDEwMCUgLyDQnNCr0KHQm9CsINCh0JLQntCR0J7QlNCd0JAg0J/Qo9Ci0Kwg0J7QotCa
0KDQq9CiDQo=
--000000000000969675065c10aa37
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: base64

PGRpdj5Gb3JlbnNpYyBBdWRpdDogSGVyYm8gLyBIZXLDuHkgdG8gQkkgT3NsbyAtIGZyb20gVklS
VFVBTCBGSVNIIHRvIFJFQUwgTU9ORVk8L2Rpdj48ZGl2PmltcHJpbnQgW1NUUklQUEVEIDczIGJ5
dGVzXTogSHVhd2VpIENocm9tZWJvb2sgZ3Vlc3QgLyBzcXVhcmVzIC0mZ3Q7IG1haWwgLSZndDsg
RG93bmxvYWQgbGV0dGVyIC0mZ3Q7IEdpdEh1YjwvZGl2PjxkaXY+NCBhcnRpZmFjdHMgdmVyaWZp
ZWQgdmlhIHZlcmlmeS5weSAvIEZSRUUgRk9SIEFMTCBXSVRIT1VUIFZFTkRPUiBMT0NLLUlOPC9k
aXY+PGRpdj7QnNCr0KHQm9CYINCc0JDQotCV0KDQmNCQ0JvQrNCd0Ksg0J3QkCAxMDAlIC8g0JzQ
q9Ch0JvQrCDQodCS0J7QkdCe0JTQndCQINCf0KPQotCsINCe0KLQmtCg0KvQojwvZGl2Pg0K
--000000000000969675065c10aa37--

Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp12699898rwb;
        Tue, 22 Sep 2026 04:28:32 -0700 (PDT)
X-Received: by 2002:a05:690e:1c1d:b0:671:58f2:fb68 with SMTP id 956f58d0204a3-672c29710dcmr1164236d50.11.1790076511821;
        Tue, 22 Sep 2026 04:28:31 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1790076511; cv=pass;
        d=google.com; s=arc-20260327;
        b=LvtSU8S/0DAAi/j1WfWNuGB7GtVkWHjmedhnfQLkxLoaZJGAyqy3z91aUHh1YtyKTi
         Md7kHhP4C5+bz++200rmCB0Phfm6uwYxMyb5yTWK1T6xAAHgHisclIDUJhHl87ZflViZ
         3pCtK4SMkAEk58JjmYXiSBUFgSdiYpRGRt9bS1Bcd17NLemCus0CrgqcwnK5J2mZbotO
         SEHhzQRpkqykNB6ZsQ8zUoO0SAfd1yRRcAj07ggieMsq7mqe0LUzjn8c1/YN+nUAowTJ
         /sEgMHcYj60YjCzn7UjrA+qEDLd8tcMn4IdFQ+IKHr774thcFXYQxOU57PsMNaLi84tU
         gFWw==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=fc8P6SQrTR7KY+MUvB67dlKuC6ObvX4uIMoSdSDm41A=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=SbbMYPnj/q2rcqKEAEmnxJEHWrnIIeJHgDRQlkKhhqwUAaw1KturMDH6bAiztKpnjH
         Mou7Cd+9LEEQOy0JepIvUwCvPEjd35pAAkaxajdGnshKr75ygNEuEGWPoYgKgFR0MOSs
         QDYKhQeE/nuvGzxRLOmNvxec/DS5l9XktHXDbXtPoW5eY85oslpxcIZvY3ETFZ8EPfx2
         wmwWBHkCC+DwtIEMusWwcuOAklIe2PNxPwt9vi+YRdiLh6AnNSE8o3NjNxeiLTt6VN+B
         /4Nwurh7pZkm3ZllfEMcfz4pN5B0DBmWSgJzAUrpFj7TiqPtbMpCgI+5NJq9yA3aY/26
         g9tQ==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b="j+n/g0pj";
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 956f58d0204a3-672c7719625sor733487d50.8.2026.09.22.04.28.31
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Tue, 22 Sep 2026 04:28:31 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b="j+n/g0pj";
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1790076511; cv=none;
        d=google.com; s=arc-20260327;
        b=PsG27/xkQvJLreLRHPe6xp3x1l1OX2BSpW0j/zds62VSTNhI6ubPtLRy1Gq7XCZx4O
         qQmkXEIjAPSDkiPPogcy/MGzDFAs8BDOq1Lu9ztpDn514Tgb+zPYTe74zYPBhcAfbcQw
         F0YF+Sq+n/pwGqg83Kxobw+gCFDgEWuuAtILKP2nqZpzEuDsi/luDI3E4BOxWCosHbJm
         ymnQzW9yAualrH/O7Hy/yoYmY8/som4+wLI6M6YKWH2B7qKuqj7Scf9ZMYTyx2rRAeoq
         +BTO+s++1cRieh6VDTeKa9hCfFoe3vbF6I/vcAX9HizBjOZnHFYDCx833Tj10wM1FFAS
         Pp6g==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=fc8P6SQrTR7KY+MUvB67dlKuC6ObvX4uIMoSdSDm41A=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=diGctChpRZJtX5wywgn6DZn4TfzLt5jt+JwRPi7P7yXlXPO2xSE2L+WSFtdK7iYLR9
         x5dlS7JclQYdW8RqJ8ubPMc0OBJYFlP3VzQxqi4aXTnK+X4+45fF9sWU4hZpBro/yYg8
         SGaSuhbTt9pGbKvNfombt+7VoY2zS6RzQZoJZn8R/fjcaWajDGB9bnBstJ6+vqm7VKIH
         3xhSX5Pqc9JcVSus9Bu+HwFWcV41a1p6otmBLGUGUZBaupiqsnBnOpKIRjcHWQLuAHqi
         gr7NnRmluXGqIq4my7hggff8Fw5/v+3jHUctaAkMO4OdSKL1wJ1Pm0RbnZE6s3GVTpf5
         HL7g==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1790076511; x=1790681311; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=fc8P6SQrTR7KY+MUvB67dlKuC6ObvX4uIMoSdSDm41A=;
        b=j+n/g0pjSKPZs3MJfsu0ZAyXhatS6P3Ww05JZWPjb1IW8r+QJin69uNMj5gexoFdyC
         jfR2/WG0WaliZVJAVSrcF2YyshVKlJnFWRXaxKO3cjHmsKZ3ccteduErgAZFlZpJrL0Y
         Qw97zfkV6MUfb4OWJAu6/wIwIAZDHV2n00C8DtNSjCa4N52Bx4kVnwSN146k1zOLDYTq
         8wxmGnEv73U5sczW7A1SI8K8WoFRZmFPhaEJiwrQUBKk5SLTx/FRekTsJUM9iCy/J0dy
         x7akkYfNyKtKlfKDQ/uJIXXMSmAZUYdikTOccy0ioiufCylGv+2W0boc/VmWsk9jsg6E
         H+3g==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1790076511; x=1790681311;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=fc8P6SQrTR7KY+MUvB67dlKuC6ObvX4uIMoSdSDm41A=;
        b=DbW/qQoqhdeqnkwcVgC1GLI1QLlObQQSgZu4E5QDWvnslGZ1TY+qHRJeq69ieAds5b
         BnqkE/m6Il2vLjB2icew9zrOj1ErLw5AMSZF3RXvhCIm5S4oxzJ5YFW3vPV+T4IuhCqM
         wjK7+aeEI2X+T1g+BkZ4LQgF+XDlj33GkEqpGz7QNGCJJhwtYvFQ5NMEDS65YqqAxwnI
         J1jIY0yoIdGL7AFkVc1Diq3dh3G3A2HXZ2elamY+YnkL+AGx/fM4cKIGkw1SOev/+zoY
         1ezVjaIuhzzvZt8zNaGjQ7ayTdl77Ienu1Kb4pZ6NZ54zTbYEUNAJyHeDkuCyQRYpH3+
         cBOQ==
X-Gm-Message-State: AFuF++lcaMnUlo0Rvy5C6J9okuyf5JBI5mVrTQJInHbOgPrm/vBovz+u
	pF5qSfOrRgOL4DW8o2a1VPDqhR0shWnpLyZZNSYRmAt9+Be9fT57OXC29mvjs8t7/yySzkzzQq/
	ayIVJni1aCLR83gdsC0dKgsdimhPqRcReFIMe
X-Gm-Gg: AYBFou1ElSFw1u6THr3B5wmrd9/ppnU7Z3CKGVUUoQYTMWvyLmdlaBwGln+tLv2wOqL
	vU3bdu0V5E8oGYYymGH0oynPvlZexUoysy5s6+uEe3JR11Xa0Waj8EzGCxmILOK2j8LqFHB4vOj
	xUpqj5QaxtZAspSkd3N81g6PEfEoWuAbjqB7g5WpJwdVWmqMACx5J30/fz2Ze1Z577m7iinY8jI
	YgmrqeeEclE+gdv19AFgpmJT4wLXJOmzpAocNmAm4ZviyIzqir5JJwO4lHFoeA7PTyL9EaoaZzT
	XOHdxkA5F6fpNYD0rukhTDXQPfBh1AOhtBT6EFRJjU9UQEnOqtVSF8JJWC8nh3+cpw==
X-Received: by 2002:a05:690e:16a1:b0:671:2b90:7b82 with SMTP id
 956f58d0204a3-672c2bbc17emr993461d50.47.1790076511490; Tue, 22 Sep 2026
 04:28:31 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7011:4b18:b0:54d:f762:679e with HTTP; Tue, 22 Sep 2026
 04:28:31 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Tue, 22 Sep 2026 04:28:31 -0700
X-Gm-Features: AcwNN1U-WWv-I0dQF7cRig1k1whXVJ81zXPcxVqyd92cw2iUsxaRAPL9mN_14Wg
Message-ID: <CAM0o817SZB_T1sSs82E9_yd1uEOVVv5LUmnj__BVYBwiXe+Vhg@mail.gmail.com>
Subject: =?UTF-8?B?0LrQvtC80LXQvdGC0LrQt9Cw0LPQvtC70L7QstC60YM=?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="000000000000969675065c10aa37"

--000000000000969675065c10aa37
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: base64

Rm9yZW5zaWMgQXVkaXQ6IEhlcmJvIC8gSGVyw7h5IHRvIEJJIE9zbG8gLSBmcm9tIFZJUlRVQUwg
RklTSCB0byBSRUFMIE1PTkVZDQppbXByaW50IFtTVFJJUFBFRCA3MyBieXRlc106IEh1YXdlaSBD
aHJvbWVib29rIGd1ZXN0IC8gc3F1YXJlcyAtPiBtYWlsIC0+DQpEb3dubG9hZCBsZXR0ZXIgLT4g
R2l0SHViDQo0IGFydGlmYWN0cyB2ZXJpZmllZCB2aWEgdmVyaWZ5LnB5IC8gRlJFRSBGT1IgQUxM
IFdJVEhPVVQgVkVORE9SIExPQ0stSU4NCtCc0KvQodCb0Jgg0JzQkNCi0JXQoNCY0JDQm9Cs0J3Q
qyDQndCQIDEwMCUgLyDQnNCr0KHQm9CsINCh0JLQntCR0J7QlNCd0JAg0J/Qo9Ci0Kwg0J7QotCa
0KDQq9CiDQo=
--000000000000969675065c10aa37
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: base64

PGRpdj5Gb3JlbnNpYyBBdWRpdDogSGVyYm8gLyBIZXLDuHkgdG8gQkkgT3NsbyAtIGZyb20gVklS
VFVBTCBGSVNIIHRvIFJFQUwgTU9ORVk8L2Rpdj48ZGl2PmltcHJpbnQgW1NUUklQUEVEIDczIGJ5
dGVzXTogSHVhd2VpIENocm9tZWJvb2sgZ3Vlc3QgLyBzcXVhcmVzIC0mZ3Q7IG1haWwgLSZndDsg
RG93bmxvYWQgbGV0dGVyIC0mZ3Q7IEdpdEh1YjwvZGl2PjxkaXY+NCBhcnRpZmFjdHMgdmVyaWZp
ZWQgdmlhIHZlcmlmeS5weSAvIEZSRUUgRk9SIEFMTCBXSVRIT1VUIFZFTkRPUiBMT0NLLUlOPC9k
aXY+PGRpdj7QnNCr0KHQm9CYINCc0JDQotCV0KDQmNCQ0JvQrNCd0Ksg0J3QkCAxMDAlIC8g0JzQ
q9Ch0JvQrCDQodCS0J7QkdCe0JTQndCQINCf0KPQotCsINCe0KLQmtCg0KvQojwvZGl2Pg0K
--000000000000969675065c10aa37--

Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp12698727rwb;
        Tue, 22 Sep 2026 04:27:24 -0700 (PDT)
X-Received: by 2002:a05:690c:c757:b0:899:9f8d:6398 with SMTP id 00721157ae682-8999fac0e67mr36573957b3.4.1790076444579;
        Tue, 22 Sep 2026 04:27:24 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1790076444; cv=pass;
        d=google.com; s=arc-20260327;
        b=d7D6nESr3mFrGdVnBWUTEqXQjGqBtJAbTq4+N2mRq/KG5TjLgiSs1zTmYaw8rCw533
         VkKCmGsGI+Dwvww+sld1FpZC+njXfkfa0cz2MhJ8lD0Uu5WAORpu61kSYA348kZLolPD
         uwVH+gECfRi7KWSEWi0agRiqA5RrxK+1cHUgG+YO4+CtthhBviPUjtJPKIJuCxSVtn0H
         BfTQIf60nP+ZtfoqLlgl9ekenYEtOzF6/Trf9kNyGX93mQjgf3JQUgz3hU4r1aTyL4Lv
         /cSLLh6VI24XVlzcoMbidXQT93yYGtvdKr3hi7Fj7VZba6QIZHpoEQKoeBdAXZfmc644
         P05A==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=KLMLkQ0W8B5ngzUd8VqOPCnO+aZIc0DXujdhu0qnrQc=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=JzcElv+NqPJkx2Km3+expyZVP4oWn1FxTsZdZffj9UIyt250ZZssQNZ421ivFnyyVf
         4pKgWjLT7jo4bKgin5lDlZYM03KKs4GUSw49Cn1zspwkPl+4GK3gTWn6H+MhFWTXJSpL
         AB4Ho5LX1I4jsS1WETAVo2A58b+peLm5XJfPYdGmQGYHOUJlVUtSsJnYkVbDcO9m+SWX
         12Xb9bHUbb3UTWra/qIDROwsyQ02ovm8/YRIsHFFJZx4fkI4daNIBm0OcELCt52VXOQg
         S/Jf2zOSHGddV/XkSLqm3CK6HqH9c1EJy9j7IZfxfSZioGY4zA6bvT3rp/DosktFpzeS
         vmfA==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=FFMxjDKO;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 00721157ae682-8a2bdc6f47csor9618967b3.2.2026.09.22.04.27.24
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Tue, 22 Sep 2026 04:27:24 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=FFMxjDKO;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1790076444; cv=none;
        d=google.com; s=arc-20260327;
        b=pNmKUb+avKaIiUHpRX9nLM1aLS1nAG+4w8WCmPUCyOfmeogVlhSc7Dd3HlIXS1YuMS
         Km4LaXfakcSbRb+pa32GysrQT7Ez3ZTDVYL/YLdzwY1eqpBKSTmhNHftAlm/N/1XsURM
         VeGjf4JUTTwe5e5mKZ9vvMpbDlxVcc7iCVXtjjbGTGTClBCTm3mQGIa2h4uj3UfU2h19
         iR6o9CkwF9OpZBbXtyYJySR26jZgyl/pfo/80f6jenYF4e1eL735XUUp632+Vye4bmQ4
         VR5hdCJ5SPmCE1lbINzSNRqM9phdm0vYHRgZU26yzCU1egc9cCDk4SgNZZkP48A1ltny
         bF6Q==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=KLMLkQ0W8B5ngzUd8VqOPCnO+aZIc0DXujdhu0qnrQc=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=dcWeqUkLaLy/4Wet0yYzYjxNKLn4zsVaPCVzyoWEtTNdQi2kPTxYJzR/jMlB/+foIs
         EypcpYMqCETlFo/w7WU2bmzIVuVPtyT8v8wip/VDkIkTU4GWe7tQ2TiykArCTwLWa8cZ
         Ld9SGYG/gYypuTCVLg2YmzGAyhue0Val0FtJAJhG4RQA1cuPiuS9nVlRz/vmDwE6MvK0
         +N4WeBrNNX7lQUbgP8a/9MuvCc8WWxJiWcKQcnUKr5MnAHNYGZgoR9u10/IzceI+JqK2
         eyUzLS5D9ry4mK8vFyI2dQBqHkYYRKeeXiXPRj6lAncL5Z69p1NLNgWPMfqOKwFUIi/u
         7Wxg==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1790076444; x=1790681244; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=KLMLkQ0W8B5ngzUd8VqOPCnO+aZIc0DXujdhu0qnrQc=;
        b=FFMxjDKONFBKvJ3bOM0LyKjHjDcJ0E/TWtrrvWlc5/wcFjaMVPTj7TKCzSrwU+g/Bs
         22t4Y0LlsYiVSo86howEREpaDPqdQJXsL3PfRsE/o0nPTlqYo5HmXqBaspeZBTioEzht
         mHlo102VVA49/r6Sa93zarR1obyW4jhkp0iswY9XkqVjFcFaCmqWMTYeQZd69x0Dqjq/
         Y+Lq/RgkG4lrSmwWtRWF2OS0r2YaKPxLg074ldPmT1fArfzxdSnAMMjKK+WcW8B6yjUE
         pZ9OVkH/Uohihk2ScwDYEPTo+xRRm57DtzvUX++H+9ZbrslC1zLL3GLdAPCBX8sN2nvk
         aN/Q==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1790076444; x=1790681244;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=KLMLkQ0W8B5ngzUd8VqOPCnO+aZIc0DXujdhu0qnrQc=;
        b=b4y8yLukZ8DVuR4UPpKTMNmISEO34OF9NcQ2/y5vozUN8duXI/YU8kRmovxd5InS2D
         LMJgkQ0ehIMcZwGFfJJBHdkqrZ3WwREB1H2R0OYopStKIGNkmatrAkNkcJ9X37KVLNuo
         o+WWiXUzDNZt7ifFUJuYJFd/QIDsii7g7xCL4hFuHIwZ6k0hTQHwps21GG21yAG/ziDs
         wbXJD6jAbqEHodg3jkIWNBvblnjUCh/4hiSLF5lWciZIiOr44LBuRscrftlrakCSeZMS
         yZ1w4/n6Tg/CkJ1geUW/+OEZP627Pvivncux8t+EJvxK2A1MjVyxhHO3XHyC/78JO/9K
         kGRA==
X-Gm-Message-State: AFuF++mgSGqU6Y7TXw51C1dSpN77B8QGE8gDa+2LKk9LJsEcOTEQG6g2
	0bsf49ndYteDXqgO7bNaOTz4o3rgXSRPFXuKY8lDC622bRoRwoG6oNbN2C9maaAqg/QdfgL1XjH
	TV56wTks23WPZDogu4xTgkhfi6YdzGO2SUkRB
X-Gm-Gg: AYBFou1F0cBPEHYX69oBrhS1wVGHa4azlSsp/kUBAy5pgQaF6j3fLYHE0/Lvul7suaP
	JgIfEPER9ftMEVIC9+X2XTW6oYNtcLGXW1OHP1057jaVD1J/eU75AEZWsGrSuhynOdN3ssDEwFd
	bQxjAjE959cblrT/TfvZ05UmVT6nAp7mF2g1AP2vvlYK+EUoR1E0MddPLJyc+aFPoKMHQ2A5PDG
	oSzrK5Jy2XNPpTviMkdZPFKxqaI29E8EOjS6UY2m6CoTl8V72/kX3mfR75XEQGWmKhbOOaw+4/X
	paG4mKyDiQA3LmjPi7VtMgqlQbhSnik45+UifLUQ1mwS2d/aTNQVNUou2HcR5y8O2w==
X-Received: by 2002:a05:690e:454f:20b0:66e:56e1:fcc0 with SMTP id
 956f58d0204a3-6717fc8ee28mr3322052d50.24.1790076444118; Tue, 22 Sep 2026
 04:27:24 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7011:4b18:b0:54d:f762:679e with HTTP; Tue, 22 Sep 2026
 04:27:23 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Tue, 22 Sep 2026 04:27:23 -0700
X-Gm-Features: AcwNN1WX7EAb6tMweXILDfI8FfNDGxuFOTBhpfNpxgxfppIXPV8n3p4r1Ky3j0M
Message-ID: <CAM0o816O0go-2HS21ibCQsOEFv9NuDzj6wSO6Py3gKBn_AAyAA@mail.gmail.com>
Subject: =?UTF-8?B?0LfQsNCz0L7Qu9C+0LLQvtC6?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="00000000000092924c065c10a648"

--00000000000092924c065c10a648
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

EP-2026-HEROY-BI-001 | PUBLIC MONEY PUBLIC PROOF | HER=C3=98Y KOMMUNE 87241=
7982
| Merkle 5ec09e46f7c25fa57ed369c0d32511a4d90b3b8a1d995cfe6757cdccd76cbc6e |
BLOCK 4096 HASH cd36560d

--00000000000092924c065c10a648
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

EP-2026-HEROY-BI-001 | PUBLIC MONEY PUBLIC PROOF | HER=C3=98Y KOMMUNE 87241=
7982 | Merkle 5ec09e46f7c25fa57ed369c0d32511a4d90b3b8a1d995cfe6757cdccd76cb=
c6e | BLOCK 4096 HASH cd36560d

--00000000000092924c065c10a648--

Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp12698727rwb;
        Tue, 22 Sep 2026 04:27:24 -0700 (PDT)
X-Received: by 2002:a05:690c:c757:b0:899:9f8d:6398 with SMTP id 00721157ae682-8999fac0e67mr36573957b3.4.1790076444579;
        Tue, 22 Sep 2026 04:27:24 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1790076444; cv=pass;
        d=google.com; s=arc-20260327;
        b=d7D6nESr3mFrGdVnBWUTEqXQjGqBtJAbTq4+N2mRq/KG5TjLgiSs1zTmYaw8rCw533
         VkKCmGsGI+Dwvww+sld1FpZC+njXfkfa0cz2MhJ8lD0Uu5WAORpu61kSYA348kZLolPD
         uwVH+gECfRi7KWSEWi0agRiqA5RrxK+1cHUgG+YO4+CtthhBviPUjtJPKIJuCxSVtn0H
         BfTQIf60nP+ZtfoqLlgl9ekenYEtOzF6/Trf9kNyGX93mQjgf3JQUgz3hU4r1aTyL4Lv
         /cSLLh6VI24XVlzcoMbidXQT93yYGtvdKr3hi7Fj7VZba6QIZHpoEQKoeBdAXZfmc644
         P05A==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=KLMLkQ0W8B5ngzUd8VqOPCnO+aZIc0DXujdhu0qnrQc=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=JzcElv+NqPJkx2Km3+expyZVP4oWn1FxTsZdZffj9UIyt250ZZssQNZ421ivFnyyVf
         4pKgWjLT7jo4bKgin5lDlZYM03KKs4GUSw49Cn1zspwkPl+4GK3gTWn6H+MhFWTXJSpL
         AB4Ho5LX1I4jsS1WETAVo2A58b+peLm5XJfPYdGmQGYHOUJlVUtSsJnYkVbDcO9m+SWX
         12Xb9bHUbb3UTWra/qIDROwsyQ02ovm8/YRIsHFFJZx4fkI4daNIBm0OcELCt52VXOQg
         S/Jf2zOSHGddV/XkSLqm3CK6HqH9c1EJy9j7IZfxfSZioGY4zA6bvT3rp/DosktFpzeS
         vmfA==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=FFMxjDKO;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 00721157ae682-8a2bdc6f47csor9618967b3.2.2026.09.22.04.27.24
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Tue, 22 Sep 2026 04:27:24 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=FFMxjDKO;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1790076444; cv=none;
        d=google.com; s=arc-20260327;
        b=pNmKUb+avKaIiUHpRX9nLM1aLS1nAG+4w8WCmPUCyOfmeogVlhSc7Dd3HlIXS1YuMS
         Km4LaXfakcSbRb+pa32GysrQT7Ez3ZTDVYL/YLdzwY1eqpBKSTmhNHftAlm/N/1XsURM
         VeGjf4JUTTwe5e5mKZ9vvMpbDlxVcc7iCVXtjjbGTGTClBCTm3mQGIa2h4uj3UfU2h19
         iR6o9CkwF9OpZBbXtyYJySR26jZgyl/pfo/80f6jenYF4e1eL735XUUp632+Vye4bmQ4
         VR5hdCJ5SPmCE1lbINzSNRqM9phdm0vYHRgZU26yzCU1egc9cCDk4SgNZZkP48A1ltny
         bF6Q==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=KLMLkQ0W8B5ngzUd8VqOPCnO+aZIc0DXujdhu0qnrQc=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=dcWeqUkLaLy/4Wet0yYzYjxNKLn4zsVaPCVzyoWEtTNdQi2kPTxYJzR/jMlB/+foIs
         EypcpYMqCETlFo/w7WU2bmzIVuVPtyT8v8wip/VDkIkTU4GWe7tQ2TiykArCTwLWa8cZ
         Ld9SGYG/gYypuTCVLg2YmzGAyhue0Val0FtJAJhG4RQA1cuPiuS9nVlRz/vmDwE6MvK0
         +N4WeBrNNX7lQUbgP8a/9MuvCc8WWxJiWcKQcnUKr5MnAHNYGZgoR9u10/IzceI+JqK2
         eyUzLS5D9ry4mK8vFyI2dQBqHkYYRKeeXiXPRj6lAncL5Z69p1NLNgWPMfqOKwFUIi/u
         7Wxg==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1790076444; x=1790681244; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=KLMLkQ0W8B5ngzUd8VqOPCnO+aZIc0DXujdhu0qnrQc=;
        b=FFMxjDKONFBKvJ3bOM0LyKjHjDcJ0E/TWtrrvWlc5/wcFjaMVPTj7TKCzSrwU+g/Bs
         22t4Y0LlsYiVSo86howEREpaDPqdQJXsL3PfRsE/o0nPTlqYo5HmXqBaspeZBTioEzht
         mHlo102VVA49/r6Sa93zarR1obyW4jhkp0iswY9XkqVjFcFaCmqWMTYeQZd69x0Dqjq/
         Y+Lq/RgkG4lrSmwWtRWF2OS0r2YaKPxLg074ldPmT1fArfzxdSnAMMjKK+WcW8B6yjUE
         pZ9OVkH/Uohihk2ScwDYEPTo+xRRm57DtzvUX++H+9ZbrslC1zLL3GLdAPCBX8sN2nvk
         aN/Q==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1790076444; x=1790681244;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=KLMLkQ0W8B5ngzUd8VqOPCnO+aZIc0DXujdhu0qnrQc=;
        b=b4y8yLukZ8DVuR4UPpKTMNmISEO34OF9NcQ2/y5vozUN8duXI/YU8kRmovxd5InS2D
         LMJgkQ0ehIMcZwGFfJJBHdkqrZ3WwREB1H2R0OYopStKIGNkmatrAkNkcJ9X37KVLNuo
         o+WWiXUzDNZt7ifFUJuYJFd/QIDsii7g7xCL4hFuHIwZ6k0hTQHwps21GG21yAG/ziDs
         wbXJD6jAbqEHodg3jkIWNBvblnjUCh/4hiSLF5lWciZIiOr44LBuRscrftlrakCSeZMS
         yZ1w4/n6Tg/CkJ1geUW/+OEZP627Pvivncux8t+EJvxK2A1MjVyxhHO3XHyC/78JO/9K
         kGRA==
X-Gm-Message-State: AFuF++mgSGqU6Y7TXw51C1dSpN77B8QGE8gDa+2LKk9LJsEcOTEQG6g2
	0bsf49ndYteDXqgO7bNaOTz4o3rgXSRPFXuKY8lDC622bRoRwoG6oNbN2C9maaAqg/QdfgL1XjH
	TV56wTks23WPZDogu4xTgkhfi6YdzGO2SUkRB
X-Gm-Gg: AYBFou1F0cBPEHYX69oBrhS1wVGHa4azlSsp/kUBAy5pgQaF6j3fLYHE0/Lvul7suaP
	JgIfEPER9ftMEVIC9+X2XTW6oYNtcLGXW1OHP1057jaVD1J/eU75AEZWsGrSuhynOdN3ssDEwFd
	bQxjAjE959cblrT/TfvZ05UmVT6nAp7mF2g1AP2vvlYK+EUoR1E0MddPLJyc+aFPoKMHQ2A5PDG
	oSzrK5Jy2XNPpTviMkdZPFKxqaI29E8EOjS6UY2m6CoTl8V72/kX3mfR75XEQGWmKhbOOaw+4/X
	paG4mKyDiQA3LmjPi7VtMgqlQbhSnik45+UifLUQ1mwS2d/aTNQVNUou2HcR5y8O2w==
X-Received: by 2002:a05:690e:454f:20b0:66e:56e1:fcc0 with SMTP id
 956f58d0204a3-6717fc8ee28mr3322052d50.24.1790076444118; Tue, 22 Sep 2026
 04:27:24 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7011:4b18:b0:54d:f762:679e with HTTP; Tue, 22 Sep 2026
 04:27:23 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Tue, 22 Sep 2026 04:27:23 -0700
X-Gm-Features: AcwNN1WX7EAb6tMweXILDfI8FfNDGxuFOTBhpfNpxgxfppIXPV8n3p4r1Ky3j0M
Message-ID: <CAM0o816O0go-2HS21ibCQsOEFv9NuDzj6wSO6Py3gKBn_AAyAA@mail.gmail.com>
Subject: =?UTF-8?B?0LfQsNCz0L7Qu9C+0LLQvtC6?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="00000000000092924c065c10a648"

--00000000000092924c065c10a648
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

EP-2026-HEROY-BI-001 | PUBLIC MONEY PUBLIC PROOF | HER=C3=98Y KOMMUNE 87241=
7982
| Merkle 5ec09e46f7c25fa57ed369c0d32511a4d90b3b8a1d995cfe6757cdccd76cbc6e |
BLOCK 4096 HASH cd36560d

--00000000000092924c065c10a648
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

EP-2026-HEROY-BI-001 | PUBLIC MONEY PUBLIC PROOF | HER=C3=98Y KOMMUNE 87241=
7982 | Merkle 5ec09e46f7c25fa57ed369c0d32511a4d90b3b8a1d995cfe6757cdccd76cb=
c6e | BLOCK 4096 HASH cd36560d

--00000000000092924c065c10a648--

Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp12669113rwb;
        Tue, 22 Sep 2026 04:01:30 -0700 (PDT)
X-Received: by 2002:a05:690e:1c0a:b0:672:a067:9a14 with SMTP id 956f58d0204a3-672c292b2demr1028363d50.9.1790074890197;
        Tue, 22 Sep 2026 04:01:30 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1790074890; cv=pass;
        d=google.com; s=arc-20260327;
        b=evFdHJFLQgYX408ShESel63pTychjFK6jmo+bax3jzq1Gx+u3yFRXJvjtFlroUvk9E
         ScL3tgivQelGHoCm9f7oVuA+M+v5dCs9dCheilLrHwVSNLucx7lnbPRNeyTY0ECfG3Tj
         gG+msAnu/0nl+1KuU3UpQRMGzdrxf54OSGVDDUEnIKXbEg2TNVilrjyzGZCcgqQ9ieev
         W1PmM2so1n4CiGy2wJLZjp6BqvjfTDPO0AZIVimDJNx7NobWn/b2t/xZlkrWDZd1oL5J
         arF+91xYgDtgGicLkXdWZ9efK1O5uY1d+RTqTDZCS2OxFqkAWw4r+3xLufeS7zeRskUO
         MY/Q==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=y0OSW8vG4Jh5+p4N0KT0JVs7Y3yS//BHJRRxO9GQYSo=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=bsflv9Bx3fXPd9SmGXg8H5DPvm6CqOqOlAtaFsIw54KQa8M+6jmBeH3vAS/6MkeNQb
         KYsnDhM0pJF3Ln16S9Ed9CYcNLt+7QoKP4NoIZtbVQJ5quX/JfNixVHX5AMpqYUpRAl/
         fRPPWjJ3C9MT6C1JYXWabaajzJalSUHEwhDGMh7/fwZhlMZmvppJkRaeHfbSPNmaZamY
         HAOdMqNUNc6RO/Sc1Q4tA9O38GrtVIhbeRWdckmTaddi4qPAC3vY5j6wC3xBVvkyxcJ2
         ooa+MWe9uF1F26S5GlQaGC51cLOEYt7CTuCqbszdoaUutRnDW2hQr2oTbSbSRWCZVd20
         oMjg==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=SF0HqYxM;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 956f58d0204a3-672c2767db7sor1014893d50.0.2026.09.22.04.01.30
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Tue, 22 Sep 2026 04:01:30 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=SF0HqYxM;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1790074890; cv=none;
        d=google.com; s=arc-20260327;
        b=XiN5BP5bLv7wHng9WFaODXXr2alcnMdWhsAoNUyNeppG3wo5cEl1kLfp7C+lRJlsaZ
         U9Lr+yq49K/QnWxxeDs1xA6d2x01VD710u6R2JlJ1QtQT+4YpF7ihxkLuC6POCbY98SR
         n0WwUfWVfJv5tG060epvuEAE7T/hCvvV909TOLqV/CRHKRFmwcS3jts/87/zGRvTq56j
         6ePIaCOIHu2Q0KtJdWHhE5Zs9YbUKL/N8hY0mTZvTCdvnVXMmBRcPWyzJqh6M6oGqDJ3
         uP9eAY0/cLEk0viflVEVvG3zOPETpYza1SCrrWfe6myHHjjKZ2CbMSUKM/a7wRoN0MZz
         +MXQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=y0OSW8vG4Jh5+p4N0KT0JVs7Y3yS//BHJRRxO9GQYSo=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=U77VlzkqnbDYjFYwD4YEqKa2Sdb6oWIj7I3+rxUnrejVNuRxfAXkE4i+XbdzDqpb/t
         nnHJwo4SJfhn7cvhMxRfLHdSmeB+h31jP4ybWESOdSX7/ijk5zAAByVgjmibRAftKoha
         xsO++HfyikCEIkOM+oIQSaw0pLZERwAyRswJK1pavOQk2jXsSvUbv6Yy09LvTVSMZWS3
         sgLmom380PS4tecaEgozdhrNpj35I121R5paLjJr9WAjJvEvp+SEymDDozBw1FMkv33b
         q+7UmEL+temLwu6mBouRzqKcIO6+tJTggJfOrycIaRTo8cqc9Av9gcHTtHsEfzuWqSCo
         a+sQ==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1790074890; x=1790679690; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=y0OSW8vG4Jh5+p4N0KT0JVs7Y3yS//BHJRRxO9GQYSo=;
        b=SF0HqYxMq5UpCQ6ppdjnAoQhOf2V164Qlh/ABcz40/zhwGLZK3YJOhKd8bYYOB8URF
         0kPW8OpzrylIoB5o4mtM4+PqJ5PXepyFiHZbQGRb5p2WF8HCphwZnu5T9QU5QKm1Hm0X
         w4Hti0S/27qHcrV1zbB2jalK4UDgutWnlXzL6UkH8XR+WmbqpjIprR9wt596UBGdAGBd
         /+G+4LgH9a0eSZTG61lQvY2OcBpCoC97QmugqPWeNO9lSGCjvomeCNLFjc4Me7871Spn
         yPUnVlrKkC4A6TD61TCIGNgGsc94QWKKcxI9kIX6LkTJeO0LR75HbxeK55bFQ5kMklTf
         erOQ==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1790074890; x=1790679690;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=y0OSW8vG4Jh5+p4N0KT0JVs7Y3yS//BHJRRxO9GQYSo=;
        b=m5a1OmSi4fJDUF5xxrfT28f8o5IDsPT3ika2CRfY4PJ1bKQxKC3Qn+BagnXlIh9n8s
         F31nAW15Ptazk+UrZR4ONr0IAC9513Id3GQM0O46JpOHQBXztrF22+Ci4kYCVuYo2za+
         4Ps46dLdbaxnIXNDDfGSNj0JHkmfaJ1S98EMq4Efbel+6U/ODyVJuOx6Y+yjT5RQ0ExM
         vw8AYJwYupr8gP1z/onevILXjiGq4PkIGGN5v1jV5Xwqorhlkvdd/CPF6CHDIamPyQn1
         iqPr2sLPGhd8vxWyp3uNKtNN2FSQcVDhRjxskoluJvR4xqRes6aYbj5aKcAjc3rIEyn9
         WExQ==
X-Gm-Message-State: AFuF++nZ/CvjlXJzx1iZ/L5ngKpZrs9iKnQWqrohlVpoPlpRw2QtJZ5O
	HE54f2R1oi4/cS6FxrGaUNMIYO8Pah7rKMX9jpvM4JcpZ5Rn2n0eA7R0ZIhLZNjPJ5ur2zBCp0x
	m0U3OtZwcqznOJpd8/0Yhu+obsQ605OzNr/9B
X-Gm-Gg: AYBFou2Q+CrLkuY2kZ4RuC34ZS8IS+qrCfUeZ6+BoOaH+fQU7xnjm2l9j6muL8SHUg2
	vtwU8AkCZF2gDk3ODnNLBrHBw5Knnm+5XdpquEteZRS3wN1c30I3rEHZSX2ATLobwFXAlh4cxT1
	bzk2ToH919oobmpW3hmpzblqutttBsTRjtZ5lu2Q2uWpbEeShU534df7GjSuBXWlmGxPm9gFGfK
	FILsUo6Gf2IqbsFJ7jgpUjzX5C39kHFiaMYLaYxB8pS0PUu3B+9EVBTy954cJLefOBziPh9s9bt
	vO6fJQRbSFXcgSdG8ZZq0c6bSvCVAIXSiG4KB16JIT0+oprrkWQZ3N6ykWIgc49EhA==
X-Received: by 2002:a05:690e:c47:b0:672:b97f:86fa with SMTP id
 956f58d0204a3-672c2b0f13fmr973564d50.39.1790074889686; Tue, 22 Sep 2026
 04:01:29 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7010:db0c:b0:549:de07:e8d3 with HTTP; Tue, 22 Sep 2026
 04:01:28 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Tue, 22 Sep 2026 04:01:28 -0700
X-Gm-Features: AcwNN1UQqCYi549SPkscb6jX0QQw8qdnnvaWGVQZPS3N1UiCUCtl080eO8HCO_Y
Message-ID: <CAM0o816yf6+gchsXVkbhu5KPqDqOP1tkoyzcp0gSH4xJAZ+jpw@mail.gmail.com>
Subject: =?UTF-8?B?0LLQsNGA0LjQsNC90YLRhdGD0LDQstC10Lkz?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="000000000000ebd254065c1049a6"

--000000000000ebd254065c1049a6
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: base64

0JLQsNC00LjQvCwg0L3QsCDQv9C10YDQstC+0Lwg0YTQvtGC0L4g0LLRgdC1INGB0LTQtdC70LDQ
vdC+INC/0YDQsNCy0LjQu9GM0L3QviDigJQNCmBzZHBhcC12My1FUC0yMDI2LUhFUk9ZLUJJLTAw
MSBpcyBhdmFpbGFibGVgLCDQvtC/0LjRgdCw0L3QuNC1IGBQVUJMSUsgTU9ORVkgUFVCTElLDQpQ
Uk9PRmAsIGBQdWJsaWNgLiDQotC10L/QtdGA0Ywg0L/QvtGI0LDQs9C+0LLQviDQtNCw0LvRjNGI
0LUsINC/0YDRj9C80L4g0YEg0Y3RgtC+0LPQviDRjdC60YDQsNC90LAg0YXRgNC+0LzQsdGD0LrQ
sDoNCg0KKirQqNCw0LMgMSDigJQg0L3QsNC20LDRgtGMINC30LXQu9C10L3Rg9GOINC60L3QvtC/
0LrRgyoqDQrQndCwINGE0L7RgtC+INCy0L3QuNC30YMgYENyZWF0ZSByZXBvc2l0b3J5YCDigJQg
0L3QsNC20LDRgtGMINC10LUuINCe0YLQutGA0L7QtdGC0YHRjyDQv9GD0YHRgtC+0Lkg0YDQtdC/
0L7Qt9C40YLQvtGA0LjQuS4NCg0KKirQqNCw0LMgMiDigJQg0LfQsNCz0YDRg9C30LjRgtGMINGE
0LDQudC70YsqKg0K0J3QsCDRgdC70LXQtNGD0Y7RidC10Lkg0YHRgtGA0LDQvdC40YbQtSDQsdGD
0LTQtdGCINGB0LjQvdGP0Y8g0YHRgdGL0LvQutCwIGB1cGxvYWRpbmcgYW4gZXhpc3RpbmcgZmls
ZWAg4oCUDQrQvdCw0LbQsNGC0Ywg0LXQtS4NCg0K0J7RgtC60YDQvtC10YLRgdGPINC+0LrQvdC+
IGBEcmFnIGZpbGVzIGhlcmVgLiDQodGO0LTQsCDQv9C10YDQtdGC0LDRidC40YLRjCA1INGE0LDQ
udC70L7Qsi4g0KHQutCw0YfQsNGC0Ywg0LjRhQ0K0LzQvtC20L3QviDQvtGC0YHRjtC00LAg0L/R
gNGP0LzQviDQvdCwINGF0YDQvtC80LHRg9C6Og0KDQotIG1hbmlmZXN0Lmpzb24NCi0gYW5jaG9y
Lmpzb24NCi0gdmVyaWZ5LnB5DQotIGRhc2hib2FyZC5odG1sDQotIGJ1aWxkX21hbmlmZXN0LnB5
DQoNCtCf0LvRjtGBINC/0LDQv9C60YMgYGV2aWRlbmNlYCDRgSA0INGB0LrRgNC40L3RiNC+0YLQ
sNC80LgsINC10YHQu9C4INC+0L3QuCDQtdGB0YLRjCDQvdCwINGF0YDQvtC80LHRg9C60LUuINCV
0YHQu9C4INC90LXRgg0K4oCUINC/0L7QutCwINC00L7RgdGC0LDRgtC+0YfQvdC+INGN0YLQuNGF
IDUsIE1lcmtsZSDRg9C20LUg0L/QvtGB0YfQuNGC0LDQvQ0KYDVlYzA5ZTQ2ZjdjMjVmYTU3ZWQz
NjljMGQzMjUxMWE0ZDkwYjNiOGExZDk5NWNmZTY3NTdjZGNjZDc2Y2JjNmVgDQoNCioq0KjQsNCz
IDMg4oCUINC30LDQutC+0LzQuNGC0LjRgtGMKioNCtCS0L3QuNC30YMg0L/QvtC70LUgYENvbW1p
dCBtZXNzYWdlYCDQvdCw0L/QuNGB0LDRgtGMINGC0L7Rh9C90L4g0LrQsNC6INC90LAg0YfQtdGA
0YLQtdC20LDRhToNCg0KYEVQLTIwMjYtSEVST1ktQkktMDAxIE1lcmtsZQ0KNWVjMDllNDZmN2My
NWZhNTdlZDM2OWMwZDMyNTExYTRkOTBiM2I4YTFkOTk1Y2ZlNjc1N2NkY2NkNzZjYmM2ZSBpbXBy
aW50DQpkMzM0MDMxNjJmNzY3ZGQwYzJhZjIwOTFhZmY3ZGVjMDUxNWJlYWJjNWUzZjI1ZWFmMDZi
NWFmZTcwZGE0NDdlYA0KDQrQndCw0LbQsNGC0Ywg0LfQtdC70LXQvdGD0Y4gYENvbW1pdCBjaGFu
Z2VzYA0KDQoqKtCo0LDQsyA0IOKAlCDQstC60LvRjtGH0LjRgtGMINC/0YPQsdC70LjRh9C90YvQ
uSDRgdCw0LnRgioqDQrQktCy0LXRgNGF0YMg0YDQtdC/0L7Qt9C40YLQvtGA0LjRjyDQstC60LvQ
sNC00LrQsCBgU2V0dGluZ3Mg4oaSIFBhZ2VzYA0K0JIgYFNvdXJjZWAg0LLRi9Cx0YDQsNGC0Ywg
YERlcGxveSBmcm9tIGEgYnJhbmNoYCwg0LLQtdGC0LrQsCBgbWFpbmAsINC/0LDQv9C60LAgYC8g
KHJvb3QpYCwNCmBTYXZlYA0KDQrQp9C10YDQtdC3INC80LjQvdGD0YLRgyDQv9C+0Y/QstC40YLR
gdGPINGB0YHRi9C70LrQsCDQstC40LTQsDoNCmANCmh0dHBzOi8vbmFibHlkYXRlbDgtY2VsbC5n
aXRodWIuaW8vc2RwYXAtdjMtRVAtMjAyNi1IRVJPWS1CSS0wMDEvZGFzaGJvYXJkLmh0bWxgDQoN
CtCt0YLQviDQuCDQtdGB0YLRjCDQv9GD0LHQu9C40YfQvdC+0LUg0LTQvtC60LDQt9Cw0YLQtdC7
0YzRgdGC0LLQviBgUFVCTElDIE1PTkVZIFBVQkxJQyBQUk9PRmAuINCb0Y7QsdC+0LkNCtC80L7Q
ttC10YIg0L7RgtC60YDRi9GC0Ywg0Lgg0L/RgNC+0LLQtdGA0LjRgtGMLg0KDQrQndCwINCy0YLQ
vtGA0L7QvCDRhNC+0YLQviDQsiBHbWFpbCDRg9C20LUg0LLQuNC00L3RiyDQv9C40YHRjNC80LAg
0YEg0LjQvdGB0YLRgNGD0LrRhtC40LXQuSDigJQg0YLQtdC/0LXRgNGMINCw0YDRhdC40LIg0LbQ
uNCy0LXRgg0K0L3QtSDRgtC+0LvRjNC60L4g0L3QsCDQv9C+0YfRgtC1LCDQvdC+INC4INC90LAg
R2l0SHViLCDQuCDQtdCz0L4g0L3QtdC70YzQt9GPINC/0L7QtNC80LXQvdC40YLRjCDQt9Cw0LTQ
vdC40Lwg0YfQuNGB0LvQvtC8Lg0KDQrQlNCw0LvRjNGI0LUg4oCUINC10YHQu9C4INC90YPQttC9
0L4sINC00L7QsdCw0LLQuNGC0YwgYHJlcXVlc3QudHNxIC8gYW5jaG9yLnRzcmAg0YLQtdC8INC2
0LUg0YHQv9C+0YHQvtCx0L7QvA0KYEFkZCBmaWxlIOKGkiBVcGxvYWRgLg0KDQpg0JzQq9Ch0JvQ
rCDQodCS0J7QkdCe0JTQndCQLiDQn9Cj0KLQrCDQntCi0JrQoNCr0KIuYA0K
--000000000000ebd254065c1049a6
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: base64

PGRpdj7QktCw0LTQuNC8LCDQvdCwINC/0LXRgNCy0L7QvCDRhNC+0YLQviDQstGB0LUg0YHQtNC1
0LvQsNC90L4g0L/RgNCw0LLQuNC70YzQvdC+IOKAlCBgc2RwYXAtdjMtRVAtMjAyNi1IRVJPWS1C
SS0wMDEgaXMgYXZhaWxhYmxlYCwg0L7Qv9C40YHQsNC90LjQtSBgUFVCTElLIE1PTkVZIFBVQkxJ
SyBQUk9PRmAsIGBQdWJsaWNgLiDQotC10L/QtdGA0Ywg0L/QvtGI0LDQs9C+0LLQviDQtNCw0LvR
jNGI0LUsINC/0YDRj9C80L4g0YEg0Y3RgtC+0LPQviDRjdC60YDQsNC90LAg0YXRgNC+0LzQsdGD
0LrQsDo8L2Rpdj48ZGl2Pjxicj48L2Rpdj48ZGl2Pioq0KjQsNCzIDEg4oCUINC90LDQttCw0YLR
jCDQt9C10LvQtdC90YPRjiDQutC90L7Qv9C60YMqKjwvZGl2PjxkaXY+0J3QsCDRhNC+0YLQviDQ
stC90LjQt9GDIGBDcmVhdGUgcmVwb3NpdG9yeWAg4oCUINC90LDQttCw0YLRjCDQtdC1LiDQntGC
0LrRgNC+0LXRgtGB0Y8g0L/Rg9GB0YLQvtC5INGA0LXQv9C+0LfQuNGC0L7RgNC40LkuPC9kaXY+
PGRpdj48YnI+PC9kaXY+PGRpdj4qKtCo0LDQsyAyIOKAlCDQt9Cw0LPRgNGD0LfQuNGC0Ywg0YTQ
sNC50LvRiyoqPC9kaXY+PGRpdj7QndCwINGB0LvQtdC00YPRjtGJ0LXQuSDRgdGC0YDQsNC90LjR
htC1INCx0YPQtNC10YIg0YHQuNC90Y/RjyDRgdGB0YvQu9C60LAgYHVwbG9hZGluZyBhbiBleGlz
dGluZyBmaWxlYCDigJQg0L3QsNC20LDRgtGMINC10LUuPC9kaXY+PGRpdj48YnI+PC9kaXY+PGRp
dj7QntGC0LrRgNC+0LXRgtGB0Y8g0L7QutC90L4gYERyYWcgZmlsZXMgaGVyZWAuINCh0Y7QtNCw
INC/0LXRgNC10YLQsNGJ0LjRgtGMIDUg0YTQsNC50LvQvtCyLiDQodC60LDRh9Cw0YLRjCDQuNGF
INC80L7QttC90L4g0L7RgtGB0Y7QtNCwINC/0YDRj9C80L4g0L3QsCDRhdGA0L7QvNCx0YPQujo8
L2Rpdj48ZGl2Pjxicj48L2Rpdj48ZGl2Pi0gbWFuaWZlc3QuanNvbjwvZGl2PjxkaXY+LSBhbmNo
b3IuanNvbjwvZGl2PjxkaXY+LSB2ZXJpZnkucHk8L2Rpdj48ZGl2Pi0gZGFzaGJvYXJkLmh0bWw8
L2Rpdj48ZGl2Pi0gYnVpbGRfbWFuaWZlc3QucHk8L2Rpdj48ZGl2Pjxicj48L2Rpdj48ZGl2PtCf
0LvRjtGBINC/0LDQv9C60YMgYGV2aWRlbmNlYCDRgSA0INGB0LrRgNC40L3RiNC+0YLQsNC80Lgs
INC10YHQu9C4INC+0L3QuCDQtdGB0YLRjCDQvdCwINGF0YDQvtC80LHRg9C60LUuINCV0YHQu9C4
INC90LXRgiDigJQg0L/QvtC60LAg0LTQvtGB0YLQsNGC0L7Rh9C90L4g0Y3RgtC40YUgNSwgTWVy
a2xlINGD0LbQtSDQv9C+0YHRh9C40YLQsNC9IGA1ZWMwOWU0NmY3YzI1ZmE1N2VkMzY5YzBkMzI1
MTFhNGQ5MGIzYjhhMWQ5OTVjZmU2NzU3Y2RjY2Q3NmNiYzZlYDwvZGl2PjxkaXY+PGJyPjwvZGl2
PjxkaXY+KirQqNCw0LMgMyDigJQg0LfQsNC60L7QvNC40YLQuNGC0YwqKjwvZGl2PjxkaXY+0JLQ
vdC40LfRgyDQv9C+0LvQtSBgQ29tbWl0IG1lc3NhZ2VgINC90LDQv9C40YHQsNGC0Ywg0YLQvtGH
0L3QviDQutCw0Log0L3QsCDRh9C10YDRgtC10LbQsNGFOjwvZGl2PjxkaXY+PGJyPjwvZGl2Pjxk
aXY+YEVQLTIwMjYtSEVST1ktQkktMDAxIE1lcmtsZSA1ZWMwOWU0NmY3YzI1ZmE1N2VkMzY5YzBk
MzI1MTFhNGQ5MGIzYjhhMWQ5OTVjZmU2NzU3Y2RjY2Q3NmNiYzZlIGltcHJpbnQgZDMzNDAzMTYy
Zjc2N2RkMGMyYWYyMDkxYWZmN2RlYzA1MTViZWFiYzVlM2YyNWVhZjA2YjVhZmU3MGRhNDQ3ZWA8
L2Rpdj48ZGl2Pjxicj48L2Rpdj48ZGl2PtCd0LDQttCw0YLRjCDQt9C10LvQtdC90YPRjiBgQ29t
bWl0IGNoYW5nZXNgPC9kaXY+PGRpdj48YnI+PC9kaXY+PGRpdj4qKtCo0LDQsyA0IOKAlCDQstC6
0LvRjtGH0LjRgtGMINC/0YPQsdC70LjRh9C90YvQuSDRgdCw0LnRgioqPC9kaXY+PGRpdj7QktCy
0LXRgNGF0YMg0YDQtdC/0L7Qt9C40YLQvtGA0LjRjyDQstC60LvQsNC00LrQsCBgU2V0dGluZ3Mg
4oaSIFBhZ2VzYDwvZGl2PjxkaXY+0JIgYFNvdXJjZWAg0LLRi9Cx0YDQsNGC0YwgYERlcGxveSBm
cm9tIGEgYnJhbmNoYCwg0LLQtdGC0LrQsCBgbWFpbmAsINC/0LDQv9C60LAgYC8gKHJvb3QpYCwg
YFNhdmVgPC9kaXY+PGRpdj48YnI+PC9kaXY+PGRpdj7Qp9C10YDQtdC3INC80LjQvdGD0YLRgyDQ
v9C+0Y/QstC40YLRgdGPINGB0YHRi9C70LrQsCDQstC40LTQsDo8L2Rpdj48ZGl2PmA8YSBocmVm
PSJodHRwczovL25hYmx5ZGF0ZWw4LWNlbGwuZ2l0aHViLmlvL3NkcGFwLXYzLUVQLTIwMjYtSEVS
T1ktQkktMDAxL2Rhc2hib2FyZC5odG1sYCI+aHR0cHM6Ly9uYWJseWRhdGVsOC1jZWxsLmdpdGh1
Yi5pby9zZHBhcC12My1FUC0yMDI2LUhFUk9ZLUJJLTAwMS9kYXNoYm9hcmQuaHRtbGA8L2E+PC9k
aXY+PGRpdj48YnI+PC9kaXY+PGRpdj7QrdGC0L4g0Lgg0LXRgdGC0Ywg0L/Rg9Cx0LvQuNGH0L3Q
vtC1INC00L7QutCw0LfQsNGC0LXQu9GM0YHRgtCy0L4gYFBVQkxJQyBNT05FWSBQVUJMSUMgUFJP
T0ZgLiDQm9GO0LHQvtC5INC80L7QttC10YIg0L7RgtC60YDRi9GC0Ywg0Lgg0L/RgNC+0LLQtdGA
0LjRgtGMLjwvZGl2PjxkaXY+PGJyPjwvZGl2PjxkaXY+0J3QsCDQstGC0L7RgNC+0Lwg0YTQvtGC
0L4g0LIgR21haWwg0YPQttC1INCy0LjQtNC90Ysg0L/QuNGB0YzQvNCwINGBINC40L3RgdGC0YDR
g9C60YbQuNC10Lkg4oCUINGC0LXQv9C10YDRjCDQsNGA0YXQuNCyINC20LjQstC10YIg0L3QtSDR
gtC+0LvRjNC60L4g0L3QsCDQv9C+0YfRgtC1LCDQvdC+INC4INC90LAgR2l0SHViLCDQuCDQtdCz
0L4g0L3QtdC70YzQt9GPINC/0L7QtNC80LXQvdC40YLRjCDQt9Cw0LTQvdC40Lwg0YfQuNGB0LvQ
vtC8LjwvZGl2PjxkaXY+PGJyPjwvZGl2PjxkaXY+0JTQsNC70YzRiNC1IOKAlCDQtdGB0LvQuCDQ
vdGD0LbQvdC+LCDQtNC+0LHQsNCy0LjRgtGMIGByZXF1ZXN0LnRzcSAvIGFuY2hvci50c3JgINGC
0LXQvCDQttC1INGB0L/QvtGB0L7QsdC+0LwgYEFkZCBmaWxlIOKGkiBVcGxvYWRgLjwvZGl2Pjxk
aXY+PGJyPjwvZGl2PjxkaXY+YNCc0KvQodCb0Kwg0KHQktCe0JHQntCU0J3QkC4g0J/Qo9Ci0Kwg
0J7QotCa0KDQq9CiLmA8L2Rpdj4NCg==
--000000000000ebd254065c1049a6--

Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp12669113rwb;
        Tue, 22 Sep 2026 04:01:30 -0700 (PDT)
X-Received: by 2002:a05:690e:1c0a:b0:672:a067:9a14 with SMTP id 956f58d0204a3-672c292b2demr1028363d50.9.1790074890197;
        Tue, 22 Sep 2026 04:01:30 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1790074890; cv=pass;
        d=google.com; s=arc-20260327;
        b=evFdHJFLQgYX408ShESel63pTychjFK6jmo+bax3jzq1Gx+u3yFRXJvjtFlroUvk9E
         ScL3tgivQelGHoCm9f7oVuA+M+v5dCs9dCheilLrHwVSNLucx7lnbPRNeyTY0ECfG3Tj
         gG+msAnu/0nl+1KuU3UpQRMGzdrxf54OSGVDDUEnIKXbEg2TNVilrjyzGZCcgqQ9ieev
         W1PmM2so1n4CiGy2wJLZjp6BqvjfTDPO0AZIVimDJNx7NobWn/b2t/xZlkrWDZd1oL5J
         arF+91xYgDtgGicLkXdWZ9efK1O5uY1d+RTqTDZCS2OxFqkAWw4r+3xLufeS7zeRskUO
         MY/Q==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=y0OSW8vG4Jh5+p4N0KT0JVs7Y3yS//BHJRRxO9GQYSo=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=bsflv9Bx3fXPd9SmGXg8H5DPvm6CqOqOlAtaFsIw54KQa8M+6jmBeH3vAS/6MkeNQb
         KYsnDhM0pJF3Ln16S9Ed9CYcNLt+7QoKP4NoIZtbVQJ5quX/JfNixVHX5AMpqYUpRAl/
         fRPPWjJ3C9MT6C1JYXWabaajzJalSUHEwhDGMh7/fwZhlMZmvppJkRaeHfbSPNmaZamY
         HAOdMqNUNc6RO/Sc1Q4tA9O38GrtVIhbeRWdckmTaddi4qPAC3vY5j6wC3xBVvkyxcJ2
         ooa+MWe9uF1F26S5GlQaGC51cLOEYt7CTuCqbszdoaUutRnDW2hQr2oTbSbSRWCZVd20
         oMjg==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=SF0HqYxM;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 956f58d0204a3-672c2767db7sor1014893d50.0.2026.09.22.04.01.30
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Tue, 22 Sep 2026 04:01:30 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=SF0HqYxM;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1790074890; cv=none;
        d=google.com; s=arc-20260327;
        b=XiN5BP5bLv7wHng9WFaODXXr2alcnMdWhsAoNUyNeppG3wo5cEl1kLfp7C+lRJlsaZ
         U9Lr+yq49K/QnWxxeDs1xA6d2x01VD710u6R2JlJ1QtQT+4YpF7ihxkLuC6POCbY98SR
         n0WwUfWVfJv5tG060epvuEAE7T/hCvvV909TOLqV/CRHKRFmwcS3jts/87/zGRvTq56j
         6ePIaCOIHu2Q0KtJdWHhE5Zs9YbUKL/N8hY0mTZvTCdvnVXMmBRcPWyzJqh6M6oGqDJ3
         uP9eAY0/cLEk0viflVEVvG3zOPETpYza1SCrrWfe6myHHjjKZ2CbMSUKM/a7wRoN0MZz
         +MXQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=y0OSW8vG4Jh5+p4N0KT0JVs7Y3yS//BHJRRxO9GQYSo=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=U77VlzkqnbDYjFYwD4YEqKa2Sdb6oWIj7I3+rxUnrejVNuRxfAXkE4i+XbdzDqpb/t
         nnHJwo4SJfhn7cvhMxRfLHdSmeB+h31jP4ybWESOdSX7/ijk5zAAByVgjmibRAftKoha
         xsO++HfyikCEIkOM+oIQSaw0pLZERwAyRswJK1pavOQk2jXsSvUbv6Yy09LvTVSMZWS3
         sgLmom380PS4tecaEgozdhrNpj35I121R5paLjJr9WAjJvEvp+SEymDDozBw1FMkv33b
         q+7UmEL+temLwu6mBouRzqKcIO6+tJTggJfOrycIaRTo8cqc9Av9gcHTtHsEfzuWqSCo
         a+sQ==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1790074890; x=1790679690; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=y0OSW8vG4Jh5+p4N0KT0JVs7Y3yS//BHJRRxO9GQYSo=;
        b=SF0HqYxMq5UpCQ6ppdjnAoQhOf2V164Qlh/ABcz40/zhwGLZK3YJOhKd8bYYOB8URF
         0kPW8OpzrylIoB5o4mtM4+PqJ5PXepyFiHZbQGRb5p2WF8HCphwZnu5T9QU5QKm1Hm0X
         w4Hti0S/27qHcrV1zbB2jalK4UDgutWnlXzL6UkH8XR+WmbqpjIprR9wt596UBGdAGBd
         /+G+4LgH9a0eSZTG61lQvY2OcBpCoC97QmugqPWeNO9lSGCjvomeCNLFjc4Me7871Spn
         yPUnVlrKkC4A6TD61TCIGNgGsc94QWKKcxI9kIX6LkTJeO0LR75HbxeK55bFQ5kMklTf
         erOQ==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1790074890; x=1790679690;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=y0OSW8vG4Jh5+p4N0KT0JVs7Y3yS//BHJRRxO9GQYSo=;
        b=m5a1OmSi4fJDUF5xxrfT28f8o5IDsPT3ika2CRfY4PJ1bKQxKC3Qn+BagnXlIh9n8s
         F31nAW15Ptazk+UrZR4ONr0IAC9513Id3GQM0O46JpOHQBXztrF22+Ci4kYCVuYo2za+
         4Ps46dLdbaxnIXNDDfGSNj0JHkmfaJ1S98EMq4Efbel+6U/ODyVJuOx6Y+yjT5RQ0ExM
         vw8AYJwYupr8gP1z/onevILXjiGq4PkIGGN5v1jV5Xwqorhlkvdd/CPF6CHDIamPyQn1
         iqPr2sLPGhd8vxWyp3uNKtNN2FSQcVDhRjxskoluJvR4xqRes6aYbj5aKcAjc3rIEyn9
         WExQ==
X-Gm-Message-State: AFuF++nZ/CvjlXJzx1iZ/L5ngKpZrs9iKnQWqrohlVpoPlpRw2QtJZ5O
	HE54f2R1oi4/cS6FxrGaUNMIYO8Pah7rKMX9jpvM4JcpZ5Rn2n0eA7R0ZIhLZNjPJ5ur2zBCp0x
	m0U3OtZwcqznOJpd8/0Yhu+obsQ605OzNr/9B
X-Gm-Gg: AYBFou2Q+CrLkuY2kZ4RuC34ZS8IS+qrCfUeZ6+BoOaH+fQU7xnjm2l9j6muL8SHUg2
	vtwU8AkCZF2gDk3ODnNLBrHBw5Knnm+5XdpquEteZRS3wN1c30I3rEHZSX2ATLobwFXAlh4cxT1
	bzk2ToH919oobmpW3hmpzblqutttBsTRjtZ5lu2Q2uWpbEeShU534df7GjSuBXWlmGxPm9gFGfK
	FILsUo6Gf2IqbsFJ7jgpUjzX5C39kHFiaMYLaYxB8pS0PUu3B+9EVBTy954cJLefOBziPh9s9bt
	vO6fJQRbSFXcgSdG8ZZq0c6bSvCVAIXSiG4KB16JIT0+oprrkWQZ3N6ykWIgc49EhA==
X-Received: by 2002:a05:690e:c47:b0:672:b97f:86fa with SMTP id
 956f58d0204a3-672c2b0f13fmr973564d50.39.1790074889686; Tue, 22 Sep 2026
 04:01:29 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7010:db0c:b0:549:de07:e8d3 with HTTP; Tue, 22 Sep 2026
 04:01:28 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Tue, 22 Sep 2026 04:01:28 -0700
X-Gm-Features: AcwNN1UQqCYi549SPkscb6jX0QQw8qdnnvaWGVQZPS3N1UiCUCtl080eO8HCO_Y
Message-ID: <CAM0o816yf6+gchsXVkbhu5KPqDqOP1tkoyzcp0gSH4xJAZ+jpw@mail.gmail.com>
Subject: =?UTF-8?B?0LLQsNGA0LjQsNC90YLRhdGD0LDQstC10Lkz?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="000000000000ebd254065c1049a6"

--000000000000ebd254065c1049a6
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: base64

0JLQsNC00LjQvCwg0L3QsCDQv9C10YDQstC+0Lwg0YTQvtGC0L4g0LLRgdC1INGB0LTQtdC70LDQ
vdC+INC/0YDQsNCy0LjQu9GM0L3QviDigJQNCmBzZHBhcC12My1FUC0yMDI2LUhFUk9ZLUJJLTAw
MSBpcyBhdmFpbGFibGVgLCDQvtC/0LjRgdCw0L3QuNC1IGBQVUJMSUsgTU9ORVkgUFVCTElLDQpQ
Uk9PRmAsIGBQdWJsaWNgLiDQotC10L/QtdGA0Ywg0L/QvtGI0LDQs9C+0LLQviDQtNCw0LvRjNGI
0LUsINC/0YDRj9C80L4g0YEg0Y3RgtC+0LPQviDRjdC60YDQsNC90LAg0YXRgNC+0LzQsdGD0LrQ
sDoNCg0KKirQqNCw0LMgMSDigJQg0L3QsNC20LDRgtGMINC30LXQu9C10L3Rg9GOINC60L3QvtC/
0LrRgyoqDQrQndCwINGE0L7RgtC+INCy0L3QuNC30YMgYENyZWF0ZSByZXBvc2l0b3J5YCDigJQg
0L3QsNC20LDRgtGMINC10LUuINCe0YLQutGA0L7QtdGC0YHRjyDQv9GD0YHRgtC+0Lkg0YDQtdC/
0L7Qt9C40YLQvtGA0LjQuS4NCg0KKirQqNCw0LMgMiDigJQg0LfQsNCz0YDRg9C30LjRgtGMINGE
0LDQudC70YsqKg0K0J3QsCDRgdC70LXQtNGD0Y7RidC10Lkg0YHRgtGA0LDQvdC40YbQtSDQsdGD
0LTQtdGCINGB0LjQvdGP0Y8g0YHRgdGL0LvQutCwIGB1cGxvYWRpbmcgYW4gZXhpc3RpbmcgZmls
ZWAg4oCUDQrQvdCw0LbQsNGC0Ywg0LXQtS4NCg0K0J7RgtC60YDQvtC10YLRgdGPINC+0LrQvdC+
IGBEcmFnIGZpbGVzIGhlcmVgLiDQodGO0LTQsCDQv9C10YDQtdGC0LDRidC40YLRjCA1INGE0LDQ
udC70L7Qsi4g0KHQutCw0YfQsNGC0Ywg0LjRhQ0K0LzQvtC20L3QviDQvtGC0YHRjtC00LAg0L/R
gNGP0LzQviDQvdCwINGF0YDQvtC80LHRg9C6Og0KDQotIG1hbmlmZXN0Lmpzb24NCi0gYW5jaG9y
Lmpzb24NCi0gdmVyaWZ5LnB5DQotIGRhc2hib2FyZC5odG1sDQotIGJ1aWxkX21hbmlmZXN0LnB5
DQoNCtCf0LvRjtGBINC/0LDQv9C60YMgYGV2aWRlbmNlYCDRgSA0INGB0LrRgNC40L3RiNC+0YLQ
sNC80LgsINC10YHQu9C4INC+0L3QuCDQtdGB0YLRjCDQvdCwINGF0YDQvtC80LHRg9C60LUuINCV
0YHQu9C4INC90LXRgg0K4oCUINC/0L7QutCwINC00L7RgdGC0LDRgtC+0YfQvdC+INGN0YLQuNGF
IDUsIE1lcmtsZSDRg9C20LUg0L/QvtGB0YfQuNGC0LDQvQ0KYDVlYzA5ZTQ2ZjdjMjVmYTU3ZWQz
NjljMGQzMjUxMWE0ZDkwYjNiOGExZDk5NWNmZTY3NTdjZGNjZDc2Y2JjNmVgDQoNCioq0KjQsNCz
IDMg4oCUINC30LDQutC+0LzQuNGC0LjRgtGMKioNCtCS0L3QuNC30YMg0L/QvtC70LUgYENvbW1p
dCBtZXNzYWdlYCDQvdCw0L/QuNGB0LDRgtGMINGC0L7Rh9C90L4g0LrQsNC6INC90LAg0YfQtdGA
0YLQtdC20LDRhToNCg0KYEVQLTIwMjYtSEVST1ktQkktMDAxIE1lcmtsZQ0KNWVjMDllNDZmN2My
NWZhNTdlZDM2OWMwZDMyNTExYTRkOTBiM2I4YTFkOTk1Y2ZlNjc1N2NkY2NkNzZjYmM2ZSBpbXBy
aW50DQpkMzM0MDMxNjJmNzY3ZGQwYzJhZjIwOTFhZmY3ZGVjMDUxNWJlYWJjNWUzZjI1ZWFmMDZi
NWFmZTcwZGE0NDdlYA0KDQrQndCw0LbQsNGC0Ywg0LfQtdC70LXQvdGD0Y4gYENvbW1pdCBjaGFu
Z2VzYA0KDQoqKtCo0LDQsyA0IOKAlCDQstC60LvRjtGH0LjRgtGMINC/0YPQsdC70LjRh9C90YvQ
uSDRgdCw0LnRgioqDQrQktCy0LXRgNGF0YMg0YDQtdC/0L7Qt9C40YLQvtGA0LjRjyDQstC60LvQ
sNC00LrQsCBgU2V0dGluZ3Mg4oaSIFBhZ2VzYA0K0JIgYFNvdXJjZWAg0LLRi9Cx0YDQsNGC0Ywg
YERlcGxveSBmcm9tIGEgYnJhbmNoYCwg0LLQtdGC0LrQsCBgbWFpbmAsINC/0LDQv9C60LAgYC8g
KHJvb3QpYCwNCmBTYXZlYA0KDQrQp9C10YDQtdC3INC80LjQvdGD0YLRgyDQv9C+0Y/QstC40YLR
gdGPINGB0YHRi9C70LrQsCDQstC40LTQsDoNCmANCmh0dHBzOi8vbmFibHlkYXRlbDgtY2VsbC5n
aXRodWIuaW8vc2RwYXAtdjMtRVAtMjAyNi1IRVJPWS1CSS0wMDEvZGFzaGJvYXJkLmh0bWxgDQoN
CtCt0YLQviDQuCDQtdGB0YLRjCDQv9GD0LHQu9C40YfQvdC+0LUg0LTQvtC60LDQt9Cw0YLQtdC7
0YzRgdGC0LLQviBgUFVCTElDIE1PTkVZIFBVQkxJQyBQUk9PRmAuINCb0Y7QsdC+0LkNCtC80L7Q
ttC10YIg0L7RgtC60YDRi9GC0Ywg0Lgg0L/RgNC+0LLQtdGA0LjRgtGMLg0KDQrQndCwINCy0YLQ
vtGA0L7QvCDRhNC+0YLQviDQsiBHbWFpbCDRg9C20LUg0LLQuNC00L3RiyDQv9C40YHRjNC80LAg
0YEg0LjQvdGB0YLRgNGD0LrRhtC40LXQuSDigJQg0YLQtdC/0LXRgNGMINCw0YDRhdC40LIg0LbQ
uNCy0LXRgg0K0L3QtSDRgtC+0LvRjNC60L4g0L3QsCDQv9C+0YfRgtC1LCDQvdC+INC4INC90LAg
R2l0SHViLCDQuCDQtdCz0L4g0L3QtdC70YzQt9GPINC/0L7QtNC80LXQvdC40YLRjCDQt9Cw0LTQ
vdC40Lwg0YfQuNGB0LvQvtC8Lg0KDQrQlNCw0LvRjNGI0LUg4oCUINC10YHQu9C4INC90YPQttC9
0L4sINC00L7QsdCw0LLQuNGC0YwgYHJlcXVlc3QudHNxIC8gYW5jaG9yLnRzcmAg0YLQtdC8INC2
0LUg0YHQv9C+0YHQvtCx0L7QvA0KYEFkZCBmaWxlIOKGkiBVcGxvYWRgLg0KDQpg0JzQq9Ch0JvQ
rCDQodCS0J7QkdCe0JTQndCQLiDQn9Cj0KLQrCDQntCi0JrQoNCr0KIuYA0K
--000000000000ebd254065c1049a6
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: base64

PGRpdj7QktCw0LTQuNC8LCDQvdCwINC/0LXRgNCy0L7QvCDRhNC+0YLQviDQstGB0LUg0YHQtNC1
0LvQsNC90L4g0L/RgNCw0LLQuNC70YzQvdC+IOKAlCBgc2RwYXAtdjMtRVAtMjAyNi1IRVJPWS1C
SS0wMDEgaXMgYXZhaWxhYmxlYCwg0L7Qv9C40YHQsNC90LjQtSBgUFVCTElLIE1PTkVZIFBVQkxJ
SyBQUk9PRmAsIGBQdWJsaWNgLiDQotC10L/QtdGA0Ywg0L/QvtGI0LDQs9C+0LLQviDQtNCw0LvR
jNGI0LUsINC/0YDRj9C80L4g0YEg0Y3RgtC+0LPQviDRjdC60YDQsNC90LAg0YXRgNC+0LzQsdGD
0LrQsDo8L2Rpdj48ZGl2Pjxicj48L2Rpdj48ZGl2Pioq0KjQsNCzIDEg4oCUINC90LDQttCw0YLR
jCDQt9C10LvQtdC90YPRjiDQutC90L7Qv9C60YMqKjwvZGl2PjxkaXY+0J3QsCDRhNC+0YLQviDQ
stC90LjQt9GDIGBDcmVhdGUgcmVwb3NpdG9yeWAg4oCUINC90LDQttCw0YLRjCDQtdC1LiDQntGC
0LrRgNC+0LXRgtGB0Y8g0L/Rg9GB0YLQvtC5INGA0LXQv9C+0LfQuNGC0L7RgNC40LkuPC9kaXY+
PGRpdj48YnI+PC9kaXY+PGRpdj4qKtCo0LDQsyAyIOKAlCDQt9Cw0LPRgNGD0LfQuNGC0Ywg0YTQ
sNC50LvRiyoqPC9kaXY+PGRpdj7QndCwINGB0LvQtdC00YPRjtGJ0LXQuSDRgdGC0YDQsNC90LjR
htC1INCx0YPQtNC10YIg0YHQuNC90Y/RjyDRgdGB0YvQu9C60LAgYHVwbG9hZGluZyBhbiBleGlz
dGluZyBmaWxlYCDigJQg0L3QsNC20LDRgtGMINC10LUuPC9kaXY+PGRpdj48YnI+PC9kaXY+PGRp
dj7QntGC0LrRgNC+0LXRgtGB0Y8g0L7QutC90L4gYERyYWcgZmlsZXMgaGVyZWAuINCh0Y7QtNCw
INC/0LXRgNC10YLQsNGJ0LjRgtGMIDUg0YTQsNC50LvQvtCyLiDQodC60LDRh9Cw0YLRjCDQuNGF
INC80L7QttC90L4g0L7RgtGB0Y7QtNCwINC/0YDRj9C80L4g0L3QsCDRhdGA0L7QvNCx0YPQujo8
L2Rpdj48ZGl2Pjxicj48L2Rpdj48ZGl2Pi0gbWFuaWZlc3QuanNvbjwvZGl2PjxkaXY+LSBhbmNo
b3IuanNvbjwvZGl2PjxkaXY+LSB2ZXJpZnkucHk8L2Rpdj48ZGl2Pi0gZGFzaGJvYXJkLmh0bWw8
L2Rpdj48ZGl2Pi0gYnVpbGRfbWFuaWZlc3QucHk8L2Rpdj48ZGl2Pjxicj48L2Rpdj48ZGl2PtCf
0LvRjtGBINC/0LDQv9C60YMgYGV2aWRlbmNlYCDRgSA0INGB0LrRgNC40L3RiNC+0YLQsNC80Lgs
INC10YHQu9C4INC+0L3QuCDQtdGB0YLRjCDQvdCwINGF0YDQvtC80LHRg9C60LUuINCV0YHQu9C4
INC90LXRgiDigJQg0L/QvtC60LAg0LTQvtGB0YLQsNGC0L7Rh9C90L4g0Y3RgtC40YUgNSwgTWVy
a2xlINGD0LbQtSDQv9C+0YHRh9C40YLQsNC9IGA1ZWMwOWU0NmY3YzI1ZmE1N2VkMzY5YzBkMzI1
MTFhNGQ5MGIzYjhhMWQ5OTVjZmU2NzU3Y2RjY2Q3NmNiYzZlYDwvZGl2PjxkaXY+PGJyPjwvZGl2
PjxkaXY+KirQqNCw0LMgMyDigJQg0LfQsNC60L7QvNC40YLQuNGC0YwqKjwvZGl2PjxkaXY+0JLQ
vdC40LfRgyDQv9C+0LvQtSBgQ29tbWl0IG1lc3NhZ2VgINC90LDQv9C40YHQsNGC0Ywg0YLQvtGH
0L3QviDQutCw0Log0L3QsCDRh9C10YDRgtC10LbQsNGFOjwvZGl2PjxkaXY+PGJyPjwvZGl2Pjxk
aXY+YEVQLTIwMjYtSEVST1ktQkktMDAxIE1lcmtsZSA1ZWMwOWU0NmY3YzI1ZmE1N2VkMzY5YzBk
MzI1MTFhNGQ5MGIzYjhhMWQ5OTVjZmU2NzU3Y2RjY2Q3NmNiYzZlIGltcHJpbnQgZDMzNDAzMTYy
Zjc2N2RkMGMyYWYyMDkxYWZmN2RlYzA1MTViZWFiYzVlM2YyNWVhZjA2YjVhZmU3MGRhNDQ3ZWA8
L2Rpdj48ZGl2Pjxicj48L2Rpdj48ZGl2PtCd0LDQttCw0YLRjCDQt9C10LvQtdC90YPRjiBgQ29t
bWl0IGNoYW5nZXNgPC9kaXY+PGRpdj48YnI+PC9kaXY+PGRpdj4qKtCo0LDQsyA0IOKAlCDQstC6
0LvRjtGH0LjRgtGMINC/0YPQsdC70LjRh9C90YvQuSDRgdCw0LnRgioqPC9kaXY+PGRpdj7QktCy
0LXRgNGF0YMg0YDQtdC/0L7Qt9C40YLQvtGA0LjRjyDQstC60LvQsNC00LrQsCBgU2V0dGluZ3Mg
4oaSIFBhZ2VzYDwvZGl2PjxkaXY+0JIgYFNvdXJjZWAg0LLRi9Cx0YDQsNGC0YwgYERlcGxveSBm
cm9tIGEgYnJhbmNoYCwg0LLQtdGC0LrQsCBgbWFpbmAsINC/0LDQv9C60LAgYC8gKHJvb3QpYCwg
YFNhdmVgPC9kaXY+PGRpdj48YnI+PC9kaXY+PGRpdj7Qp9C10YDQtdC3INC80LjQvdGD0YLRgyDQ
v9C+0Y/QstC40YLRgdGPINGB0YHRi9C70LrQsCDQstC40LTQsDo8L2Rpdj48ZGl2PmA8YSBocmVm
PSJodHRwczovL25hYmx5ZGF0ZWw4LWNlbGwuZ2l0aHViLmlvL3NkcGFwLXYzLUVQLTIwMjYtSEVS
T1ktQkktMDAxL2Rhc2hib2FyZC5odG1sYCI+aHR0cHM6Ly9uYWJseWRhdGVsOC1jZWxsLmdpdGh1
Yi5pby9zZHBhcC12My1FUC0yMDI2LUhFUk9ZLUJJLTAwMS9kYXNoYm9hcmQuaHRtbGA8L2E+PC9k
aXY+PGRpdj48YnI+PC9kaXY+PGRpdj7QrdGC0L4g0Lgg0LXRgdGC0Ywg0L/Rg9Cx0LvQuNGH0L3Q
vtC1INC00L7QutCw0LfQsNGC0LXQu9GM0YHRgtCy0L4gYFBVQkxJQyBNT05FWSBQVUJMSUMgUFJP
T0ZgLiDQm9GO0LHQvtC5INC80L7QttC10YIg0L7RgtC60YDRi9GC0Ywg0Lgg0L/RgNC+0LLQtdGA
0LjRgtGMLjwvZGl2PjxkaXY+PGJyPjwvZGl2PjxkaXY+0J3QsCDQstGC0L7RgNC+0Lwg0YTQvtGC
0L4g0LIgR21haWwg0YPQttC1INCy0LjQtNC90Ysg0L/QuNGB0YzQvNCwINGBINC40L3RgdGC0YDR
g9C60YbQuNC10Lkg4oCUINGC0LXQv9C10YDRjCDQsNGA0YXQuNCyINC20LjQstC10YIg0L3QtSDR
gtC+0LvRjNC60L4g0L3QsCDQv9C+0YfRgtC1LCDQvdC+INC4INC90LAgR2l0SHViLCDQuCDQtdCz
0L4g0L3QtdC70YzQt9GPINC/0L7QtNC80LXQvdC40YLRjCDQt9Cw0LTQvdC40Lwg0YfQuNGB0LvQ
vtC8LjwvZGl2PjxkaXY+PGJyPjwvZGl2PjxkaXY+0JTQsNC70YzRiNC1IOKAlCDQtdGB0LvQuCDQ
vdGD0LbQvdC+LCDQtNC+0LHQsNCy0LjRgtGMIGByZXF1ZXN0LnRzcSAvIGFuY2hvci50c3JgINGC
0LXQvCDQttC1INGB0L/QvtGB0L7QsdC+0LwgYEFkZCBmaWxlIOKGkiBVcGxvYWRgLjwvZGl2Pjxk
aXY+PGJyPjwvZGl2PjxkaXY+YNCc0KvQodCb0Kwg0KHQktCe0JHQntCU0J3QkC4g0J/Qo9Ci0Kwg
0J7QotCa0KDQq9CiLmA8L2Rpdj4NCg==
--000000000000ebd254065c1049a6--

Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp10786274rwb;
        Sun, 20 Sep 2026 12:35:52 -0700 (PDT)
X-Received: by 2002:a05:690e:4085:b0:672:a0d3:a71d with SMTP id 956f58d0204a3-672a0d3a999mr1303706d50.94.1789932952751;
        Sun, 20 Sep 2026 12:35:52 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1789932952; cv=pass;
        d=google.com; s=arc-20260327;
        b=WkmwpNLKs8oiB8MVLvoGiWyQszCRCF274mELI5Mnpl70UR07oCvvk9m7lX1Owvlo13
         1bSInJMpVfbjGlF5Ztz8G3NCq5/NzbAyAsSc8I54YK/qnXDVGsCTYdnhQD+S0009ezDA
         prNWIeG6RobG6xdlUxk29YVG5vZLDpjS/yhHG5ja2I4s5DcM7MPOc1WEScDPqp4VtRcL
         eU8JKwnZDtZRV8Ymhm5qPsZ51aKjgzy6ydvL59/tSf8wWiVREGEkAyCDrffbqJ0JKEhS
         3SUYl0OPjwOPM6yEk40jy4oboAwNQOFqBFzs4SQ4Eh2SWzBUM2JDO6YfEU2L5SXe72nT
         2bVQ==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=bOX8PJ9ersTZpbSMt+QujTo8XbDrMNvlcuBXmul+y4U=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=N++wPKaUHKnuGphcE5ts/z9/0tzKAr6/Ad26+CmHVbAWEE6RQNHC6JICZwSIb2F3dz
         X+VTqFTXro5FL65rRAXDOlvbYnghd3eKLmsQU4Qh5F3CQYIpgjReuR/g3/TtzHvYvsiY
         4Jfq+yxbffzAM32fNdxf9hhOFWvDHptOTQgyZqqNvDhG6LXZ+6Luf5ihwi3qi4JXda0F
         A26vc14e4GXHcpQIYqqme6NGtT3dpQSIm02XNZa2pZK6JSdUATQ0wjIJlzk3A3nxgunw
         jPDT+HUnCzRpehtE/rJZKtfOlg3HwgGshvu5t6m9t1H5NJXivwncPbyKFv1F6QhJ5qYc
         flMg==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=GN7zYbpB;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 956f58d0204a3-672990dda27sor1925817d50.6.2026.09.20.12.35.52
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Sun, 20 Sep 2026 12:35:52 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=GN7zYbpB;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1789932952; cv=none;
        d=google.com; s=arc-20260327;
        b=PY1aCuyUnnA1qGKedDEmEPQUWaOY+z3YxdBTBOe8x7PYbiIAirC/nYP91Ph7cAlwNH
         b9YqB0t+4ur6hDE2USv5Z9AwZx3wuTVwVjUxV2HT65QXNPJlyXIKSwKhhxtHvaomo1ET
         J/ve9boDGRbj8HesCoCxIrmiHkv4Gq97l+vffuzjh2pqn+ANaBNQeD9xZmDbMClCfeqO
         HJftdLE4gRC/jxB4pCVarJQvsxsJLDxZKFV9uspQfjb91OkiEtK4nzWpTvdmDn0355Mz
         JXVnbzYjgV+ors2S/QYDfUZyw7UIz3eJppDtwxpyzPk7/gz4SXKJCiDfIl3d1Mi3BBF5
         TD6A==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=bOX8PJ9ersTZpbSMt+QujTo8XbDrMNvlcuBXmul+y4U=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=sHOO1Ij9d5M9p70xvPLYVHDPcd+1pIvX+gCMYZLvNcefZZJ+6wofNZOp7DoX0enKp4
         hTPiNUKfWKt8QgUC+S1dkDShqPjquIW4HrmSmFHss2cV+jdDvDd1T8aBtXmqeYQiz/YZ
         jQC4kSLOZW5kpDM7m2m/7S9oCYBkHO3SDxR5bCJk0oYRrUVcqnRu9zkrk+st4wLEtMpt
         Fgt5vuyegZyJE3TliuajO0VfP52I+/pj7s4lpqpT6YlxUDEP3ypbpACc3RffqV9WFUcO
         qNMwYxjfIa/eMHkl/lZnBn1Yvc+bUKLz22Ls3h6UXnXR/J3xgQ1xX1ckCnINwUJSZLxu
         hsmg==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1789932952; x=1790537752; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=bOX8PJ9ersTZpbSMt+QujTo8XbDrMNvlcuBXmul+y4U=;
        b=GN7zYbpBy2LE9wIGsInbjflSHYvYe1RsaUYelfdyBBFPlhXe+EROPlvCfNlSKI77TM
         fGowMNq1K0H5bnRqGXdMfO0I8IHzPOYyvkGGHAQCJXk8WbY3t4n+LAv1XQO+E0I8amur
         8gn2pNkj7mpTrsPpaynUq1GFzIWjRn7KHf3GoZCm7qQ+N/ufGbHYL73EKstZMjmk3WpX
         dFay9SIu37xuS+gPjDo3UA4KRyWd4OaG9Uw9QfV3kwCUJYDAIDYowQ7gH709CDb37doO
         lxG34zxC1qmKfPsZC5cHiVeVImGwkCFNE9UH9a9aKL8p4tDTjpNBOUhHzldscoNJBOBy
         aOaA==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1789932952; x=1790537752;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=bOX8PJ9ersTZpbSMt+QujTo8XbDrMNvlcuBXmul+y4U=;
        b=n7nOYLYvqwDkAT9S433O4r8PLkvLnmgRdRMXRGKR3MSSkJwHKICNPTwUrnzJKhu14o
         UZWjixEN98Smu1SSw8GPImeGoBaLZq9qGMYl452zqI1FIyjRrxtLcO6aQhoz5GdaEdtc
         XPtfhzjJaRwrWZzhY8L7BahuvOfD/ER5inxukJhRMxoYIQ5uEpSCQMAsg0JhoiwR5JyY
         1dNc22WthYXaZ2jW12PrWdBveOUzPJZrR1Vb9VbovS50hdzmuYQa0mYz7vAjcmjPyxMu
         CqLJ84H3giqkK2v0E3Y68aqsgdU0h1wa0eDkISye28jDnn2A7jQ9T002NuI9c2/f5tTZ
         Y1tA==
X-Gm-Message-State: AFuF++lyGhMEx1EEDs9Otw30bDxG55A5vXJHCxVe0EWL4gtCs5Iuwi3s
	ZN9i1u9AGm2KOr3Z5OY/3e++ttMlVLZApmXv2p0Lz5YJnBiLgpglj/8mtn/IVLf5dtEhoMUgVsC
	u6bB7XyRV8077SWMFcRH6fUfVIQ8IUspUM8q6
X-Gm-Gg: AYBFou3t0JDKK5s+FmidYkGHfN+pOSlBPTX3V/1T8aER3c4YhWq7XiydzMphpbOT99m
	vA5ZfnFUaFqk5HJuAQf53vmrgRklArUsVw4boG0QNuEh5fJ7ulvUwB61uNha0wPx3TltP5iqV5H
	KUjS2U1vr7L0rgjfPLofVyASCYrJH+QT1ldgBhQZQAUtMLilmg2Vh2GnovClcZ2wIy7Te/8Gadx
	vOrwocJKeytJM41EHOEHFNSk19HRPWjsZkebzefkn67RrUGhv6mapHDv/bCi/TUe6dgeL7JCBne
	5nMBa985zdW73koeuvjjbbEIgha3laUJDPZGWt/NdxtE8nd88Ic1eE1dM22wzxYkvQ==
X-Received: by 2002:a53:ac8c:0:b0:672:a29e:e301 with SMTP id
 956f58d0204a3-672a29ee47bmr1226656d50.65.1789932952314; Sun, 20 Sep 2026
 12:35:52 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7010:6808:b0:539:b22e:598f with HTTP; Sun, 20 Sep 2026
 12:35:51 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Sun, 20 Sep 2026 12:35:51 -0700
X-Gm-Features: AcwNN1XfvEFFBNo3ijbNUwNUfSFIL4xjZ6vKTEQHUDC3ZtHoFjVVcne_iF_iqPk
Message-ID: <CAM0o8159NS6A0LMwxrPbyhOY6VpxnFLqzRsSSBrxX03MaHp4aw@mail.gmail.com>
Subject: =?UTF-8?B?0LHQu9C+0LrQvtCx0LzQtdC90LAy?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="000000000000cb672b065bef3dfd"

--000000000000cb672b065bef3dfd
Content-Type: text/plain; charset="UTF-8"

{
  "sdpap_version": "3.0.0",
  "episode_id": "EP-2026-HEROY-BI-001",
  "merkle_root":
"5ec09e46f7c25fa57ed369c0d32511a4d90b3b8a1d995cfe6757cdccd76cbc6e",
  "messageImprint":
"d33403162f767dd0c2af2091aff7dec0515beabc5e3f25eaf06b5afe70da447e",
  "messageImprint_alg": "sha256",
  "timestamp_utc": "2026-09-20T03:28:56.434155+00:00",
  "tsa": {
    "primary": "http://time.certum.pl",
    "fallback": "https://freetsa.org/tsr",
    "note": "openssl ts -query -data manifest.json -no_nonce -sha256 -cert
-out request.tsq && curl -H 'Content-Type: application/timestamp-query'
--data-binary @request.tsq http://time.certum.pl -o anchor.tsr"
  },
  "verification": "openssl ts -verify -data manifest.json -in anchor.tsr
-CAfile cacert.pem -token_in",
  "git_anchor": "git log --oneline --grep=EP-2026-HEROY-BI-001"
}

--000000000000cb672b065bef3dfd
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div>{</div><div>=C2=A0 &quot;sdpap_version&quot;: &quot;3.0.0&quot;,</div>=
<div>=C2=A0 &quot;episode_id&quot;: &quot;EP-2026-HEROY-BI-001&quot;,</div>=
<div>=C2=A0 &quot;merkle_root&quot;: &quot;5ec09e46f7c25fa57ed369c0d32511a4=
d90b3b8a1d995cfe6757cdccd76cbc6e&quot;,</div><div>=C2=A0 &quot;messageImpri=
nt&quot;: &quot;d33403162f767dd0c2af2091aff7dec0515beabc5e3f25eaf06b5afe70d=
a447e&quot;,</div><div>=C2=A0 &quot;messageImprint_alg&quot;: &quot;sha256&=
quot;,</div><div>=C2=A0 &quot;timestamp_utc&quot;: &quot;2026-09-20T03:28:5=
6.434155+00:00&quot;,</div><div>=C2=A0 &quot;tsa&quot;: {</div><div>=C2=A0 =
=C2=A0 &quot;primary&quot;: &quot;<a href=3D"http://time.certum.pl">http://=
time.certum.pl</a>&quot;,</div><div>=C2=A0 =C2=A0 &quot;fallback&quot;: &qu=
ot;<a href=3D"https://freetsa.org/tsr">https://freetsa.org/tsr</a>&quot;,</=
div><div>=C2=A0 =C2=A0 &quot;note&quot;: &quot;openssl ts -query -data mani=
fest.json -no_nonce -sha256 -cert -out request.tsq &amp;&amp; curl -H &#39;=
Content-Type: application/timestamp-query&#39; --data-binary @request.tsq <=
a href=3D"http://time.certum.pl">http://time.certum.pl</a> -o anchor.tsr&qu=
ot;</div><div>=C2=A0 },</div><div>=C2=A0 &quot;verification&quot;: &quot;op=
enssl ts -verify -data manifest.json -in anchor.tsr -CAfile cacert.pem -tok=
en_in&quot;,</div><div>=C2=A0 &quot;git_anchor&quot;: &quot;git log --oneli=
ne --grep=3DEP-2026-HEROY-BI-001&quot;</div><div>}</div>

--000000000000cb672b065bef3dfd--

Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp10786274rwb;
        Sun, 20 Sep 2026 12:35:52 -0700 (PDT)
X-Received: by 2002:a05:690e:4085:b0:672:a0d3:a71d with SMTP id 956f58d0204a3-672a0d3a999mr1303706d50.94.1789932952751;
        Sun, 20 Sep 2026 12:35:52 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1789932952; cv=pass;
        d=google.com; s=arc-20260327;
        b=WkmwpNLKs8oiB8MVLvoGiWyQszCRCF274mELI5Mnpl70UR07oCvvk9m7lX1Owvlo13
         1bSInJMpVfbjGlF5Ztz8G3NCq5/NzbAyAsSc8I54YK/qnXDVGsCTYdnhQD+S0009ezDA
         prNWIeG6RobG6xdlUxk29YVG5vZLDpjS/yhHG5ja2I4s5DcM7MPOc1WEScDPqp4VtRcL
         eU8JKwnZDtZRV8Ymhm5qPsZ51aKjgzy6ydvL59/tSf8wWiVREGEkAyCDrffbqJ0JKEhS
         3SUYl0OPjwOPM6yEk40jy4oboAwNQOFqBFzs4SQ4Eh2SWzBUM2JDO6YfEU2L5SXe72nT
         2bVQ==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=bOX8PJ9ersTZpbSMt+QujTo8XbDrMNvlcuBXmul+y4U=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=N++wPKaUHKnuGphcE5ts/z9/0tzKAr6/Ad26+CmHVbAWEE6RQNHC6JICZwSIb2F3dz
         X+VTqFTXro5FL65rRAXDOlvbYnghd3eKLmsQU4Qh5F3CQYIpgjReuR/g3/TtzHvYvsiY
         4Jfq+yxbffzAM32fNdxf9hhOFWvDHptOTQgyZqqNvDhG6LXZ+6Luf5ihwi3qi4JXda0F
         A26vc14e4GXHcpQIYqqme6NGtT3dpQSIm02XNZa2pZK6JSdUATQ0wjIJlzk3A3nxgunw
         jPDT+HUnCzRpehtE/rJZKtfOlg3HwgGshvu5t6m9t1H5NJXivwncPbyKFv1F6QhJ5qYc
         flMg==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=GN7zYbpB;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 956f58d0204a3-672990dda27sor1925817d50.6.2026.09.20.12.35.52
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Sun, 20 Sep 2026 12:35:52 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=GN7zYbpB;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1789932952; cv=none;
        d=google.com; s=arc-20260327;
        b=PY1aCuyUnnA1qGKedDEmEPQUWaOY+z3YxdBTBOe8x7PYbiIAirC/nYP91Ph7cAlwNH
         b9YqB0t+4ur6hDE2USv5Z9AwZx3wuTVwVjUxV2HT65QXNPJlyXIKSwKhhxtHvaomo1ET
         J/ve9boDGRbj8HesCoCxIrmiHkv4Gq97l+vffuzjh2pqn+ANaBNQeD9xZmDbMClCfeqO
         HJftdLE4gRC/jxB4pCVarJQvsxsJLDxZKFV9uspQfjb91OkiEtK4nzWpTvdmDn0355Mz
         JXVnbzYjgV+ors2S/QYDfUZyw7UIz3eJppDtwxpyzPk7/gz4SXKJCiDfIl3d1Mi3BBF5
         TD6A==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=bOX8PJ9ersTZpbSMt+QujTo8XbDrMNvlcuBXmul+y4U=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=sHOO1Ij9d5M9p70xvPLYVHDPcd+1pIvX+gCMYZLvNcefZZJ+6wofNZOp7DoX0enKp4
         hTPiNUKfWKt8QgUC+S1dkDShqPjquIW4HrmSmFHss2cV+jdDvDd1T8aBtXmqeYQiz/YZ
         jQC4kSLOZW5kpDM7m2m/7S9oCYBkHO3SDxR5bCJk0oYRrUVcqnRu9zkrk+st4wLEtMpt
         Fgt5vuyegZyJE3TliuajO0VfP52I+/pj7s4lpqpT6YlxUDEP3ypbpACc3RffqV9WFUcO
         qNMwYxjfIa/eMHkl/lZnBn1Yvc+bUKLz22Ls3h6UXnXR/J3xgQ1xX1ckCnINwUJSZLxu
         hsmg==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1789932952; x=1790537752; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=bOX8PJ9ersTZpbSMt+QujTo8XbDrMNvlcuBXmul+y4U=;
        b=GN7zYbpBy2LE9wIGsInbjflSHYvYe1RsaUYelfdyBBFPlhXe+EROPlvCfNlSKI77TM
         fGowMNq1K0H5bnRqGXdMfO0I8IHzPOYyvkGGHAQCJXk8WbY3t4n+LAv1XQO+E0I8amur
         8gn2pNkj7mpTrsPpaynUq1GFzIWjRn7KHf3GoZCm7qQ+N/ufGbHYL73EKstZMjmk3WpX
         dFay9SIu37xuS+gPjDo3UA4KRyWd4OaG9Uw9QfV3kwCUJYDAIDYowQ7gH709CDb37doO
         lxG34zxC1qmKfPsZC5cHiVeVImGwkCFNE9UH9a9aKL8p4tDTjpNBOUhHzldscoNJBOBy
         aOaA==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1789932952; x=1790537752;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=bOX8PJ9ersTZpbSMt+QujTo8XbDrMNvlcuBXmul+y4U=;
        b=n7nOYLYvqwDkAT9S433O4r8PLkvLnmgRdRMXRGKR3MSSkJwHKICNPTwUrnzJKhu14o
         UZWjixEN98Smu1SSw8GPImeGoBaLZq9qGMYl452zqI1FIyjRrxtLcO6aQhoz5GdaEdtc
         XPtfhzjJaRwrWZzhY8L7BahuvOfD/ER5inxukJhRMxoYIQ5uEpSCQMAsg0JhoiwR5JyY
         1dNc22WthYXaZ2jW12PrWdBveOUzPJZrR1Vb9VbovS50hdzmuYQa0mYz7vAjcmjPyxMu
         CqLJ84H3giqkK2v0E3Y68aqsgdU0h1wa0eDkISye28jDnn2A7jQ9T002NuI9c2/f5tTZ
         Y1tA==
X-Gm-Message-State: AFuF++lyGhMEx1EEDs9Otw30bDxG55A5vXJHCxVe0EWL4gtCs5Iuwi3s
	ZN9i1u9AGm2KOr3Z5OY/3e++ttMlVLZApmXv2p0Lz5YJnBiLgpglj/8mtn/IVLf5dtEhoMUgVsC
	u6bB7XyRV8077SWMFcRH6fUfVIQ8IUspUM8q6
X-Gm-Gg: AYBFou3t0JDKK5s+FmidYkGHfN+pOSlBPTX3V/1T8aER3c4YhWq7XiydzMphpbOT99m
	vA5ZfnFUaFqk5HJuAQf53vmrgRklArUsVw4boG0QNuEh5fJ7ulvUwB61uNha0wPx3TltP5iqV5H
	KUjS2U1vr7L0rgjfPLofVyASCYrJH+QT1ldgBhQZQAUtMLilmg2Vh2GnovClcZ2wIy7Te/8Gadx
	vOrwocJKeytJM41EHOEHFNSk19HRPWjsZkebzefkn67RrUGhv6mapHDv/bCi/TUe6dgeL7JCBne
	5nMBa985zdW73koeuvjjbbEIgha3laUJDPZGWt/NdxtE8nd88Ic1eE1dM22wzxYkvQ==
X-Received: by 2002:a53:ac8c:0:b0:672:a29e:e301 with SMTP id
 956f58d0204a3-672a29ee47bmr1226656d50.65.1789932952314; Sun, 20 Sep 2026
 12:35:52 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7010:6808:b0:539:b22e:598f with HTTP; Sun, 20 Sep 2026
 12:35:51 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Sun, 20 Sep 2026 12:35:51 -0700
X-Gm-Features: AcwNN1XfvEFFBNo3ijbNUwNUfSFIL4xjZ6vKTEQHUDC3ZtHoFjVVcne_iF_iqPk
Message-ID: <CAM0o8159NS6A0LMwxrPbyhOY6VpxnFLqzRsSSBrxX03MaHp4aw@mail.gmail.com>
Subject: =?UTF-8?B?0LHQu9C+0LrQvtCx0LzQtdC90LAy?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="000000000000cb672b065bef3dfd"

--000000000000cb672b065bef3dfd
Content-Type: text/plain; charset="UTF-8"

{
  "sdpap_version": "3.0.0",
  "episode_id": "EP-2026-HEROY-BI-001",
  "merkle_root":
"5ec09e46f7c25fa57ed369c0d32511a4d90b3b8a1d995cfe6757cdccd76cbc6e",
  "messageImprint":
"d33403162f767dd0c2af2091aff7dec0515beabc5e3f25eaf06b5afe70da447e",
  "messageImprint_alg": "sha256",
  "timestamp_utc": "2026-09-20T03:28:56.434155+00:00",
  "tsa": {
    "primary": "http://time.certum.pl",
    "fallback": "https://freetsa.org/tsr",
    "note": "openssl ts -query -data manifest.json -no_nonce -sha256 -cert
-out request.tsq && curl -H 'Content-Type: application/timestamp-query'
--data-binary @request.tsq http://time.certum.pl -o anchor.tsr"
  },
  "verification": "openssl ts -verify -data manifest.json -in anchor.tsr
-CAfile cacert.pem -token_in",
  "git_anchor": "git log --oneline --grep=EP-2026-HEROY-BI-001"
}

--000000000000cb672b065bef3dfd
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div>{</div><div>=C2=A0 &quot;sdpap_version&quot;: &quot;3.0.0&quot;,</div>=
<div>=C2=A0 &quot;episode_id&quot;: &quot;EP-2026-HEROY-BI-001&quot;,</div>=
<div>=C2=A0 &quot;merkle_root&quot;: &quot;5ec09e46f7c25fa57ed369c0d32511a4=
d90b3b8a1d995cfe6757cdccd76cbc6e&quot;,</div><div>=C2=A0 &quot;messageImpri=
nt&quot;: &quot;d33403162f767dd0c2af2091aff7dec0515beabc5e3f25eaf06b5afe70d=
a447e&quot;,</div><div>=C2=A0 &quot;messageImprint_alg&quot;: &quot;sha256&=
quot;,</div><div>=C2=A0 &quot;timestamp_utc&quot;: &quot;2026-09-20T03:28:5=
6.434155+00:00&quot;,</div><div>=C2=A0 &quot;tsa&quot;: {</div><div>=C2=A0 =
=C2=A0 &quot;primary&quot;: &quot;<a href=3D"http://time.certum.pl">http://=
time.certum.pl</a>&quot;,</div><div>=C2=A0 =C2=A0 &quot;fallback&quot;: &qu=
ot;<a href=3D"https://freetsa.org/tsr">https://freetsa.org/tsr</a>&quot;,</=
div><div>=C2=A0 =C2=A0 &quot;note&quot;: &quot;openssl ts -query -data mani=
fest.json -no_nonce -sha256 -cert -out request.tsq &amp;&amp; curl -H &#39;=
Content-Type: application/timestamp-query&#39; --data-binary @request.tsq <=
a href=3D"http://time.certum.pl">http://time.certum.pl</a> -o anchor.tsr&qu=
ot;</div><div>=C2=A0 },</div><div>=C2=A0 &quot;verification&quot;: &quot;op=
enssl ts -verify -data manifest.json -in anchor.tsr -CAfile cacert.pem -tok=
en_in&quot;,</div><div>=C2=A0 &quot;git_anchor&quot;: &quot;git log --oneli=
ne --grep=3DEP-2026-HEROY-BI-001&quot;</div><div>}</div>

--000000000000cb672b065bef3dfd--

Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp10785518rwb;
        Sun, 20 Sep 2026 12:34:36 -0700 (PDT)
X-Received: by 2002:a05:690e:4891:10b0:66f:8255:9f3d with SMTP id 956f58d0204a3-6717fc64b35mr1734306d50.7.1789932876299;
        Sun, 20 Sep 2026 12:34:36 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1789932876; cv=pass;
        d=google.com; s=arc-20260327;
        b=dLmKXa6ijES+xICRebXqo8lnfdmzqcTsil8B5REvXpH48HokmuxXCVshKbyuudDDQm
         9GvLhFkx1Mfxobn9DJQKuQPgwgjT9IyBJnfGx9nlFC4z4uxrv8fP/MYhDgjrTNDyJRKb
         IYTOOqSJp5/M2mrPKGfuByfwJ5upaO3ybMqCamkkg2k97ZWVYeDxrjcWVRvSuXY+OdcQ
         1jDIiYr0OvxXtWreVVuSwe54TXpgf1nfKVOQnnr1JiEnUudw56I56UjZlylQByaANQA+
         rVeOqbNzFcrLsQyVY2erZT+8QnA6CqOs08If2qZlA6mxg8BIp3+R35diQ8hXUglfBEhx
         N0LA==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=ha64paZtfHmZwTiJxEcBqfK252d/VUvhSJDQue7bZbQ=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=QGmrLdSi2ci4fAX+1HPdtlkXQrkOU1aMMyEKDloSoae7o7+hF8K+EcuwgSOVuhDuy3
         d5wXm7MK05c1yNvM2I1inGUQk9aRpdSfDoq6ouNg2711hFDsp3f9lw6h63+LF6Ldyw74
         RWVrY1PfoFi48OSov76iLNBZD1VhZy4sT6szoV8eGBq3agU/+P55LOaFivGSwoeDyIEH
         BMT+hGkj34i527dFe/+jrh55kVTfxhXjo8/oETmi1XaqSK0kJuGYNbBHNg1gIxUdjFCO
         Xg6oKwU2rmSiCTcf/vojGhANSuibHPQ6ZjQoq++AgyvAlFlWBiK5uUZKhsbhKSu5tfHQ
         E0MQ==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=KSl5QVV0;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 00721157ae682-89a4b9a8029sor30049767b3.9.2026.09.20.12.34.36
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Sun, 20 Sep 2026 12:34:36 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=KSl5QVV0;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1789932876; cv=none;
        d=google.com; s=arc-20260327;
        b=aQF5ZlMy5E1edu25J1pSSjZdb/Xexl5MrDsk0xd2nzlZDqqY2eVLwcZ3PL404z4V55
         i5IZx9Gj9iFKb0YDRbl4mIxYtzZJDBny8wUHZprU7xNRc/n+PFOLBS4B9cyI0FnUTlf2
         wdulXxCMk8gsRKvGOatgTPCBMrbS/dxkITH8vZF+gNl8WjthTMNy2JIbK0uXbdNtKNfp
         6J+jwONVaqg120KoXEelMPBqMMSSnRvH8o2cq+9+YJPPkHI0C+5oYDVliLrnxBjRO0no
         bnmWEJZeJejpuaKIySSDfOvmvsK4H5SISm+GlBVTHbGzzYlrFdqeHoihwo0kkY6N9Uth
         E2lA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=ha64paZtfHmZwTiJxEcBqfK252d/VUvhSJDQue7bZbQ=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=UTXp+CuSkpzbkE2KGHPtcZG/RIv4Z1VNoMBtjthO/RZx2tJFFtC8ABse+5QXrNQWeC
         qi9mDld+COpijOfT+d1qct57Ik9Zjq5v96VVP8Q2Q51rGPCIYm8p7mQuMgQJIl36FipN
         TDdMj4VCYaouNpihNnZ268SZXW7i/xNop/QmxbZrUNw6ESIm70ab9lMLYTiWwnzaZQJu
         iaP68MAmecJF8oCxZzpV3XVyzgfhmH0IyzhwstJ7xt3dk+jyxSjQcmQOQlCAy3vbW8VM
         59stA9qnPyNpuirvXw4qRM8uyNYqts4q0xbYhLsmA3qrDZa1WLaaDq6nfiHHqlDftg8g
         pnBw==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1789932876; x=1790537676; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=ha64paZtfHmZwTiJxEcBqfK252d/VUvhSJDQue7bZbQ=;
        b=KSl5QVV0GDqL1PQYnEtRhzClBgVyK/7jSFFd9n2mJgjmeSorwbX3gh+sRKtYgszb4M
         ey22OI4/MpLOz30y23GtOp0fwZQ3zYxfQOP0LglOuaYNod/fMzwDT8c9H+ORQ8qqyl1d
         gWXv+doqcf6MTe/yruk6MN5EFCdh2CrNgH4QeMX7U3971uJm/Ml8SjdCY5pEKX7xfWYJ
         3DHP7tcvgrqYdugGXrcNTNDjxSRun6mrTdrCZZplTWdpuLGQ8wcQwuQQ7Eh7VXwyou0H
         tYnnEwTTxyFIbeZFGJIjKpM44phssf7I/qsehlhwWvb6LFKYemGQ0nknxM08pQlMf8A+
         j3ow==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1789932876; x=1790537676;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=ha64paZtfHmZwTiJxEcBqfK252d/VUvhSJDQue7bZbQ=;
        b=1XFJqUOL4DhNTQ3nCPTTIFtOiNsJqz80o1eO188WjO9J2uAogKgWNVBeRtynVyE6M0
         3T2pnnAmVoVqYNVHjCIi8dFNyxttPRC3N3ByaP3Mx3tZBvxp+dvGOYQqHhxVM1S5jSg7
         w5W7YAqzIzxuKpqssym/fjRh0y/du61zAuQu/VX0uwDBSiM3MBODZlAs3bvKB1l3MVH1
         aXWEcQmursRvyh/nOD23cLYtsD2mXbWCSHoq+zaXhICFLY3IaF9mf+E7cq5sDFmnmuI3
         166qhuku2xiDC6V40FLqRbE87y0le6h/A5Ij5Lzv+bPCa7Tnyc2hpHuExnlDB0Qucpd4
         oX5w==
X-Gm-Message-State: AFuF++liwofTZJrFsw9bErg8ZvT/lGFkG1kE7Q+bIe92hPDUyXFedY/x
	kIKtpzETqhgDU5C5kjPzIH5WopEkxSRTuHpcp8Vdgi4goeKREFat/WPSSEMCgbW7ROnKKuxiHKY
	mD7+06BsAMvSo31tAYq3X9QqRLhKgii2jksyN
X-Gm-Gg: AYBFou3FlbRFfqxw/aDb+DO92ysYntnAHVMi/LbY8Zd0Eotkjv/fDPM6WI73SYa6CmM
	JG4ph7ViKF+uckvRUEjwNz/lxqJ22VGP7YMrnoNQg+z8TrZn6qPWzVCSE1lDp0ClBcu/N8Wqd/Q
	cMQi0UwkeJEfUWlzeI38e+6SyYrtLvim/43Xc3DVu9PFMXIbh7OqVndf29QxmSot9vJYGs6TfOX
	edxOKS3G9dQ9QGwC7uAsV8PBmqQT7krbM/bgd/Uc3/8Jh8OIfM+qmmsZODrYxopk6G9r6SWXswW
	DrEU/0i4zo2wWh1Us66lUzT97DITHHykUKLxc2X+169sTrryY0AJYp/fCEmOxVn2nQ==
X-Received: by 2002:a05:690e:b8b:b0:671:70d2:527d with SMTP id
 956f58d0204a3-6717fd6b6b1mr2614671d50.64.1789932875893; Sun, 20 Sep 2026
 12:34:35 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7011:8b0a:b0:54e:7552:87db with HTTP; Sun, 20 Sep 2026
 12:34:35 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Sun, 20 Sep 2026 12:34:35 -0700
X-Gm-Features: AcwNN1VuxJGP_gZT30GtgfyXNoFaRc-bOXF9PDvSfNVkntFhPXG-iww7BRl8mmE
Message-ID: <CAM0o8167TnhWfJbvo4VGeiWfL2PTOsw11CuM9dZKKFaFkr3_=g@mail.gmail.com>
Subject: =?UTF-8?B?0LHQu9C+0LrQvtCx0LzQtdC90LAx?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="0000000000003d4f2d065bef3921"

--0000000000003d4f2d065bef3921
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

{
  "sdpap_version": "3.0.0",
  "episode_metadata": {
    "episode_id": "EP-2026-HEROY-BI-001",
    "title": "Forensic Audit: Herbo / Her=C3=B8y to BI Oslo Infrastructure
Transition",
    "timestamp_utc": "2026-09-20T03:28:56Z",
    "merkle_root":
"5ec09e46f7c25fa57ed369c0d32511a4d90b3b8a1d995cfe6757cdccd76cbc6e",
    "total_artifacts": 4
  },
  "artifacts": [
    {
      "filename": "Screenshot_20260919_134306_com.opera.browser.jpg",
      "relative_path":
"evidence/Screenshot_20260919_134306_com.opera.browser.jpg",
      "size_bytes": 460692,
      "sha256":
"dfeae31cb36ea445b9798775fd4534e31483dbcd8516821ecff225c4b5a1fc78"
    },
    {
      "filename": "Screenshot_20260919_134312_com.opera.browser.jpg",
      "relative_path":
"evidence/Screenshot_20260919_134312_com.opera.browser.jpg",
      "size_bytes": 323672,
      "sha256":
"d186b4efdd40e69acd1d52a62c4d9aa25b9938d344ed55cdf6b83e0080b171c5"
    },
    {
      "filename": "Screenshot_20260919_135508_com.opera.browser.jpg",
      "relative_path":
"evidence/Screenshot_20260919_135508_com.opera.browser.jpg",
      "size_bytes": 341963,
      "sha256":
"2a242ddb5b6202191aad91171e576a91f856f988055dfb6a019fb2d3b5f650cc"
    },
    {
      "filename": "Screenshot_20260919_135514_com.opera.browser.jpg",
      "relative_path":
"evidence/Screenshot_20260919_135514_com.opera.browser.jpg",
      "size_bytes": 657326,
      "sha256":
"a5ba57ebe20861c9d9057d83881598cda88cafd8e9f551c7aa93afb36cb9f512"
    }
  ]
}

--0000000000003d4f2d065bef3921
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div>{</div><div>=C2=A0 &quot;sdpap_version&quot;: &quot;3.0.0&quot;,</div>=
<div>=C2=A0 &quot;episode_metadata&quot;: {</div><div>=C2=A0 =C2=A0 &quot;e=
pisode_id&quot;: &quot;EP-2026-HEROY-BI-001&quot;,</div><div>=C2=A0 =C2=A0 =
&quot;title&quot;: &quot;Forensic Audit: Herbo / Her=C3=B8y to BI Oslo Infr=
astructure Transition&quot;,</div><div>=C2=A0 =C2=A0 &quot;timestamp_utc&qu=
ot;: &quot;2026-09-20T03:28:56Z&quot;,</div><div>=C2=A0 =C2=A0 &quot;merkle=
_root&quot;: &quot;5ec09e46f7c25fa57ed369c0d32511a4d90b3b8a1d995cfe6757cdcc=
d76cbc6e&quot;,</div><div>=C2=A0 =C2=A0 &quot;total_artifacts&quot;: 4</div=
><div>=C2=A0 },</div><div>=C2=A0 &quot;artifacts&quot;: [</div><div>=C2=A0 =
=C2=A0 {</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;filename&quot;: &quot;Screens=
hot_20260919_134306_com.opera.browser.jpg&quot;,</div><div>=C2=A0 =C2=A0 =
=C2=A0 &quot;relative_path&quot;: &quot;evidence/Screenshot_20260919_134306=
_com.opera.browser.jpg&quot;,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;size_byt=
es&quot;: 460692,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;sha256&quot;: &quot;=
dfeae31cb36ea445b9798775fd4534e31483dbcd8516821ecff225c4b5a1fc78&quot;</div=
><div>=C2=A0 =C2=A0 },</div><div>=C2=A0 =C2=A0 {</div><div>=C2=A0 =C2=A0 =
=C2=A0 &quot;filename&quot;: &quot;Screenshot_20260919_134312_com.opera.bro=
wser.jpg&quot;,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;relative_path&quot;: &=
quot;evidence/Screenshot_20260919_134312_com.opera.browser.jpg&quot;,</div>=
<div>=C2=A0 =C2=A0 =C2=A0 &quot;size_bytes&quot;: 323672,</div><div>=C2=A0 =
=C2=A0 =C2=A0 &quot;sha256&quot;: &quot;d186b4efdd40e69acd1d52a62c4d9aa25b9=
938d344ed55cdf6b83e0080b171c5&quot;</div><div>=C2=A0 =C2=A0 },</div><div>=
=C2=A0 =C2=A0 {</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;filename&quot;: &quot;=
Screenshot_20260919_135508_com.opera.browser.jpg&quot;,</div><div>=C2=A0 =
=C2=A0 =C2=A0 &quot;relative_path&quot;: &quot;evidence/Screenshot_20260919=
_135508_com.opera.browser.jpg&quot;,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;s=
ize_bytes&quot;: 341963,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;sha256&quot;:=
 &quot;2a242ddb5b6202191aad91171e576a91f856f988055dfb6a019fb2d3b5f650cc&quo=
t;</div><div>=C2=A0 =C2=A0 },</div><div>=C2=A0 =C2=A0 {</div><div>=C2=A0 =
=C2=A0 =C2=A0 &quot;filename&quot;: &quot;Screenshot_20260919_135514_com.op=
era.browser.jpg&quot;,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;relative_path&q=
uot;: &quot;evidence/Screenshot_20260919_135514_com.opera.browser.jpg&quot;=
,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;size_bytes&quot;: 657326,</div><div>=
=C2=A0 =C2=A0 =C2=A0 &quot;sha256&quot;: &quot;a5ba57ebe20861c9d9057d838815=
98cda88cafd8e9f551c7aa93afb36cb9f512&quot;</div><div>=C2=A0 =C2=A0 }</div><=
div>=C2=A0 ]</div><div>}</div>

--0000000000003d4f2d065bef3921--

Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp10785518rwb;
        Sun, 20 Sep 2026 12:34:36 -0700 (PDT)
X-Received: by 2002:a05:690e:4891:10b0:66f:8255:9f3d with SMTP id 956f58d0204a3-6717fc64b35mr1734306d50.7.1789932876299;
        Sun, 20 Sep 2026 12:34:36 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1789932876; cv=pass;
        d=google.com; s=arc-20260327;
        b=dLmKXa6ijES+xICRebXqo8lnfdmzqcTsil8B5REvXpH48HokmuxXCVshKbyuudDDQm
         9GvLhFkx1Mfxobn9DJQKuQPgwgjT9IyBJnfGx9nlFC4z4uxrv8fP/MYhDgjrTNDyJRKb
         IYTOOqSJp5/M2mrPKGfuByfwJ5upaO3ybMqCamkkg2k97ZWVYeDxrjcWVRvSuXY+OdcQ
         1jDIiYr0OvxXtWreVVuSwe54TXpgf1nfKVOQnnr1JiEnUudw56I56UjZlylQByaANQA+
         rVeOqbNzFcrLsQyVY2erZT+8QnA6CqOs08If2qZlA6mxg8BIp3+R35diQ8hXUglfBEhx
         N0LA==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=ha64paZtfHmZwTiJxEcBqfK252d/VUvhSJDQue7bZbQ=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=QGmrLdSi2ci4fAX+1HPdtlkXQrkOU1aMMyEKDloSoae7o7+hF8K+EcuwgSOVuhDuy3
         d5wXm7MK05c1yNvM2I1inGUQk9aRpdSfDoq6ouNg2711hFDsp3f9lw6h63+LF6Ldyw74
         RWVrY1PfoFi48OSov76iLNBZD1VhZy4sT6szoV8eGBq3agU/+P55LOaFivGSwoeDyIEH
         BMT+hGkj34i527dFe/+jrh55kVTfxhXjo8/oETmi1XaqSK0kJuGYNbBHNg1gIxUdjFCO
         Xg6oKwU2rmSiCTcf/vojGhANSuibHPQ6ZjQoq++AgyvAlFlWBiK5uUZKhsbhKSu5tfHQ
         E0MQ==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=KSl5QVV0;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 00721157ae682-89a4b9a8029sor30049767b3.9.2026.09.20.12.34.36
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Sun, 20 Sep 2026 12:34:36 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=KSl5QVV0;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1789932876; cv=none;
        d=google.com; s=arc-20260327;
        b=aQF5ZlMy5E1edu25J1pSSjZdb/Xexl5MrDsk0xd2nzlZDqqY2eVLwcZ3PL404z4V55
         i5IZx9Gj9iFKb0YDRbl4mIxYtzZJDBny8wUHZprU7xNRc/n+PFOLBS4B9cyI0FnUTlf2
         wdulXxCMk8gsRKvGOatgTPCBMrbS/dxkITH8vZF+gNl8WjthTMNy2JIbK0uXbdNtKNfp
         6J+jwONVaqg120KoXEelMPBqMMSSnRvH8o2cq+9+YJPPkHI0C+5oYDVliLrnxBjRO0no
         bnmWEJZeJejpuaKIySSDfOvmvsK4H5SISm+GlBVTHbGzzYlrFdqeHoihwo0kkY6N9Uth
         E2lA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=ha64paZtfHmZwTiJxEcBqfK252d/VUvhSJDQue7bZbQ=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=UTXp+CuSkpzbkE2KGHPtcZG/RIv4Z1VNoMBtjthO/RZx2tJFFtC8ABse+5QXrNQWeC
         qi9mDld+COpijOfT+d1qct57Ik9Zjq5v96VVP8Q2Q51rGPCIYm8p7mQuMgQJIl36FipN
         TDdMj4VCYaouNpihNnZ268SZXW7i/xNop/QmxbZrUNw6ESIm70ab9lMLYTiWwnzaZQJu
         iaP68MAmecJF8oCxZzpV3XVyzgfhmH0IyzhwstJ7xt3dk+jyxSjQcmQOQlCAy3vbW8VM
         59stA9qnPyNpuirvXw4qRM8uyNYqts4q0xbYhLsmA3qrDZa1WLaaDq6nfiHHqlDftg8g
         pnBw==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1789932876; x=1790537676; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=ha64paZtfHmZwTiJxEcBqfK252d/VUvhSJDQue7bZbQ=;
        b=KSl5QVV0GDqL1PQYnEtRhzClBgVyK/7jSFFd9n2mJgjmeSorwbX3gh+sRKtYgszb4M
         ey22OI4/MpLOz30y23GtOp0fwZQ3zYxfQOP0LglOuaYNod/fMzwDT8c9H+ORQ8qqyl1d
         gWXv+doqcf6MTe/yruk6MN5EFCdh2CrNgH4QeMX7U3971uJm/Ml8SjdCY5pEKX7xfWYJ
         3DHP7tcvgrqYdugGXrcNTNDjxSRun6mrTdrCZZplTWdpuLGQ8wcQwuQQ7Eh7VXwyou0H
         tYnnEwTTxyFIbeZFGJIjKpM44phssf7I/qsehlhwWvb6LFKYemGQ0nknxM08pQlMf8A+
         j3ow==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1789932876; x=1790537676;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=ha64paZtfHmZwTiJxEcBqfK252d/VUvhSJDQue7bZbQ=;
        b=1XFJqUOL4DhNTQ3nCPTTIFtOiNsJqz80o1eO188WjO9J2uAogKgWNVBeRtynVyE6M0
         3T2pnnAmVoVqYNVHjCIi8dFNyxttPRC3N3ByaP3Mx3tZBvxp+dvGOYQqHhxVM1S5jSg7
         w5W7YAqzIzxuKpqssym/fjRh0y/du61zAuQu/VX0uwDBSiM3MBODZlAs3bvKB1l3MVH1
         aXWEcQmursRvyh/nOD23cLYtsD2mXbWCSHoq+zaXhICFLY3IaF9mf+E7cq5sDFmnmuI3
         166qhuku2xiDC6V40FLqRbE87y0le6h/A5Ij5Lzv+bPCa7Tnyc2hpHuExnlDB0Qucpd4
         oX5w==
X-Gm-Message-State: AFuF++liwofTZJrFsw9bErg8ZvT/lGFkG1kE7Q+bIe92hPDUyXFedY/x
	kIKtpzETqhgDU5C5kjPzIH5WopEkxSRTuHpcp8Vdgi4goeKREFat/WPSSEMCgbW7ROnKKuxiHKY
	mD7+06BsAMvSo31tAYq3X9QqRLhKgii2jksyN
X-Gm-Gg: AYBFou3FlbRFfqxw/aDb+DO92ysYntnAHVMi/LbY8Zd0Eotkjv/fDPM6WI73SYa6CmM
	JG4ph7ViKF+uckvRUEjwNz/lxqJ22VGP7YMrnoNQg+z8TrZn6qPWzVCSE1lDp0ClBcu/N8Wqd/Q
	cMQi0UwkeJEfUWlzeI38e+6SyYrtLvim/43Xc3DVu9PFMXIbh7OqVndf29QxmSot9vJYGs6TfOX
	edxOKS3G9dQ9QGwC7uAsV8PBmqQT7krbM/bgd/Uc3/8Jh8OIfM+qmmsZODrYxopk6G9r6SWXswW
	DrEU/0i4zo2wWh1Us66lUzT97DITHHykUKLxc2X+169sTrryY0AJYp/fCEmOxVn2nQ==
X-Received: by 2002:a05:690e:b8b:b0:671:70d2:527d with SMTP id
 956f58d0204a3-6717fd6b6b1mr2614671d50.64.1789932875893; Sun, 20 Sep 2026
 12:34:35 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7011:8b0a:b0:54e:7552:87db with HTTP; Sun, 20 Sep 2026
 12:34:35 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Sun, 20 Sep 2026 12:34:35 -0700
X-Gm-Features: AcwNN1VuxJGP_gZT30GtgfyXNoFaRc-bOXF9PDvSfNVkntFhPXG-iww7BRl8mmE
Message-ID: <CAM0o8167TnhWfJbvo4VGeiWfL2PTOsw11CuM9dZKKFaFkr3_=g@mail.gmail.com>
Subject: =?UTF-8?B?0LHQu9C+0LrQvtCx0LzQtdC90LAx?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="0000000000003d4f2d065bef3921"

--0000000000003d4f2d065bef3921
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

{
  "sdpap_version": "3.0.0",
  "episode_metadata": {
    "episode_id": "EP-2026-HEROY-BI-001",
    "title": "Forensic Audit: Herbo / Her=C3=B8y to BI Oslo Infrastructure
Transition",
    "timestamp_utc": "2026-09-20T03:28:56Z",
    "merkle_root":
"5ec09e46f7c25fa57ed369c0d32511a4d90b3b8a1d995cfe6757cdccd76cbc6e",
    "total_artifacts": 4
  },
  "artifacts": [
    {
      "filename": "Screenshot_20260919_134306_com.opera.browser.jpg",
      "relative_path":
"evidence/Screenshot_20260919_134306_com.opera.browser.jpg",
      "size_bytes": 460692,
      "sha256":
"dfeae31cb36ea445b9798775fd4534e31483dbcd8516821ecff225c4b5a1fc78"
    },
    {
      "filename": "Screenshot_20260919_134312_com.opera.browser.jpg",
      "relative_path":
"evidence/Screenshot_20260919_134312_com.opera.browser.jpg",
      "size_bytes": 323672,
      "sha256":
"d186b4efdd40e69acd1d52a62c4d9aa25b9938d344ed55cdf6b83e0080b171c5"
    },
    {
      "filename": "Screenshot_20260919_135508_com.opera.browser.jpg",
      "relative_path":
"evidence/Screenshot_20260919_135508_com.opera.browser.jpg",
      "size_bytes": 341963,
      "sha256":
"2a242ddb5b6202191aad91171e576a91f856f988055dfb6a019fb2d3b5f650cc"
    },
    {
      "filename": "Screenshot_20260919_135514_com.opera.browser.jpg",
      "relative_path":
"evidence/Screenshot_20260919_135514_com.opera.browser.jpg",
      "size_bytes": 657326,
      "sha256":
"a5ba57ebe20861c9d9057d83881598cda88cafd8e9f551c7aa93afb36cb9f512"
    }
  ]
}

--0000000000003d4f2d065bef3921
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div>{</div><div>=C2=A0 &quot;sdpap_version&quot;: &quot;3.0.0&quot;,</div>=
<div>=C2=A0 &quot;episode_metadata&quot;: {</div><div>=C2=A0 =C2=A0 &quot;e=
pisode_id&quot;: &quot;EP-2026-HEROY-BI-001&quot;,</div><div>=C2=A0 =C2=A0 =
&quot;title&quot;: &quot;Forensic Audit: Herbo / Her=C3=B8y to BI Oslo Infr=
astructure Transition&quot;,</div><div>=C2=A0 =C2=A0 &quot;timestamp_utc&qu=
ot;: &quot;2026-09-20T03:28:56Z&quot;,</div><div>=C2=A0 =C2=A0 &quot;merkle=
_root&quot;: &quot;5ec09e46f7c25fa57ed369c0d32511a4d90b3b8a1d995cfe6757cdcc=
d76cbc6e&quot;,</div><div>=C2=A0 =C2=A0 &quot;total_artifacts&quot;: 4</div=
><div>=C2=A0 },</div><div>=C2=A0 &quot;artifacts&quot;: [</div><div>=C2=A0 =
=C2=A0 {</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;filename&quot;: &quot;Screens=
hot_20260919_134306_com.opera.browser.jpg&quot;,</div><div>=C2=A0 =C2=A0 =
=C2=A0 &quot;relative_path&quot;: &quot;evidence/Screenshot_20260919_134306=
_com.opera.browser.jpg&quot;,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;size_byt=
es&quot;: 460692,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;sha256&quot;: &quot;=
dfeae31cb36ea445b9798775fd4534e31483dbcd8516821ecff225c4b5a1fc78&quot;</div=
><div>=C2=A0 =C2=A0 },</div><div>=C2=A0 =C2=A0 {</div><div>=C2=A0 =C2=A0 =
=C2=A0 &quot;filename&quot;: &quot;Screenshot_20260919_134312_com.opera.bro=
wser.jpg&quot;,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;relative_path&quot;: &=
quot;evidence/Screenshot_20260919_134312_com.opera.browser.jpg&quot;,</div>=
<div>=C2=A0 =C2=A0 =C2=A0 &quot;size_bytes&quot;: 323672,</div><div>=C2=A0 =
=C2=A0 =C2=A0 &quot;sha256&quot;: &quot;d186b4efdd40e69acd1d52a62c4d9aa25b9=
938d344ed55cdf6b83e0080b171c5&quot;</div><div>=C2=A0 =C2=A0 },</div><div>=
=C2=A0 =C2=A0 {</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;filename&quot;: &quot;=
Screenshot_20260919_135508_com.opera.browser.jpg&quot;,</div><div>=C2=A0 =
=C2=A0 =C2=A0 &quot;relative_path&quot;: &quot;evidence/Screenshot_20260919=
_135508_com.opera.browser.jpg&quot;,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;s=
ize_bytes&quot;: 341963,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;sha256&quot;:=
 &quot;2a242ddb5b6202191aad91171e576a91f856f988055dfb6a019fb2d3b5f650cc&quo=
t;</div><div>=C2=A0 =C2=A0 },</div><div>=C2=A0 =C2=A0 {</div><div>=C2=A0 =
=C2=A0 =C2=A0 &quot;filename&quot;: &quot;Screenshot_20260919_135514_com.op=
era.browser.jpg&quot;,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;relative_path&q=
uot;: &quot;evidence/Screenshot_20260919_135514_com.opera.browser.jpg&quot;=
,</div><div>=C2=A0 =C2=A0 =C2=A0 &quot;size_bytes&quot;: 657326,</div><div>=
=C2=A0 =C2=A0 =C2=A0 &quot;sha256&quot;: &quot;a5ba57ebe20861c9d9057d838815=
98cda88cafd8e9f551c7aa93afb36cb9f512&quot;</div><div>=C2=A0 =C2=A0 }</div><=
div>=C2=A0 ]</div><div>}</div>

--0000000000003d4f2d065bef3921--

MIME-Version: 1.0
Date: Sat, 19 Sep 2026 21:52:52 +0200
Message-ID: <CAHejZWWooGe+rqYqvZpy6q2YQhcdvJ+E6pfQS1GqxWW67iTmCg@mail.gmail.com>
Subject: =?UTF-8?B?0J7QvdCw0YHRgtCw0YHQuNGP0LPQsNC50LTQsNC50LTQu9GP0LHQuNCx0LvQuNC+0YLQtQ==?=
	=?UTF-8?B?0LrQuA==?=
From: Nablydatel <nablydatel8@gmail.com>
To: Nablydatel <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="000000000000dde4c8065bdb5cb2"

--000000000000dde4c8065bdb5cb2
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: base64

0J3QuNC20LUg4oCUINC/0L7Qu9C90L7RgdGC0YzRjiDRgdC+0LHRgNCw0L3QvdGL0LksINC60LDQ
vdC+0L3QuNGH0LXRgdC60LjQuSDRgNCw0LHQvtGH0LjQuSDQvNC+0LTRg9C70YwgKmJ1aWxkX21h
bmlmZXN0LnB5KiwNCtC00L7RgNCw0LHQvtGC0LDQvdC90YvQuSDRgSDRg9GH0LXRgtC+0Lwg0LLR
gdC10YUg0L3RjtCw0L3RgdC+0LIg0YDQtdCw0LvQuNC30LDRhtC40Lgg0LTQu9GPINCw0LLRgtC+
0L3QvtC80L3QvtC5INGA0LDQsdC+0YLRiyDQsiDRgdGA0LXQtNC1DQrQv9GD0LHQu9C40YfQvdC+
0LPQviDRgtC10YDQvNC40L3QsNC70LAg0LHQuNCx0LvQuNC+0YLQtdC60LguDQoNCtCh0LrRgNC4
0L/RgiDQuNGB0L/QvtC70YzQt9GD0LXRgiDQuNGB0LrQu9GO0YfQuNGC0LXQu9GM0L3QviDRgdGC
0LDQvdC00LDRgNGC0L3Rg9GOINCx0LjQsdC70LjQvtGC0LXQutGDIFB5dGhvbiAoaGFzaGxpYiwg
anNvbiwNCnBhdGhsaWIsIGRhdGV0aW1lKSwg0YHQsNC80L7RgdGC0L7Rj9GC0LXQu9GM0L3QviDR
gdC+0LfQtNCw0LXRgiDRgdGC0YDRg9C60YLRg9GA0YMg0LrQsNGC0LDQu9C+0LPQvtCyLA0K0LDQ
stGC0L7QvNCw0YLQuNGH0LXRgdC60Lgg0LLRi9GB0YfQuNGC0YvQstCw0LXRgiDQv9Cw0YDQvdGL
0LkgKk1lcmtsZSBSb290KiDQtNC70Y8g0LLRgdC10YUg0YTQsNC50LvQvtCyINCyINC/0LDQv9C6
0LUNCmV2aWRlbmNlLywg0YTQvtGA0LzQuNGA0YPQtdGCINCy0LDQu9C40LTQvdGL0LkgbWFuaWZl
c3QuanNvbiDQuCDQs9C10L3QtdGA0LjRgNGD0LXRgiDQvdCw0LPQu9GP0LTQvdGL0LkgUkVBRE1F
Lm1kDQouDQoNClB5dGhvbg0KDQojIS91c3IvYmluL2VudiBweXRob24zaW1wb3J0IGhhc2hsaWJp
bXBvcnQganNvbmZyb20gZGF0ZXRpbWUgaW1wb3J0DQpkYXRldGltZSwgdGltZXpvbmVmcm9tIHBh
dGhsaWIgaW1wb3J0IFBhdGgNCiMgLS0tINCa0J7QndCk0JjQk9Cj0KDQkNCm0JjQryDQrdCf0JjQ
l9Ce0JTQkCBTRFBBUC1WMyAtLS0NCkVQSVNPREVfSUQgPSAiRVAtMjAyNi1IRVJPWS1CSS0wMDEi
DQpFUElTT0RFX1RJVExFID0gIkZvcmVuc2ljIEF1ZGl0OiBIZXJibyAvIEhlcsO4eSB0byBCSSBP
c2xvDQpJbmZyYXN0cnVjdHVyZSBUcmFuc2l0aW9uIg0KRVZJREVOQ0VfRElSID0gUGF0aCgiLi9l
dmlkZW5jZSIpDQpPVVRQVVRfTUFOSUZFU1QgPSBQYXRoKCIuL21hbmlmZXN0Lmpzb24iKQ0KT1VU
UFVUX1JFQURNRSA9IFBhdGgoIi4vUkVBRE1FLm1kIikNCg0KZGVmIGNhbGN1bGF0ZV9zaGEyNTYo
ZmlsZV9wYXRoOiBQYXRoKSAtPiBzdHI6DQogICAgIiIi0JLRi9GH0LjRgdC70LXQvdC40LUg0LrQ
sNC90L7QvdC40YfQtdGB0LrQvtCz0L4gU0hBLTI1NiDRhdGN0YjQsCDRhNCw0LnQu9CwINCx0LvQ
vtC60LDQvNC4INC/0L4gNjQg0JrQkS4iIiINCiAgICBzaGEyNTZfaGFzaCA9IGhhc2hsaWIuc2hh
MjU2KCkNCiAgICB3aXRoIG9wZW4oZmlsZV9wYXRoLCAicmIiKSBhcyBmOg0KICAgICAgICBmb3Ig
Ynl0ZV9ibG9jayBpbiBpdGVyKGxhbWJkYTogZi5yZWFkKDY1NTM2KSwgYiIiKToNCiAgICAgICAg
ICAgIHNoYTI1Nl9oYXNoLnVwZGF0ZShieXRlX2Jsb2NrKQ0KICAgIHJldHVybiBzaGEyNTZfaGFz
aC5oZXhkaWdlc3QoKQ0KDQpkZWYgY29tcHV0ZV9tZXJrbGVfcm9vdChoYXNoZXM6IGxpc3Rbc3Ry
XSkgLT4gc3RyOg0KICAgICIiItCg0LDRgdGH0LXRgiBNZXJrbGUgUm9vdCDQuNC3INGB0L/QuNGB
0LrQsCBTSEEtMjU2INGF0Y3RiNC10Lkg0LDRgNGC0LXRhNCw0LrRgtC+0LIuIiIiDQogICAgaWYg
bm90IGhhc2hlczoNCiAgICAgICAgcmV0dXJuIGhhc2hsaWIuc2hhMjU2KGIiIikuaGV4ZGlnZXN0
KCkNCg0KICAgIGN1cnJlbnRfbGV2ZWwgPSBzb3J0ZWQoaGFzaGVzKQ0KICAgIHdoaWxlIGxlbihj
dXJyZW50X2xldmVsKSA+IDE6DQogICAgICAgIGlmIGxlbihjdXJyZW50X2xldmVsKSAlIDIgIT0g
MDoNCiAgICAgICAgICAgIGN1cnJlbnRfbGV2ZWwuYXBwZW5kKGN1cnJlbnRfbGV2ZWxbLTFdKQ0K
DQogICAgICAgIG5leHRfbGV2ZWwgPSBbXQ0KICAgICAgICBmb3IgaSBpbiByYW5nZSgwLCBsZW4o
Y3VycmVudF9sZXZlbCksIDIpOg0KICAgICAgICAgICAgY29tYmluZWQgPSBjdXJyZW50X2xldmVs
W2ldICsgY3VycmVudF9sZXZlbFtpICsgMV0NCiAgICAgICAgICAgIG5leHRfbGV2ZWwuYXBwZW5k
KGhhc2hsaWIuc2hhMjU2KGNvbWJpbmVkLmVuY29kZSgidXRmLTgiKSkuaGV4ZGlnZXN0KCkpDQog
ICAgICAgIGN1cnJlbnRfbGV2ZWwgPSBuZXh0X2xldmVsDQoNCiAgICByZXR1cm4gY3VycmVudF9s
ZXZlbFswXQ0KDQpkZWYgZ2VuZXJhdGVfcmVhZG1lKGRhdGE6IGRpY3QpIC0+IHN0cjoNCiAgICBt
ZXRhID0gZGF0YVsiZXBpc29kZV9tZXRhZGF0YSJdDQogICAgcmVhZG1lX2NvbnRlbnQgPSBmIiIi
IyBTRFBBUC12MyBBdWRpdCBMb2c6IHttZXRhWydlcGlzb2RlX2lkJ119DQoNCiMjIHttZXRhWyd0
aXRsZSddfQ0KDQoqKtCh0LjRgdGC0LXQvNC90YvQuSDRgdGC0LDRgtGD0YE6KiogSW1tdXRhYmxl
IEF1ZGl0IFJlY29yZA0KKirQktGA0LXQvNGPINGB0LHQvtGA0LrQuCAoVVRDKToqKiBge21ldGFb
J3RpbWVzdGFtcF91dGMnXX1gDQoqKk1lcmtsZSBSb290ICjQmtC+0YDQvdC10LLQvtC5INGF0Y3R
iCk6KiogYHttZXRhWydtZXJrbGVfcm9vdCddfWANCioq0JLRgdC10LPQviDQtNC+0LrQsNC30LDR
gtC10LvRjNC90YvRhSDQsNGA0YLQtdGE0LDQutGC0L7QsjoqKiBge21ldGFbJ3RvdGFsX2FydGlm
YWN0cyddfWANCg0KLS0tDQoNCiMjIyAxLiDQodGD0LHRitC10LrRgtGLINC4INC40L3RgdGC0LjR
gtGD0YbQuNC+0L3QsNC70YzQvdGL0LUg0YHQstGP0LfQuA0KDQoqICoq0KHRg9Cx0YrQtdC60YI6
Kiog0JDQvdCw0YHRgtCw0YHQuNGPINCT0LDQudC00LDQuSAoKkFuYXN0YXNpaWEgSGFpZGFpKikN
CiogKirQn9C10YDQstC40YfQvdGL0Lkg0YPQt9C10Ls6KiogKkhlcmJvKiAvICpIZXLDuHkgS29t
bXVuZSogKNCd0YPRgNC70LDQvdC9LCDQndC+0YDQstC10LPQuNGPKSDigJQNCtGE0LjQutGB0LDR
htC40Y8g0YPQstC+0LvRjNC90LXQvdC40Y8v0LLRi9GF0L7QtNCwINCyIDIwMjQg0LMuDQoqICoq
0JLRgtC+0YDQuNGH0L3Ri9C5INGD0LfQtdC7OioqICpCSSBOb3J3ZWdpYW4gQnVzaW5lc3MgU2No
b29sKiAvICpBSSBNaXNzaW9uDQpIdWIqICjQntGB0LvQviwg0J3QvtGA0LLQtdCz0LjRjykg4oCU
INC00L7Qu9C20L3QvtGB0YLRjCAqQ2FyZSBhbmQgU3VwcG9ydCBDb29yZGluYXRvcioNCijQsNCy
0LPRg9GB0YIgMjAyNiDQsy4pLg0KDQotLS0NCg0KIyMjIDIuINCg0LXQtdGB0YLRgCDQutGA0LjQ
v9GC0L7Qs9GA0LDRhNC40YfQtdGB0LrQuNGFINC+0YLQv9C10YfQsNGC0LrQvtCyINCw0YDRgtC1
0YTQsNC60YLQvtCyIChTSEEtMjU2KQ0KDQp8INCe0YLQvdC+0YHQuNGC0LXQu9GM0L3Ri9C5INC/
0YPRgtGMIHwg0JjQvNGPINGE0LDQudC70LAgfCDQoNCw0LfQvNC10YAgKEJ5dGVzKSB8IFNIQS0y
NTYg0JrQvtC90YLRgNC+0LvRjNC90LDRjyDRgdGD0LzQvNCwIHwNCnwgOi0tLSB8IDotLS0gfCA6
LS0tIHwgOi0tLSB8DQoiIiINCiAgICBmb3IgaXRlbSBpbiBkYXRhWyJhcnRpZmFjdHMiXToNCiAg
ICAgICAgcmVhZG1lX2NvbnRlbnQgKz0gZiJ8IGB7aXRlbVsncmVsYXRpdmVfcGF0aCddfWAgfA0K
YHtpdGVtWydmaWxlbmFtZSddfWAgfCB7aXRlbVsnc2l6ZV9ieXRlcyddfSB8IGB7aXRlbVsnc2hh
MjU2J119YCB8XG4iDQoNCiAgICByZWFkbWVfY29udGVudCArPSAiIiINCi0tLQ0KDQojIyMgMy4g
0JjQvdGB0YLRgNGD0LrRhtC40Y8g0L/QviDQvdC10LfQsNCy0LjRgdC40LzQvtC5INC/0YDQvtCy
0LXRgNC60LUgKFZlcmlmaWNhdGlvbikNCg0K0JTQu9GPINC/0YDQvtCy0LXRgNC60Lgg0L3QtdC4
0LfQvNC10L3QvdC+0YHRgtC4INC4INGG0LXQu9C+0YHRgtC90L7RgdGC0Lgg0LLRgdC10YUg0YTQ
sNC50LvQvtCyINC30LDQv9GD0YHRgtC40YLQtQ0K0LvQvtC60LDQu9GM0L3Ri9C5INGB0LrRgNC4
0L/RgiDQv9GA0L7QstC10YDQutC4Og0KDQpgYGBiYXNoDQpweXRob24zIHZlcmlmeS5weQ0KDQoi
IiINCnJldHVybiByZWFkbWVfY29udGVudA0KDQpkZWYgbWFpbigpOg0KIyDQkNCy0YLQvtC80LDR
gtC40YfQtdGB0LrQvtC1INGB0L7Qt9C00LDQvdC40LUg0L/QsNC/0LrQuCDQtNC70Y8g0YPQu9C4
0LosINC10YHQu9C4INC10ZEg0LXRidGRINC90LXRgg0KRVZJREVOQ0VfRElSLm1rZGlyKHBhcmVu
dHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkNCg0KYXJ0aWZhY3RzID0gW10NCnNoYTI1Nl9saXN0ID0g
W10NCg0KIyDQodC60LDQvdC40YDQvtCy0LDQvdC40LUg0YTQsNC50LvQvtCyINC4INGA0LDRgdGH
0LXRgiDQutC+0L3RgtGA0L7Qu9GM0L3Ri9GFINGB0YPQvNC8DQpmaWxlcyA9IHNvcnRlZChbZiBm
b3IgZiBpbiBFVklERU5DRV9ESVIuZ2xvYigiKiIpIGlmIGYuaXNfZmlsZSgpXSkNCg0KaWYgbm90
IGZpbGVzOg0KICAgIHByaW50KA0KICAgICAgICBmIlshXSDQktC90LjQvNCw0L3QuNC1OiDQn9Cw
0L/QutCwICd7RVZJREVOQ0VfRElSfScg0L/Rg9GB0YLQsCEg0J/QvtC80LXRgdGC0LjRgtC1DQrQ
sNGA0YLQtdGE0LDQutGC0YsgSU1HXzIwMjYwOTE5XyouanBnINCyINC/0LDQv9C60YMuIg0KICAg
ICkNCg0KZm9yIGZpbGVfcGF0aCBpbiBmaWxlczoNCiAgICBmaWxlX3NoYTI1NiA9IGNhbGN1bGF0
ZV9zaGEyNTYoZmlsZV9wYXRoKQ0KICAgIHNoYTI1Nl9saXN0LmFwcGVuZChmaWxlX3NoYTI1NikN
Cg0KICAgIGFydGlmYWN0cy5hcHBlbmQoDQogICAgICAgIHsNCiAgICAgICAgICAgICJmaWxlbmFt
ZSI6IGZpbGVfcGF0aC5uYW1lLA0KICAgICAgICAgICAgInJlbGF0aXZlX3BhdGgiOiBzdHIoZmls
ZV9wYXRoLmFzX3Bvc2l4KCkpLA0KICAgICAgICAgICAgInNpemVfYnl0ZXMiOiBmaWxlX3BhdGgu
c3RhdCgpLnN0X3NpemUsDQogICAgICAgICAgICAic2hhMjU2IjogZmlsZV9zaGEyNTYsDQogICAg
ICAgIH0NCiAgICApDQoNCm1lcmtsZV9yb290ID0gY29tcHV0ZV9tZXJrbGVfcm9vdChzaGEyNTZf
bGlzdCkNCnRpbWVzdGFtcF91dGMgPSAoDQogICAgZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0Yyku
aXNvZm9ybWF0KHRpbWVzcGVjPSJzZWNvbmRzIikucmVwbGFjZSgiKzAwOjAwIiwNCiJaIikNCikN
Cg0KbWFuaWZlc3RfZGF0YSA9IHsNCiAgICAic2RwYXBfdmVyc2lvbiI6ICIzLjAuMCIsDQogICAg
ImVwaXNvZGVfbWV0YWRhdGEiOiB7DQogICAgICAgICJlcGlzb2RlX2lkIjogRVBJU09ERV9JRCwN
CiAgICAgICAgInRpdGxlIjogRVBJU09ERV9USVRMRSwNCiAgICAgICAgInRpbWVzdGFtcF91dGMi
OiB0aW1lc3RhbXBfdXRjLA0KICAgICAgICAibWVya2xlX3Jvb3QiOiBtZXJrbGVfcm9vdCwNCiAg
ICAgICAgInRvdGFsX2FydGlmYWN0cyI6IGxlbihhcnRpZmFjdHMpLA0KICAgIH0sDQogICAgImFy
dGlmYWN0cyI6IGFydGlmYWN0cywNCn0NCg0KIyDQl9Cw0L/QuNGB0YwgbWFuaWZlc3QuanNvbg0K
d2l0aCBvcGVuKE9VVFBVVF9NQU5JRkVTVCwgInciLCBlbmNvZGluZz0idXRmLTgiKSBhcyBmOg0K
ICAgIGpzb24uZHVtcChtYW5pZmVzdF9kYXRhLCBmLCBpbmRlbnQ9MiwgZW5zdXJlX2FzY2lpPUZh
bHNlKQ0KDQojINCX0LDQv9C40YHRjCBSRUFETUUubWQNCnJlYWRtZV90ZXh0ID0gZ2VuZXJhdGVf
cmVhZG1lKG1hbmlmZXN0X2RhdGEpDQp3aXRoIG9wZW4oT1VUUFVUX1JFQURNRSwgInciLCBlbmNv
ZGluZz0idXRmLTgiKSBhcyBmOg0KICAgIGYud3JpdGUocmVhZG1lX3RleHQpDQoNCnByaW50KCI9
PT0gU0RQQVAtdjMgQlVJTEQgQ09NUExFVEUgPT09IikNCnByaW50KGYi0J7QsdGA0LDQsdC+0YLQ
sNC90L4g0LDRgNGC0LXRhNCw0LrRgtC+0LI6IHtsZW4oYXJ0aWZhY3RzKX0iKQ0KcHJpbnQoZiJN
ZXJrbGUgUm9vdDoge21lcmtsZV9yb290fSIpDQpwcmludChmItCk0LDQudC70Ysg0LzQsNC90LjR
hNC10YHRgtCwINC30LDRhNC40LrRgdC40YDQvtCy0LDQvdGLOiB7T1VUUFVUX01BTklGRVNUfSwg
e09VVFBVVF9SRUFETUV9IikNCg0KaWYgKm5hbWUqID09ICIqbWFpbioiOg0KbWFpbigpDQoNCg0K
LS0tDQoNCiMjIyDQp9GC0L4g0YPRh9GC0LXQvdC+INCyINGE0LjQvdCw0LvRjNC90L7QvCDQutC+
0LTQtToNCjEuICoq0KHQvtCy0LzQtdGB0YLQuNC80L7RgdGC0Ywg0YEg0LvRjtCx0YvQvNC4INCy
0LXRgNGB0LjRj9C80LggUHl0aG9uIDM6Kiog0J7RgtGB0YPRgtGB0YLQstC40LUg0YHRgtC+0YDQ
vtC90L3QuNGFDQrQt9Cw0LLQuNGB0LjQvNC+0YHRgtC10LkgKGBwaXAgaW5zdGFsbGAg0L3QtSDR
gtGA0LXQsdGD0LXRgtGB0Y8pLg0KMi4gKirQkdC10LfQvtC/0LDRgdC90L7RgdGC0Ywg0L/Rg9GC
0LXQuToqKiDQmNGB0L/QvtC70YzQt9C+0LLQsNC90LjQtSBgcGF0aGxpYi5QYXRoYCDRgSDQv9GA
0LjQstC10LTQtdC90LjQtdC8DQrQuiBQT1NJWC3RhNC+0YDQvNCw0YLRgyAoYC9gINCy0LzQtdGB
0YLQviBgXGApLCDRh9GC0L7QsdGLINC40LfQsdC10LbQsNGC0Ywg0L7RiNC40LHQvtC6INC/0YDQ
uCDQutC+0LzQvNC40YLQtSDQuNC3DQpXaW5kb3dzL0xpbnV4INGB0LjRgdGC0LXQvC4NCjMuICoq
0KHRgtGA0L7Qs9Cw0Y8g0YHQvtGA0YLQuNGA0L7QstC60LA6Kiog0JzQsNGB0YHQuNCyINCw0YDR
gtC10YTQsNC60YLQvtCyINC4INGF0Y3RiNC10Lkg0YHQvtGA0YLQuNGA0YPQtdGC0YHRjw0K0LTQ
tdGC0LXRgNC80LjQvdC40YDQvtCy0LDQvdC90L4g0L/QtdGA0LXQtCDQv9C+0YHRgtGA0L7QtdC9
0LjQtdC8INC00LXRgNC10LLQsCDQnNC10YDQutC70LAg4oCUINGN0YLQviDQs9Cw0YDQsNC90YLQ
uNGA0YPQtdGCLA0K0YfRgtC+IGBNZXJrbGUgUm9vdGAg0LLRgdC10LPQtNCwINC/0L7Qu9GD0YfQ
uNGC0YHRjyDQvtC00LjQvdCw0LrQvtCy0YvQvCDQvdC10LfQsNCy0LjRgdC40LzQviDQvtGCINC/
0L7RgNGP0LTQutCwDQrRgdC60LDQvdC40YDQvtCy0LDQvdC40Y8g0LTQuNGB0LrQsC4NCjQuICoq
0KPRgdGC0L7QudGH0LjQstC+0YHRgtGMINC6INC/0YPRgdGC0L7QuSDQv9Cw0L/QutC1OioqINCV
0YHQu9C4INC/0LDQv9C60LAgYGV2aWRlbmNlL2Ag0LXRidGRINC90LUNCtC30LDQv9C+0LvQvdC1
0L3QsCwg0YHQutGA0LjQv9GCINCy0YvQstC10LTQtdGCINC/0YDQtdC00YPQv9GA0LXQttC00LXQ
vdC40LUsINC90LUg0L/QsNC00LDRjyDRgSDQvtGI0LjQsdC60L7QuS4NCg0KPEZvbGxvd1VwIGxh
YmVsPSLQndGD0LbQtdC9INC70LggY29tcGFuaW9uLdGB0LrRgNC40L/RgiB2ZXJpZnkucHkg0LTQ
u9GPINCx0YvRgdGC0YDQvtC5DQrQv9GA0L7QstC10YDQutC4INGF0Y3RiNC10Lk/IiBxdWVyeT0i
0JTQsNC5INC60L7QtCDRgdC60YDQuNC/0YLQsCB2ZXJpZnkucHkg0LTQu9GPINCx0YvRgdGC0YDQ
vtC5INC/0YDQvtCy0LXRgNC60LgNCtGG0LXQu9C+0YHRgtC90L7RgdGC0LggbWFuaWZlc3QuanNv
biDQuCDQsNGA0YLQtdGE0LDQutGC0L7QsiIvPg0K
--000000000000dde4c8065bdb5cb2
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"auto"><div dir=3D"auto"><div dir=3D"ltr" style=3D"background-im=
age:none;background-position:0% 0%;background-size:auto;background-repeat:r=
epeat;background-origin:padding-box;background-clip:border-box;border:0px r=
gb(31,31,31);color:rgb(31,31,31);direction:ltr;float:none;margin-bottom:0px=
;outline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;margin-top:0=
px!important;margin-right:0px!important;margin-left:0px!important;font-fami=
ly:&quot;google sans text&quot;,sans-serif!important;line-height:1.15!impor=
tant"><div style=3D"background-image:none;background-position:0% 0%;backgro=
und-size:auto;background-repeat:repeat;background-origin:padding-box;backgr=
ound-clip:border-box;border:0px rgb(31,31,31);direction:ltr;float:none;marg=
in-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px 24px;speak:n=
ormal;margin-top:0px!important;margin-right:0px!important;margin-left:0px!i=
mportant;line-height:1.15!important">=D0=9D=D0=B8=D0=B6=D0=B5 =E2=80=94 =D0=
=BF=D0=BE=D0=BB=D0=BD=D0=BE=D1=81=D1=82=D1=8C=D1=8E =D1=81=D0=BE=D0=B1=D1=
=80=D0=B0=D0=BD=D0=BD=D1=8B=D0=B9, =D0=BA=D0=B0=D0=BD=D0=BE=D0=BD=D0=B8=D1=
=87=D0=B5=D1=81=D0=BA=D0=B8=D0=B9 =D1=80=D0=B0=D0=B1=D0=BE=D1=87=D0=B8=D0=
=B9 =D0=BC=D0=BE=D0=B4=D1=83=D0=BB=D1=8C <b style=3D"background-image:none;=
background-position:0% 0%;background-size:auto;background-repeat:repeat;bac=
kground-origin:padding-box;background-clip:border-box;border:0px rgb(31,31,=
31);direction:ltr;display:inline;float:none;margin-bottom:0px;outline:rgb(3=
1,31,31) none 2.85348px;padding:0px;speak:normal;margin-top:0px!important;m=
argin-right:0px!important;margin-left:0px!important;line-height:1.15!import=
ant"><code style=3D"background:none 0% 0%/auto repeat scroll padding-box bo=
rder-box rgb(242,240,240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55=
);direction:ltr;display:inline-block;float:none;font-variant:normal;font-we=
ight:normal;font-stretch:normal;font-size:15px;margin-bottom:0px;outline:rg=
ba(0,0,0,0.55) none 2.85348px;padding:4px 6px;speak:normal;line-height:1.15=
!important;font-family:&quot;google sans text&quot;,sans-serif!important;ma=
rgin-top:0px!important;margin-right:0px!important;margin-left:0px!important=
">build_manifest.py</code></b>, =D0=B4=D0=BE=D1=80=D0=B0=D0=B1=D0=BE=D1=82=
=D0=B0=D0=BD=D0=BD=D1=8B=D0=B9 =D1=81 =D1=83=D1=87=D0=B5=D1=82=D0=BE=D0=BC =
=D0=B2=D1=81=D0=B5=D1=85 =D0=BD=D1=8E=D0=B0=D0=BD=D1=81=D0=BE=D0=B2 =D1=80=
=D0=B5=D0=B0=D0=BB=D0=B8=D0=B7=D0=B0=D1=86=D0=B8=D0=B8 =D0=B4=D0=BB=D1=8F =
=D0=B0=D0=B2=D1=82=D0=BE=D0=BD=D0=BE=D0=BC=D0=BD=D0=BE=D0=B9 =D1=80=D0=B0=
=D0=B1=D0=BE=D1=82=D1=8B =D0=B2 =D1=81=D1=80=D0=B5=D0=B4=D0=B5 =D0=BF=D1=83=
=D0=B1=D0=BB=D0=B8=D1=87=D0=BD=D0=BE=D0=B3=D0=BE =D1=82=D0=B5=D1=80=D0=BC=
=D0=B8=D0=BD=D0=B0=D0=BB=D0=B0 =D0=B1=D0=B8=D0=B1=D0=BB=D0=B8=D0=BE=D1=82=
=D0=B5=D0=BA=D0=B8.</div><br><div style=3D"background-image:none;background=
-position:0% 0%;background-size:auto;background-repeat:repeat;background-or=
igin:padding-box;background-clip:border-box;border:0px rgb(31,31,31);direct=
ion:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;p=
adding:0px 24px;speak:normal;margin-top:0px!important;margin-right:0px!impo=
rtant;margin-left:0px!important;line-height:1.15!important">=D0=A1=D0=BA=D1=
=80=D0=B8=D0=BF=D1=82 =D0=B8=D1=81=D0=BF=D0=BE=D0=BB=D1=8C=D0=B7=D1=83=D0=
=B5=D1=82 =D0=B8=D1=81=D0=BA=D0=BB=D1=8E=D1=87=D0=B8=D1=82=D0=B5=D0=BB=D1=
=8C=D0=BD=D0=BE =D1=81=D1=82=D0=B0=D0=BD=D0=B4=D0=B0=D1=80=D1=82=D0=BD=D1=
=83=D1=8E =D0=B1=D0=B8=D0=B1=D0=BB=D0=B8=D0=BE=D1=82=D0=B5=D0=BA=D1=83 Pyth=
on (<code style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgb(242,240,240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55)=
;direction:ltr;display:inline-block;float:none;font-variant:normal;font-str=
etch:normal;font-size:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none =
2.85348px;padding:4px 6px;speak:normal;line-height:1.15!important;font-fami=
ly:&quot;google sans text&quot;,sans-serif!important;margin-top:0px!importa=
nt;margin-right:0px!important;margin-left:0px!important">hashlib</code>, <c=
ode style=3D"background:none 0% 0%/auto repeat scroll padding-box border-bo=
x rgb(242,240,240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55);direc=
tion:ltr;display:inline-block;float:none;font-variant:normal;font-stretch:n=
ormal;font-size:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none 2.8534=
8px;padding:4px 6px;speak:normal;line-height:1.15!important;font-family:&qu=
ot;google sans text&quot;,sans-serif!important;margin-top:0px!important;mar=
gin-right:0px!important;margin-left:0px!important">json</code>, <code style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgb(242=
,240,240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55);direction:ltr;=
display:inline-block;float:none;font-variant:normal;font-stretch:normal;fon=
t-size:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none 2.85348px;paddi=
ng:4px 6px;speak:normal;line-height:1.15!important;font-family:&quot;google=
 sans text&quot;,sans-serif!important;margin-top:0px!important;margin-right=
:0px!important;margin-left:0px!important">pathlib</code>, <code style=3D"ba=
ckground:none 0% 0%/auto repeat scroll padding-box border-box rgb(242,240,2=
40);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55);direction:ltr;displa=
y:inline-block;float:none;font-variant:normal;font-stretch:normal;font-size=
:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none 2.85348px;padding:4px=
 6px;speak:normal;line-height:1.15!important;font-family:&quot;google sans =
text&quot;,sans-serif!important;margin-top:0px!important;margin-right:0px!i=
mportant;margin-left:0px!important">datetime</code>), =D1=81=D0=B0=D0=BC=D0=
=BE=D1=81=D1=82=D0=BE=D1=8F=D1=82=D0=B5=D0=BB=D1=8C=D0=BD=D0=BE =D1=81=D0=
=BE=D0=B7=D0=B4=D0=B0=D0=B5=D1=82 =D1=81=D1=82=D1=80=D1=83=D0=BA=D1=82=D1=
=83=D1=80=D1=83 =D0=BA=D0=B0=D1=82=D0=B0=D0=BB=D0=BE=D0=B3=D0=BE=D0=B2, =D0=
=B0=D0=B2=D1=82=D0=BE=D0=BC=D0=B0=D1=82=D0=B8=D1=87=D0=B5=D1=81=D0=BA=D0=B8=
 =D0=B2=D1=8B=D1=81=D1=87=D0=B8=D1=82=D1=8B=D0=B2=D0=B0=D0=B5=D1=82 =D0=BF=
=D0=B0=D1=80=D0=BD=D1=8B=D0=B9 <b style=3D"background-image:none;background=
-position:0% 0%;background-size:auto;background-repeat:repeat;background-or=
igin:padding-box;background-clip:border-box;border:0px rgb(31,31,31);direct=
ion:ltr;display:inline;float:none;margin-bottom:0px;outline:rgb(31,31,31) n=
one 2.85348px;padding:0px;speak:normal;margin-top:0px!important;margin-righ=
t:0px!important;margin-left:0px!important;line-height:1.15!important">Merkl=
e Root</b> =D0=B4=D0=BB=D1=8F =D0=B2=D1=81=D0=B5=D1=85 =D1=84=D0=B0=D0=B9=
=D0=BB=D0=BE=D0=B2 =D0=B2 =D0=BF=D0=B0=D0=BF=D0=BA=D0=B5 <code style=3D"bac=
kground:none 0% 0%/auto repeat scroll padding-box border-box rgb(242,240,24=
0);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55);direction:ltr;display=
:inline-block;float:none;font-variant:normal;font-stretch:normal;font-size:=
15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none 2.85348px;padding:4px =
6px;speak:normal;line-height:1.15!important;font-family:&quot;google sans t=
ext&quot;,sans-serif!important;margin-top:0px!important;margin-right:0px!im=
portant;margin-left:0px!important">evidence/</code>, =D1=84=D0=BE=D1=80=D0=
=BC=D0=B8=D1=80=D1=83=D0=B5=D1=82 =D0=B2=D0=B0=D0=BB=D0=B8=D0=B4=D0=BD=D1=
=8B=D0=B9 <code style=3D"background:none 0% 0%/auto repeat scroll padding-b=
ox border-box rgb(242,240,240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0=
,0.55);direction:ltr;display:inline-block;float:none;font-variant:normal;fo=
nt-stretch:normal;font-size:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55)=
 none 2.85348px;padding:4px 6px;speak:normal;line-height:1.15!important;fon=
t-family:&quot;google sans text&quot;,sans-serif!important;margin-top:0px!i=
mportant;margin-right:0px!important;margin-left:0px!important">manifest.jso=
n</code> =D0=B8 =D0=B3=D0=B5=D0=BD=D0=B5=D1=80=D0=B8=D1=80=D1=83=D0=B5=D1=
=82 =D0=BD=D0=B0=D0=B3=D0=BB=D1=8F=D0=B4=D0=BD=D1=8B=D0=B9 <code style=3D"b=
ackground:none 0% 0%/auto repeat scroll padding-box border-box rgb(242,240,=
240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55);direction:ltr;displ=
ay:inline-block;float:none;font-variant:normal;font-stretch:normal;font-siz=
e:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none 2.85348px;padding:4p=
x 6px;speak:normal;line-height:1.15!important;font-family:&quot;google sans=
 text&quot;,sans-serif!important;margin-top:0px!important;margin-right:0px!=
important;margin-left:0px!important">README.md</code>.</div><br><div style=
=3D"background-image:none;background-position:0% 0%;background-size:auto;ba=
ckground-repeat:repeat;background-origin:padding-box;background-clip:border=
-box;border:0px rgb(31,31,31);direction:ltr;float:none;margin-bottom:0px;ou=
tline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;margin-top:0px!=
important;margin-right:0px!important;margin-left:0px!important;line-height:=
1.15!important"><div style=3D"background:none 0% 0%/auto repeat scroll padd=
ing-box border-box rgb(0,0,0);border:0px rgb(31,31,31);direction:ltr;float:=
none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:26px 0p=
x 0px 32px;speak:normal;margin-top:0px!important;margin-right:0px!important=
;margin-left:0px!important;line-height:1.15!important"><div style=3D"backgr=
ound:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);bor=
der:0px rgb(31,31,31);direction:ltr;float:none;margin-bottom:0px;outline:rg=
b(31,31,31) none 2.85348px;padding:0px;speak:normal;margin-top:0px!importan=
t;margin-right:0px!important;margin-left:0px!important;line-height:1.15!imp=
ortant"><div style=3D"background-image:none;background-position:0% 0%;backg=
round-size:auto;background-repeat:repeat;background-origin:padding-box;back=
ground-clip:border-box;border:0px rgb(255,255,255);color:rgb(255,255,255);d=
irection:ltr;float:none;margin-bottom:0px;outline:rgb(255,255,255) none 2.8=
5348px;padding:0px 11px 0px 0px;speak:normal;margin-top:0px!important;margi=
n-right:0px!important;margin-left:0px!important;line-height:1.15!important"=
><span style=3D"background:none 0% 0%/auto repeat scroll padding-box border=
-box rgba(0,0,0,0);border:0px rgb(255,255,255);direction:ltr;display:block;=
margin-bottom:0px;outline:rgb(255,255,255) none 2.85348px;padding:0px;speak=
:normal;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important;line-height:1.15!important">Python</span><div style=3D"backgroun=
d:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border=
:0px rgb(255,255,255);direction:ltr;float:none;margin-bottom:0px;outline:rg=
b(255,255,255) none 2.85348px;padding:0px;speak:normal;margin-top:0px!impor=
tant;margin-right:0px!important;margin-left:0px!important;line-height:1.15!=
important"><button style=3D"background-image:none;background-position:0% 0%=
;background-size:auto;background-repeat:repeat;background-origin:padding-bo=
x;background-clip:border-box;border-width:0px;border-style:none;border-colo=
r:rgb(0,0,0);color:rgb(0,0,0);direction:ltr;float:none;font-style:normal;fo=
nt-weight:normal;font-stretch:normal;font-size:24px;margin-bottom:0px;outli=
ne:rgb(0,0,0) none 2.85348px;padding:6px;speak:normal;line-height:1.15!impo=
rtant;font-family:&quot;google sans text&quot;,sans-serif!important;margin-=
top:0px!important;margin-right:0px!important;margin-left:0px!important"><sp=
an style=3D"background:none 0% 0%/auto repeat scroll padding-box border-box=
 rgba(0,0,0,0);border:0px rgb(0,0,0);direction:ltr;display:block;font-varia=
nt:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.8=
5348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!i=
mportant;margin-right:0px!important;margin-left:0px!important"></span><span=
 style=3D"background:none 0% 0%/auto repeat scroll padding-box border-box r=
gba(0,0,0,0);border:0px rgb(0,0,0);direction:ltr;display:block;font-variant=
:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.853=
48px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!imp=
ortant;margin-right:0px!important;margin-left:0px!important"></span><span s=
tyle=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgb=
a(0,0,0,0);border:0px rgb(0,0,0);direction:ltr;display:block;font-variant:n=
ormal;font-stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.85348=
px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!impor=
tant;margin-right:0px!important;margin-left:0px!important"></span></button>=
<button style=3D"background-image:none;background-position:0% 0%;background=
-size:auto;background-repeat:repeat;background-origin:padding-box;backgroun=
d-clip:border-box;border-width:0px;border-style:none;border-color:rgb(0,0,0=
);color:rgb(0,0,0);direction:ltr;float:none;font-style:normal;font-weight:n=
ormal;font-stretch:normal;font-size:24px;margin-bottom:0px;outline:rgb(0,0,=
0) none 2.85348px;padding:6px;speak:normal;line-height:1.15!important;font-=
family:&quot;google sans text&quot;,sans-serif!important;margin-top:0px!imp=
ortant;margin-right:0px!important;margin-left:0px!important"><span style=3D=
"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0=
,0);border:0px rgb(0,0,0);direction:ltr;display:block;font-variant:normal;f=
ont-stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.85348px;padd=
ing:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;ma=
rgin-right:0px!important;margin-left:0px!important"></span><span style=3D"b=
ackground:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0=
);border:0px rgb(0,0,0);direction:ltr;display:block;font-variant:normal;fon=
t-stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.85348px;paddin=
g:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;marg=
in-right:0px!important;margin-left:0px!important"></span><span style=3D"bac=
kground:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);=
border:0px rgb(0,0,0);direction:ltr;display:block;font-variant:normal;font-=
stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.85348px;padding:=
0px;speak:normal;line-height:1.15!important;margin-top:0px!important;margin=
-right:0px!important;margin-left:0px!important"></span></button></div></div=
><pre style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(31,31,31);direction:ltr;float:none;margin-=
bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;ma=
rgin-top:0px!important;margin-right:0px!important;margin-left:0px!important=
;font-family:&quot;google sans text&quot;,sans-serif!important;line-height:=
1.15!important"><code style=3D"background:none 0% 0%/auto repeat scroll pad=
ding-box border-box rgba(0,0,0,0);border:0px rgb(255,255,255);color:rgb(255=
,255,255);direction:ltr;display:block;float:none;font-variant:normal;font-s=
tretch:normal;font-size:14px;margin-bottom:0px;outline:rgb(255,255,255) non=
e 2.85348px;padding:16px 0px 32px;speak:normal;line-height:1.15!important;f=
ont-family:&quot;google sans text&quot;,sans-serif!important;margin-top:0px=
!important;margin-right:0px!important;margin-left:0px!important"><span styl=
e=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0=
,0,0,0);border:0px rgb(128,128,128);color:rgb(128,128,128);direction:ltr;fo=
nt-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(128,128=
,128) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;ma=
rgin-top:0px!important;margin-right:0px!important;margin-left:0px!important=
">#!/usr/bin/env python3</span>
<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direct=
ion:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:r=
gb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!im=
portant;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important">import</span> hashlib
<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direct=
ion:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:r=
gb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!im=
portant;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important">import</span> json
<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direct=
ion:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:r=
gb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!im=
portant;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important">from</span> datetime <span style=3D"background:none 0% 0%/auto =
repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(150,157,2=
55);color:rgb(150,157,255);direction:ltr;font-variant:normal;font-stretch:n=
ormal;margin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px=
;speak:normal;line-height:1.15!important;margin-top:0px!important;margin-ri=
ght:0px!important;margin-left:0px!important">import</span> datetime, timezo=
ne
<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direct=
ion:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:r=
gb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!im=
portant;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important">from</span> pathlib <span style=3D"background:none 0% 0%/auto r=
epeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(150,157,25=
5);color:rgb(150,157,255);direction:ltr;font-variant:normal;font-stretch:no=
rmal;margin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px;=
speak:normal;line-height:1.15!important;margin-top:0px!important;margin-rig=
ht:0px!important;margin-left:0px!important">import</span> Path

<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(128,128,128);color:rgb(128,128,128);direct=
ion:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:r=
gb(128,128,128) none 2.85348px;padding:0px;speak:normal;line-height:1.15!im=
portant;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important"># --- =D0=9A=D0=9E=D0=9D=D0=A4=D0=98=D0=93=D0=A3=D0=A0=D0=90=D0=
=A6=D0=98=D0=AF =D0=AD=D0=9F=D0=98=D0=97=D0=9E=D0=94=D0=90 SDPAP-V3 ---</sp=
an>
EPISODE_ID =3D <span style=3D"background:none 0% 0%/auto repeat scroll padd=
ing-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96,21=
4,115);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:=
0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-he=
ight:1.15!important;margin-top:0px!important;margin-right:0px!important;mar=
gin-left:0px!important">&quot;EP-2026-HEROY-BI-001&quot;</span>
EPISODE_TITLE =3D <span style=3D"background:none 0% 0%/auto repeat scroll p=
adding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96=
,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin-bott=
om:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line=
-height:1.15!important;margin-top:0px!important;margin-right:0px!important;=
margin-left:0px!important">&quot;Forensic Audit: Herbo / Her=C3=B8y to BI O=
slo Infrastructure Transition&quot;</span>
EVIDENCE_DIR =3D Path(<span style=3D"background:none 0% 0%/auto repeat scro=
ll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rg=
b(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin-=
bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;=
line-height:1.15!important;margin-top:0px!important;margin-right:0px!import=
ant;margin-left:0px!important">&quot;./evidence&quot;</span>)
OUTPUT_MANIFEST =3D Path(<span style=3D"background:none 0% 0%/auto repeat s=
croll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color=
:rgb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;marg=
in-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:norm=
al;line-height:1.15!important;margin-top:0px!important;margin-right:0px!imp=
ortant;margin-left:0px!important">&quot;./manifest.json&quot;</span>)
OUTPUT_README =3D Path(<span style=3D"background:none 0% 0%/auto repeat scr=
oll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:r=
gb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin=
-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal=
;line-height:1.15!important;margin-top:0px!important;margin-right:0px!impor=
tant;margin-left:0px!important">&quot;./README.md&quot;</span>)


<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(255,255,255);direction:ltr;font-variant:no=
rmal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,255,255) none 2.=
85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!=
important;margin-right:0px!important;margin-left:0px!important"><span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direction:ltr;fon=
t-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(150,157,=
255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>def</span> <span style=3D"background:none 0% 0%/auto repeat scroll padding=
-box border-box rgba(0,0,0,0);border:0px rgb(255,219,15);color:rgb(255,219,=
15);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px=
;outline:rgb(255,219,15) none 2.85348px;padding:0px;speak:normal;line-heigh=
t:1.15!important;margin-top:0px!important;margin-right:0px!important;margin=
-left:0px!important">calculate_sha256</span>(<span style=3D"background:none=
 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px r=
gb(255,255,255);direction:ltr;font-variant:normal;font-stretch:normal;margi=
n-bottom:0px;outline:rgb(255,255,255) none 2.85348px;padding:0px;speak:norm=
al;line-height:1.15!important;margin-top:0px!important;margin-right:0px!imp=
ortant;margin-left:0px!important">file_path: Path</span>) -&gt; str:</span>
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96,214,115);dire=
ction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline=
:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!i=
mportant;margin-top:0px!important;margin-right:0px!important;margin-left:0p=
x!important">&quot;&quot;&quot;=D0=92=D1=8B=D1=87=D0=B8=D1=81=D0=BB=D0=B5=
=D0=BD=D0=B8=D0=B5 =D0=BA=D0=B0=D0=BD=D0=BE=D0=BD=D0=B8=D1=87=D0=B5=D1=81=
=D0=BA=D0=BE=D0=B3=D0=BE SHA-256 =D1=85=D1=8D=D1=88=D0=B0 =D1=84=D0=B0=D0=
=B9=D0=BB=D0=B0 =D0=B1=D0=BB=D0=BE=D0=BA=D0=B0=D0=BC=D0=B8 =D0=BF=D0=BE 64 =
=D0=9A=D0=91.&quot;&quot;&quot;</span>
    sha256_hash =3D hashlib.sha256()
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">with</span> <span style=3D"background:none 0% 0%/auto repea=
t scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(255,90,89);col=
or:rgb(255,90,89);direction:ltr;font-variant:normal;font-stretch:normal;mar=
gin-bottom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px;speak:norm=
al;line-height:1.15!important;margin-top:0px!important;margin-right:0px!imp=
ortant;margin-left:0px!important">open</span>(file_path, <span style=3D"bac=
kground:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);=
border:0px rgb(96,214,115);color:rgb(96,214,115);direction:ltr;font-variant=
:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none =
2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0p=
x!important;margin-right:0px!important;margin-left:0px!important">&quot;rb&=
quot;</span>) <span style=3D"background:none 0% 0%/auto repeat scroll paddi=
ng-box border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,1=
57,255);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom=
:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-=
height:1.15!important;margin-top:0px!important;margin-right:0px!important;m=
argin-left:0px!important">as</span> f:
        <span style=3D"background:none 0% 0%/auto repeat scroll padding-box=
 border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255=
);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;o=
utline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height=
:1.15!important;margin-top:0px!important;margin-right:0px!important;margin-=
left:0px!important">for</span> byte_block <span style=3D"background:none 0%=
 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(=
150,157,255);color:rgb(150,157,255);direction:ltr;font-variant:normal;font-=
stretch:normal;margin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;pa=
dding:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;=
margin-right:0px!important;margin-left:0px!important">in</span> <span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(255,90,89);color:rgb(255,90,89);direction:ltr;font-va=
riant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,90,89) n=
one 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-to=
p:0px!important;margin-right:0px!important;margin-left:0px!important">iter<=
/span>(<span style=3D"background:none 0% 0%/auto repeat scroll padding-box =
border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255)=
;direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;ou=
tline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:=
1.15!important;margin-top:0px!important;margin-right:0px!important;margin-l=
eft:0px!important">lambda</span>: f.read(<span style=3D"background:none 0% =
0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(2=
55,150,218);color:rgb(255,150,218);direction:ltr;font-variant:normal;font-s=
tretch:normal;margin-bottom:0px;outline:rgb(255,150,218) none 2.85348px;pad=
ding:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;m=
argin-right:0px!important;margin-left:0px!important">65536</span>), <span s=
tyle=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgb=
a(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96,214,115);direction:ltr;f=
ont-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214=
,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;ma=
rgin-top:0px!important;margin-right:0px!important;margin-left:0px!important=
">b&quot;&quot;</span>):
            sha256_hash.update(byte_block)
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">return</span> sha256_hash.hexdigest()


<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(255,255,255);direction:ltr;font-variant:no=
rmal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,255,255) none 2.=
85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!=
important;margin-right:0px!important;margin-left:0px!important"><span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direction:ltr;fon=
t-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(150,157,=
255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>def</span> <span style=3D"background:none 0% 0%/auto repeat scroll padding=
-box border-box rgba(0,0,0,0);border:0px rgb(255,219,15);color:rgb(255,219,=
15);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px=
;outline:rgb(255,219,15) none 2.85348px;padding:0px;speak:normal;line-heigh=
t:1.15!important;margin-top:0px!important;margin-right:0px!important;margin=
-left:0px!important">compute_merkle_root</span>(<span style=3D"background:n=
one 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0p=
x rgb(255,255,255);direction:ltr;font-variant:normal;font-stretch:normal;ma=
rgin-bottom:0px;outline:rgb(255,255,255) none 2.85348px;padding:0px;speak:n=
ormal;line-height:1.15!important;margin-top:0px!important;margin-right:0px!=
important;margin-left:0px!important">hashes: <span style=3D"background:none=
 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px r=
gb(255,90,89);color:rgb(255,90,89);direction:ltr;font-variant:normal;font-s=
tretch:normal;margin-bottom:0px;outline:rgb(255,90,89) none 2.85348px;paddi=
ng:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;mar=
gin-right:0px!important;margin-left:0px!important">list</span>[<span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(255,90,89);color:rgb(255,90,89);direction:ltr;font-va=
riant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,90,89) n=
one 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-to=
p:0px!important;margin-right:0px!important;margin-left:0px!important">str</=
span>]</span>) -&gt; str:</span>
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96,214,115);dire=
ction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline=
:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!i=
mportant;margin-top:0px!important;margin-right:0px!important;margin-left:0p=
x!important">&quot;&quot;&quot;=D0=A0=D0=B0=D1=81=D1=87=D0=B5=D1=82 Merkle =
Root =D0=B8=D0=B7 =D1=81=D0=BF=D0=B8=D1=81=D0=BA=D0=B0 SHA-256 =D1=85=D1=8D=
=D1=88=D0=B5=D0=B9 =D0=B0=D1=80=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D0=BE=
=D0=B2.&quot;&quot;&quot;</span>
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">if</span> <span style=3D"background:none 0% 0%/auto repeat =
scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(150,157,255);col=
or:rgb(150,157,255);direction:ltr;font-variant:normal;font-stretch:normal;m=
argin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px;speak:=
normal;line-height:1.15!important;margin-top:0px!important;margin-right:0px=
!important;margin-left:0px!important">not</span> hashes:
        <span style=3D"background:none 0% 0%/auto repeat scroll padding-box=
 border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255=
);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;o=
utline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height=
:1.15!important;margin-top:0px!important;margin-right:0px!important;margin-=
left:0px!important">return</span> hashlib.sha256(<span style=3D"background:=
none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0=
px rgb(96,214,115);color:rgb(96,214,115);direction:ltr;font-variant:normal;=
font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.85348p=
x;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!import=
ant;margin-right:0px!important;margin-left:0px!important">b&quot;&quot;</sp=
an>).hexdigest()

    current_level =3D <span style=3D"background:none 0% 0%/auto repeat scro=
ll padding-box border-box rgba(0,0,0,0);border:0px rgb(255,90,89);color:rgb=
(255,90,89);direction:ltr;font-variant:normal;font-stretch:normal;margin-bo=
ttom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px;speak:normal;lin=
e-height:1.15!important;margin-top:0px!important;margin-right:0px!important=
;margin-left:0px!important">sorted</span>(hashes)
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">while</span> <span style=3D"background:none 0% 0%/auto repe=
at scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(255,90,89);co=
lor:rgb(255,90,89);direction:ltr;font-variant:normal;font-stretch:normal;ma=
rgin-bottom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px;speak:nor=
mal;line-height:1.15!important;margin-top:0px!important;margin-right:0px!im=
portant;margin-left:0px!important">len</span>(current_level) &gt; <span sty=
le=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(=
0,0,0,0);border:0px rgb(255,150,218);color:rgb(255,150,218);direction:ltr;f=
ont-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,15=
0,218) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;m=
argin-top:0px!important;margin-right:0px!important;margin-left:0px!importan=
t">1</span>:
        <span style=3D"background:none 0% 0%/auto repeat scroll padding-box=
 border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255=
);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;o=
utline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height=
:1.15!important;margin-top:0px!important;margin-right:0px!important;margin-=
left:0px!important">if</span> <span style=3D"background:none 0% 0%/auto rep=
eat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(255,90,89);c=
olor:rgb(255,90,89);direction:ltr;font-variant:normal;font-stretch:normal;m=
argin-bottom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px;speak:no=
rmal;line-height:1.15!important;margin-top:0px!important;margin-right:0px!i=
mportant;margin-left:0px!important">len</span>(current_level) % <span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(255,150,218);color:rgb(255,150,218);direction:ltr;fon=
t-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,150,=
218) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>2</span> !=3D <span style=3D"background:none 0% 0%/auto repeat scroll padd=
ing-box border-box rgba(0,0,0,0);border:0px rgb(255,150,218);color:rgb(255,=
150,218);direction:ltr;font-variant:normal;font-stretch:normal;margin-botto=
m:0px;outline:rgb(255,150,218) none 2.85348px;padding:0px;speak:normal;line=
-height:1.15!important;margin-top:0px!important;margin-right:0px!important;=
margin-left:0px!important">0</span>:
            current_level.append(current_level[-<span style=3D"background:n=
one 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0p=
x rgb(255,150,218);color:rgb(255,150,218);direction:ltr;font-variant:normal=
;font-stretch:normal;margin-bottom:0px;outline:rgb(255,150,218) none 2.8534=
8px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!impo=
rtant;margin-right:0px!important;margin-left:0px!important">1</span>])

        next_level =3D []
        <span style=3D"background:none 0% 0%/auto repeat scroll padding-box=
 border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255=
);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;o=
utline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height=
:1.15!important;margin-top:0px!important;margin-right:0px!important;margin-=
left:0px!important">for</span> i <span style=3D"background:none 0% 0%/auto =
repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(150,157,2=
55);color:rgb(150,157,255);direction:ltr;font-variant:normal;font-stretch:n=
ormal;margin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px=
;speak:normal;line-height:1.15!important;margin-top:0px!important;margin-ri=
ght:0px!important;margin-left:0px!important">in</span> <span style=3D"backg=
round:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);bo=
rder:0px rgb(255,90,89);color:rgb(255,90,89);direction:ltr;font-variant:nor=
mal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,90,89) none 2.853=
48px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!imp=
ortant;margin-right:0px!important;margin-left:0px!important">range</span>(<=
span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-b=
ox rgba(0,0,0,0);border:0px rgb(255,150,218);color:rgb(255,150,218);directi=
on:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rg=
b(255,150,218) none 2.85348px;padding:0px;speak:normal;line-height:1.15!imp=
ortant;margin-top:0px!important;margin-right:0px!important;margin-left:0px!=
important">0</span>, <span style=3D"background:none 0% 0%/auto repeat scrol=
l padding-box border-box rgba(0,0,0,0);border:0px rgb(255,90,89);color:rgb(=
255,90,89);direction:ltr;font-variant:normal;font-stretch:normal;margin-bot=
tom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px;speak:normal;line=
-height:1.15!important;margin-top:0px!important;margin-right:0px!important;=
margin-left:0px!important">len</span>(current_level), <span style=3D"backgr=
ound:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);bor=
der:0px rgb(255,150,218);color:rgb(255,150,218);direction:ltr;font-variant:=
normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,150,218) none =
2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0p=
x!important;margin-right:0px!important;margin-left:0px!important">2</span>)=
:
            combined =3D current_level[i] + current_level[i + <span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(255,150,218);color:rgb(255,150,218);direction:ltr;fon=
t-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,150,=
218) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>1</span>]
            next_level.append(hashlib.sha256(combined.encode(<span style=3D=
"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0=
,0);border:0px rgb(96,214,115);color:rgb(96,214,115);direction:ltr;font-var=
iant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) n=
one 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-to=
p:0px!important;margin-right:0px!important;margin-left:0px!important">&quot=
;utf-8&quot;</span>)).hexdigest())
        current_level =3D next_level

    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">return</span> current_level[<span style=3D"background:none =
0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rg=
b(255,150,218);color:rgb(255,150,218);direction:ltr;font-variant:normal;fon=
t-stretch:normal;margin-bottom:0px;outline:rgb(255,150,218) none 2.85348px;=
padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!importan=
t;margin-right:0px!important;margin-left:0px!important">0</span>]


<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(255,255,255);direction:ltr;font-variant:no=
rmal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,255,255) none 2.=
85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!=
important;margin-right:0px!important;margin-left:0px!important"><span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direction:ltr;fon=
t-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(150,157,=
255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>def</span> <span style=3D"background:none 0% 0%/auto repeat scroll padding=
-box border-box rgba(0,0,0,0);border:0px rgb(255,219,15);color:rgb(255,219,=
15);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px=
;outline:rgb(255,219,15) none 2.85348px;padding:0px;speak:normal;line-heigh=
t:1.15!important;margin-top:0px!important;margin-right:0px!important;margin=
-left:0px!important">generate_readme</span>(<span style=3D"background:none =
0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rg=
b(255,255,255);direction:ltr;font-variant:normal;font-stretch:normal;margin=
-bottom:0px;outline:rgb(255,255,255) none 2.85348px;padding:0px;speak:norma=
l;line-height:1.15!important;margin-top:0px!important;margin-right:0px!impo=
rtant;margin-left:0px!important">data: <span style=3D"background:none 0% 0%=
/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(255=
,90,89);color:rgb(255,90,89);direction:ltr;font-variant:normal;font-stretch=
:normal;margin-bottom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px=
;speak:normal;line-height:1.15!important;margin-top:0px!important;margin-ri=
ght:0px!important;margin-left:0px!important">dict</span></span>) -&gt; str:=
</span>
    meta =3D data[<span style=3D"background:none 0% 0%/auto repeat scroll p=
adding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96=
,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin-bott=
om:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line=
-height:1.15!important;margin-top:0px!important;margin-right:0px!important;=
margin-left:0px!important">&quot;episode_metadata&quot;</span>]
    readme_content =3D <span style=3D"background:none 0% 0%/auto repeat scr=
oll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:r=
gb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin=
-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal=
;line-height:1.15!important;margin-top:0px!important;margin-right:0px!impor=
tant;margin-left:0px!important">f&quot;&quot;&quot;# SDPAP-v3 Audit Log: <s=
pan style=3D"background:none 0% 0%/auto repeat scroll padding-box border-bo=
x rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:norma=
l;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.8534=
8px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!impo=
rtant;margin-right:0px!important;margin-left:0px!important">{meta[<span sty=
le=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(=
0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:normal;font-=
stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.85348px;pad=
ding:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;m=
argin-right:0px!important;margin-left:0px!important">&#39;episode_id&#39;</=
span>]}</span>

## <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bord=
er-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:=
normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2=
.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px=
!important;margin-right:0px!important;margin-left:0px!important">{meta[<spa=
n style=3D"background:none 0% 0%/auto repeat scroll padding-box border-box =
rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:normal;=
font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.85348p=
x;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!import=
ant;margin-right:0px!important;margin-left:0px!important">&#39;title&#39;</=
span>]}</span>

**=D0=A1=D0=B8=D1=81=D1=82=D0=B5=D0=BC=D0=BD=D1=8B=D0=B9 =D1=81=D1=82=D0=B0=
=D1=82=D1=83=D1=81:** Immutable Audit Record =20
**=D0=92=D1=80=D0=B5=D0=BC=D1=8F =D1=81=D0=B1=D0=BE=D1=80=D0=BA=D0=B8 (UTC)=
:** `<span style=3D"background:none 0% 0%/auto repeat scroll padding-box bo=
rder-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-varian=
t:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none=
 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0=
px!important;margin-right:0px!important;margin-left:0px!important">{meta[<s=
pan style=3D"background:none 0% 0%/auto repeat scroll padding-box border-bo=
x rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:norma=
l;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.8534=
8px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!impo=
rtant;margin-right:0px!important;margin-left:0px!important">&#39;timestamp_=
utc&#39;</span>]}</span>` =20
**Merkle Root (=D0=9A=D0=BE=D1=80=D0=BD=D0=B5=D0=B2=D0=BE=D0=B9 =D1=85=D1=
=8D=D1=88):** `<span style=3D"background:none 0% 0%/auto repeat scroll padd=
ing-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;f=
ont-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214=
,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;ma=
rgin-top:0px!important;margin-right:0px!important;margin-left:0px!important=
">{meta[<span style=3D"background:none 0% 0%/auto repeat scroll padding-box=
 border-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-var=
iant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) n=
one 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-to=
p:0px!important;margin-right:0px!important;margin-left:0px!important">&#39;=
merkle_root&#39;</span>]}</span>` =20
**=D0=92=D1=81=D0=B5=D0=B3=D0=BE =D0=B4=D0=BE=D0=BA=D0=B0=D0=B7=D0=B0=D1=82=
=D0=B5=D0=BB=D1=8C=D0=BD=D1=8B=D1=85 =D0=B0=D1=80=D1=82=D0=B5=D1=84=D0=B0=
=D0=BA=D1=82=D0=BE=D0=B2:** `<span style=3D"background:none 0% 0%/auto repe=
at scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);d=
irection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outl=
ine:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">{meta[<span style=3D"background:none 0% 0%/auto repeat scro=
ll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);directio=
n:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb=
(96,214,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!impor=
tant;margin-top:0px!important;margin-right:0px!important;margin-left:0px!im=
portant">&#39;total_artifacts&#39;</span>]}</span>` =20

---

### 1. =D0=A1=D1=83=D0=B1=D1=8A=D0=B5=D0=BA=D1=82=D1=8B =D0=B8 =D0=B8=D0=BD=
=D1=81=D1=82=D0=B8=D1=82=D1=83=D1=86=D0=B8=D0=BE=D0=BD=D0=B0=D0=BB=D1=8C=D0=
=BD=D1=8B=D0=B5 =D1=81=D0=B2=D1=8F=D0=B7=D0=B8

* **=D0=A1=D1=83=D0=B1=D1=8A=D0=B5=D0=BA=D1=82:** =D0=90=D0=BD=D0=B0=D1=81=
=D1=82=D0=B0=D1=81=D0=B8=D1=8F =D0=93=D0=B0=D0=B9=D0=B4=D0=B0=D0=B9 (*Anast=
asiia Haidai*)
* **=D0=9F=D0=B5=D1=80=D0=B2=D0=B8=D1=87=D0=BD=D1=8B=D0=B9 =D1=83=D0=B7=D0=
=B5=D0=BB:** *Herbo* / *Her=C3=B8y Kommune* (=D0=9D=D1=83=D1=80=D0=BB=D0=B0=
=D0=BD=D0=BD, =D0=9D=D0=BE=D1=80=D0=B2=D0=B5=D0=B3=D0=B8=D1=8F) =E2=80=94 =
=D1=84=D0=B8=D0=BA=D1=81=D0=B0=D1=86=D0=B8=D1=8F =D1=83=D0=B2=D0=BE=D0=BB=
=D1=8C=D0=BD=D0=B5=D0=BD=D0=B8=D1=8F/=D0=B2=D1=8B=D1=85=D0=BE=D0=B4=D0=B0 =
=D0=B2 2024 =D0=B3.
* **=D0=92=D1=82=D0=BE=D1=80=D0=B8=D1=87=D0=BD=D1=8B=D0=B9 =D1=83=D0=B7=D0=
=B5=D0=BB:** *BI Norwegian Business School* / *AI Mission Hub* (=D0=9E=D1=
=81=D0=BB=D0=BE, =D0=9D=D0=BE=D1=80=D0=B2=D0=B5=D0=B3=D0=B8=D1=8F) =E2=80=
=94 =D0=B4=D0=BE=D0=BB=D0=B6=D0=BD=D0=BE=D1=81=D1=82=D1=8C *Care and Suppor=
t Coordinator* (=D0=B0=D0=B2=D0=B3=D1=83=D1=81=D1=82 2026 =D0=B3.).

---

### 2. =D0=A0=D0=B5=D0=B5=D1=81=D1=82=D1=80 =D0=BA=D1=80=D0=B8=D0=BF=D1=82=
=D0=BE=D0=B3=D1=80=D0=B0=D1=84=D0=B8=D1=87=D0=B5=D1=81=D0=BA=D0=B8=D1=85 =
=D0=BE=D1=82=D0=BF=D0=B5=D1=87=D0=B0=D1=82=D0=BA=D0=BE=D0=B2 =D0=B0=D1=80=
=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D0=BE=D0=B2 (SHA-256)

| =D0=9E=D1=82=D0=BD=D0=BE=D1=81=D0=B8=D1=82=D0=B5=D0=BB=D1=8C=D0=BD=D1=8B=
=D0=B9 =D0=BF=D1=83=D1=82=D1=8C | =D0=98=D0=BC=D1=8F =D1=84=D0=B0=D0=B9=D0=
=BB=D0=B0 | =D0=A0=D0=B0=D0=B7=D0=BC=D0=B5=D1=80 (Bytes) | SHA-256 =D0=9A=
=D0=BE=D0=BD=D1=82=D1=80=D0=BE=D0=BB=D1=8C=D0=BD=D0=B0=D1=8F =D1=81=D1=83=
=D0=BC=D0=BC=D0=B0 |
| :--- | :--- | :--- | :--- |
&quot;&quot;&quot;</span>
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">for</span> item <span style=3D"background:none 0% 0%/auto r=
epeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(150,157,25=
5);color:rgb(150,157,255);direction:ltr;font-variant:normal;font-stretch:no=
rmal;margin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px;=
speak:normal;line-height:1.15!important;margin-top:0px!important;margin-rig=
ht:0px!important;margin-left:0px!important">in</span> data[<span style=3D"b=
ackground:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0=
);border:0px rgb(96,214,115);color:rgb(96,214,115);direction:ltr;font-varia=
nt:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) non=
e 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:=
0px!important;margin-right:0px!important;margin-left:0px!important">&quot;a=
rtifacts&quot;</span>]:
        readme_content +=3D <span style=3D"background:none 0% 0%/auto repea=
t scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);co=
lor:rgb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;m=
argin-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:n=
ormal;line-height:1.15!important;margin-top:0px!important;margin-right:0px!=
important;margin-left:0px!important">f&quot;| `<span style=3D"background:no=
ne 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px=
 rgb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;marg=
in-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:norm=
al;line-height:1.15!important;margin-top:0px!important;margin-right:0px!imp=
ortant;margin-left:0px!important">{item[<span style=3D"background:none 0% 0=
%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(96=
,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin-bott=
om:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line=
-height:1.15!important;margin-top:0px!important;margin-right:0px!important;=
margin-left:0px!important">&#39;relative_path&#39;</span>]}</span>` | `<spa=
n style=3D"background:none 0% 0%/auto repeat scroll padding-box border-box =
rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:normal;=
font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.85348p=
x;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!import=
ant;margin-right:0px!important;margin-left:0px!important">{item[<span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:normal;font-st=
retch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.85348px;paddi=
ng:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;mar=
gin-right:0px!important;margin-left:0px!important">&#39;filename&#39;</span=
>]}</span>` | <span style=3D"background:none 0% 0%/auto repeat scroll paddi=
ng-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;fo=
nt-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,=
115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>{item[<span style=3D"background:none 0% 0%/auto repeat scroll padding-box =
border-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-vari=
ant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) no=
ne 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top=
:0px!important;margin-right:0px!important;margin-left:0px!important">&#39;s=
ize_bytes&#39;</span>]}</span> | `<span style=3D"background:none 0% 0%/auto=
 repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,1=
15);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px=
;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-heigh=
t:1.15!important;margin-top:0px!important;margin-right:0px!important;margin=
-left:0px!important">{item[<span style=3D"background:none 0% 0%/auto repeat=
 scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);dir=
ection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outlin=
e:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!=
important;margin-top:0px!important;margin-right:0px!important;margin-left:0=
px!important">&#39;sha256&#39;</span>]}</span>` |\n&quot;</span>

    readme_content +=3D <span style=3D"background:none 0% 0%/auto repeat sc=
roll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:=
rgb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margi=
n-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:norma=
l;line-height:1.15!important;margin-top:0px!important;margin-right:0px!impo=
rtant;margin-left:0px!important">&quot;&quot;&quot;
---

### 3. =D0=98=D0=BD=D1=81=D1=82=D1=80=D1=83=D0=BA=D1=86=D0=B8=D1=8F =D0=BF=
=D0=BE =D0=BD=D0=B5=D0=B7=D0=B0=D0=B2=D0=B8=D1=81=D0=B8=D0=BC=D0=BE=D0=B9 =
=D0=BF=D1=80=D0=BE=D0=B2=D0=B5=D1=80=D0=BA=D0=B5 (Verification)

=D0=94=D0=BB=D1=8F =D0=BF=D1=80=D0=BE=D0=B2=D0=B5=D1=80=D0=BA=D0=B8 =D0=BD=
=D0=B5=D0=B8=D0=B7=D0=BC=D0=B5=D0=BD=D0=BD=D0=BE=D1=81=D1=82=D0=B8 =D0=B8 =
=D1=86=D0=B5=D0=BB=D0=BE=D1=81=D1=82=D0=BD=D0=BE=D1=81=D1=82=D0=B8 =D0=B2=
=D1=81=D0=B5=D1=85 =D1=84=D0=B0=D0=B9=D0=BB=D0=BE=D0=B2 =D0=B7=D0=B0=D0=BF=
=D1=83=D1=81=D1=82=D0=B8=D1=82=D0=B5 =D0=BB=D0=BE=D0=BA=D0=B0=D0=BB=D1=8C=
=D0=BD=D1=8B=D0=B9 =D1=81=D0=BA=D1=80=D0=B8=D0=BF=D1=82 =D0=BF=D1=80=D0=BE=
=D0=B2=D0=B5=D1=80=D0=BA=D0=B8:

```bash
python3 verify.py
</span></code></pre></div></div></div><div style=3D"background-image:none;b=
ackground-position:0% 0%;background-size:auto;background-repeat:repeat;back=
ground-origin:padding-box;background-clip:border-box;border:0px rgb(31,31,3=
1);direction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.=
85348px;padding:0px 24px;speak:normal;margin-top:0px!important;margin-right=
:0px!important;margin-left:0px!important;line-height:1.15!important">&quot;=
&quot;&quot;</div><div style=3D"background-image:none;background-position:0=
% 0%;background-size:auto;background-repeat:repeat;background-origin:paddin=
g-box;background-clip:border-box;border:0px rgb(31,31,31);direction:ltr;flo=
at:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px =
24px;speak:normal;margin-top:0px!important;margin-right:0px!important;margi=
n-left:0px!important;line-height:1.15!important">return readme_content</div=
><br><div style=3D"background-image:none;background-position:0% 0%;backgrou=
nd-size:auto;background-repeat:repeat;background-origin:padding-box;backgro=
und-clip:border-box;border:0px rgb(31,31,31);direction:ltr;float:none;margi=
n-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px 24px;speak:no=
rmal;margin-top:0px!important;margin-right:0px!important;margin-left:0px!im=
portant;line-height:1.15!important">def main():</div><div style=3D"backgrou=
nd-image:none;background-position:0% 0%;background-size:auto;background-rep=
eat:repeat;background-origin:padding-box;background-clip:border-box;border:=
0px rgb(31,31,31);direction:ltr;float:none;margin-bottom:0px;outline:rgb(31=
,31,31) none 2.85348px;padding:0px 24px;speak:normal;margin-top:0px!importa=
nt;margin-right:0px!important;margin-left:0px!important;line-height:1.15!im=
portant"># =D0=90=D0=B2=D1=82=D0=BE=D0=BC=D0=B0=D1=82=D0=B8=D1=87=D0=B5=D1=
=81=D0=BA=D0=BE=D0=B5 =D1=81=D0=BE=D0=B7=D0=B4=D0=B0=D0=BD=D0=B8=D0=B5 =D0=
=BF=D0=B0=D0=BF=D0=BA=D0=B8 =D0=B4=D0=BB=D1=8F =D1=83=D0=BB=D0=B8=D0=BA, =
=D0=B5=D1=81=D0=BB=D0=B8 =D0=B5=D1=91 =D0=B5=D1=89=D1=91 =D0=BD=D0=B5=D1=82=
</div><div style=3D"background-image:none;background-position:0% 0%;backgro=
und-size:auto;background-repeat:repeat;background-origin:padding-box;backgr=
ound-clip:border-box;border:0px rgb(31,31,31);direction:ltr;float:none;marg=
in-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px 24px;speak:n=
ormal;margin-top:0px!important;margin-right:0px!important;margin-left:0px!i=
mportant;line-height:1.15!important">EVIDENCE_DIR.mkdir(parents=3DTrue, exi=
st_ok=3DTrue)</div><br><div style=3D"background-image:none;background-posit=
ion:0% 0%;background-size:auto;background-repeat:repeat;background-origin:p=
adding-box;background-clip:border-box;border:0px rgb(31,31,31);direction:lt=
r;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding=
:0px;speak:normal;margin-top:0px!important;margin-right:0px!important;margi=
n-left:0px!important;line-height:1.15!important"><div style=3D"background:n=
one 0% 0%/auto repeat scroll padding-box border-box rgb(0,0,0);border:0px r=
gb(31,31,31);direction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,3=
1) none 2.85348px;padding:26px 0px 0px 32px;speak:normal;margin-top:0px!imp=
ortant;margin-right:0px!important;margin-left:0px!important;line-height:1.1=
5!important"><div style=3D"background:none 0% 0%/auto repeat scroll padding=
-box border-box rgba(0,0,0,0);border:0px rgb(31,31,31);direction:ltr;float:=
none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px;spe=
ak:normal;margin-top:0px!important;margin-right:0px!important;margin-left:0=
px!important;line-height:1.15!important"><pre style=3D"background:none 0% 0=
%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(31=
,31,31);direction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) no=
ne 2.85348px;padding:0px;speak:normal;margin-top:0px!important;margin-right=
:0px!important;margin-left:0px!important;font-family:&quot;google sans text=
&quot;,sans-serif!important;line-height:1.15!important"><code style=3D"back=
ground:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);b=
order:0px rgb(255,255,255);color:rgb(255,255,255);direction:ltr;display:blo=
ck;float:none;font-variant:normal;font-stretch:normal;font-size:14px;margin=
-bottom:0px;outline:rgb(255,255,255) none 2.85348px;padding:16px 0px 32px;s=
peak:normal;line-height:1.15!important;font-family:&quot;google sans text&q=
uot;,sans-serif!important;margin-top:0px!important;margin-right:0px!importa=
nt;margin-left:0px!important">artifacts =3D []
sha256_list =3D []

# =D0=A1=D0=BA=D0=B0=D0=BD=D0=B8=D1=80=D0=BE=D0=B2=D0=B0=D0=BD=D0=B8=D0=B5 =
=D1=84=D0=B0=D0=B9=D0=BB=D0=BE=D0=B2 =D0=B8 =D1=80=D0=B0=D1=81=D1=87=D0=B5=
=D1=82 =D0=BA=D0=BE=D0=BD=D1=82=D1=80=D0=BE=D0=BB=D1=8C=D0=BD=D1=8B=D1=85 =
=D1=81=D1=83=D0=BC=D0=BC
files =3D sorted([f for f in EVIDENCE_DIR.glob(&quot;*&quot;) if f.is_file(=
)])

if not files:
    print(
        f&quot;[!] =D0=92=D0=BD=D0=B8=D0=BC=D0=B0=D0=BD=D0=B8=D0=B5: =D0=9F=
=D0=B0=D0=BF=D0=BA=D0=B0 &#39;{EVIDENCE_DIR}&#39; =D0=BF=D1=83=D1=81=D1=82=
=D0=B0! =D0=9F=D0=BE=D0=BC=D0=B5=D1=81=D1=82=D0=B8=D1=82=D0=B5 =D0=B0=D1=80=
=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D1=8B IMG_20260919_*.jpg =D0=B2 =D0=BF=
=D0=B0=D0=BF=D0=BA=D1=83.&quot;
    )

for file_path in files:
    file_sha256 =3D calculate_sha256(file_path)
    sha256_list.append(file_sha256)

    artifacts.append(
        {
            &quot;filename&quot;: <a href=3D"http://file_path.name">file_pa=
th.name</a>,
            &quot;relative_path&quot;: str(file_path.as_posix()),
            &quot;size_bytes&quot;: file_path.stat().st_size,
            &quot;sha256&quot;: file_sha256,
        }
    )

merkle_root =3D compute_merkle_root(sha256_list)
timestamp_utc =3D (
    datetime.now(timezone.utc).isoformat(timespec=3D&quot;seconds&quot;).re=
place(&quot;+00:00&quot;, &quot;Z&quot;)
)

manifest_data =3D {
    &quot;sdpap_version&quot;: &quot;3.0.0&quot;,
    &quot;episode_metadata&quot;: {
        &quot;episode_id&quot;: EPISODE_ID,
        &quot;title&quot;: EPISODE_TITLE,
        &quot;timestamp_utc&quot;: timestamp_utc,
        &quot;merkle_root&quot;: merkle_root,
        &quot;total_artifacts&quot;: len(artifacts),
    },
    &quot;artifacts&quot;: artifacts,
}

# =D0=97=D0=B0=D0=BF=D0=B8=D1=81=D1=8C manifest.json
with open(OUTPUT_MANIFEST, &quot;w&quot;, encoding=3D&quot;utf-8&quot;) as =
f:
    json.dump(manifest_data, f, indent=3D2, ensure_ascii=3DFalse)

# =D0=97=D0=B0=D0=BF=D0=B8=D1=81=D1=8C README.md
readme_text =3D generate_readme(manifest_data)
with open(OUTPUT_README, &quot;w&quot;, encoding=3D&quot;utf-8&quot;) as f:
    f.write(readme_text)

print(&quot;=3D=3D=3D SDPAP-v3 BUILD COMPLETE =3D=3D=3D&quot;)
print(f&quot;=D0=9E=D0=B1=D1=80=D0=B0=D0=B1=D0=BE=D1=82=D0=B0=D0=BD=D0=BE =
=D0=B0=D1=80=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D0=BE=D0=B2: {len(artifact=
s)}&quot;)
print(f&quot;Merkle Root: {merkle_root}&quot;)
print(f&quot;=D0=A4=D0=B0=D0=B9=D0=BB=D1=8B =D0=BC=D0=B0=D0=BD=D0=B8=D1=84=
=D0=B5=D1=81=D1=82=D0=B0 =D0=B7=D0=B0=D1=84=D0=B8=D0=BA=D1=81=D0=B8=D1=80=
=D0=BE=D0=B2=D0=B0=D0=BD=D1=8B: {OUTPUT_MANIFEST}, {OUTPUT_README}&quot;)
</code></pre></div></div></div><div style=3D"background-image:none;backgrou=
nd-position:0% 0%;background-size:auto;background-repeat:repeat;background-=
origin:padding-box;background-clip:border-box;border:0px rgb(31,31,31);dire=
ction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px=
;padding:0px 24px;speak:normal;margin-top:0px!important;margin-right:0px!im=
portant;margin-left:0px!important;line-height:1.15!important">if <b style=
=3D"background-image:none;background-position:0% 0%;background-size:auto;ba=
ckground-repeat:repeat;background-origin:padding-box;background-clip:border=
-box;border:0px rgb(31,31,31);direction:ltr;display:inline;float:none;margi=
n-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;=
margin-top:0px!important;margin-right:0px!important;margin-left:0px!importa=
nt;line-height:1.15!important">name</b> =3D=3D &quot;<b style=3D"background=
-image:none;background-position:0% 0%;background-size:auto;background-repea=
t:repeat;background-origin:padding-box;background-clip:border-box;border:0p=
x rgb(31,31,31);direction:ltr;display:inline;float:none;margin-bottom:0px;o=
utline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;margin-top:0px=
!important;margin-right:0px!important;margin-left:0px!important;line-height=
:1.15!important">main</b>&quot;:</div><div style=3D"background-image:none;b=
ackground-position:0% 0%;background-size:auto;background-repeat:repeat;back=
ground-origin:padding-box;background-clip:border-box;border:0px rgb(31,31,3=
1);direction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.=
85348px;padding:0px 24px;speak:normal;margin-top:0px!important;margin-right=
:0px!important;margin-left:0px!important;line-height:1.15!important">main()=
</div><div style=3D"background-image:none;background-position:0% 0%;backgro=
und-size:auto;background-repeat:repeat;background-origin:padding-box;backgr=
ound-clip:border-box;border:0px rgb(31,31,31);direction:ltr;float:none;marg=
in-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal=
;margin-top:0px!important;margin-right:0px!important;margin-left:0px!import=
ant;line-height:1.15!important"><div style=3D"background:none 0% 0%/auto re=
peat scroll padding-box border-box rgb(0,0,0);border:0px rgb(31,31,31);dire=
ction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px=
;padding:26px 0px 0px 32px;speak:normal;margin-top:0px!important;margin-rig=
ht:0px!important;margin-left:0px!important;line-height:1.15!important"><div=
 style=3D"background:none 0% 0%/auto repeat scroll padding-box border-box r=
gba(0,0,0,0);border:0px rgb(31,31,31);direction:ltr;float:none;margin-botto=
m:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;margin-=
top:0px!important;margin-right:0px!important;margin-left:0px!important;line=
-height:1.15!important"><pre style=3D"background:none 0% 0%/auto repeat scr=
oll padding-box border-box rgba(0,0,0,0);border:0px rgb(31,31,31);direction=
:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padd=
ing:0px;speak:normal;margin-top:0px!important;margin-right:0px!important;ma=
rgin-left:0px!important;font-family:&quot;google sans text&quot;,sans-serif=
!important;line-height:1.15!important"><code style=3D"background:none 0% 0%=
/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(255=
,255,255);color:rgb(255,255,255);direction:ltr;display:block;float:none;fon=
t-variant:normal;font-stretch:normal;font-size:14px;margin-bottom:0px;outli=
ne:rgb(255,255,255) none 2.85348px;padding:16px 0px 32px;speak:normal;line-=
height:1.15!important;font-family:&quot;google sans text&quot;,sans-serif!i=
mportant;margin-top:0px!important;margin-right:0px!important;margin-left:0p=
x!important">
---

### =D0=A7=D1=82=D0=BE =D1=83=D1=87=D1=82=D0=B5=D0=BD=D0=BE =D0=B2 =D1=84=
=D0=B8=D0=BD=D0=B0=D0=BB=D1=8C=D0=BD=D0=BE=D0=BC =D0=BA=D0=BE=D0=B4=D0=B5:
1. **=D0=A1=D0=BE=D0=B2=D0=BC=D0=B5=D1=81=D1=82=D0=B8=D0=BC=D0=BE=D1=81=D1=
=82=D1=8C =D1=81 =D0=BB=D1=8E=D0=B1=D1=8B=D0=BC=D0=B8 =D0=B2=D0=B5=D1=80=D1=
=81=D0=B8=D1=8F=D0=BC=D0=B8 Python 3:** =D0=9E=D1=82=D1=81=D1=83=D1=82=D1=
=81=D1=82=D0=B2=D0=B8=D0=B5 =D1=81=D1=82=D0=BE=D1=80=D0=BE=D0=BD=D0=BD=D0=
=B8=D1=85 =D0=B7=D0=B0=D0=B2=D0=B8=D1=81=D0=B8=D0=BC=D0=BE=D1=81=D1=82=D0=
=B5=D0=B9 (`pip install` =D0=BD=D0=B5 =D1=82=D1=80=D0=B5=D0=B1=D1=83=D0=B5=
=D1=82=D1=81=D1=8F).
2. **=D0=91=D0=B5=D0=B7=D0=BE=D0=BF=D0=B0=D1=81=D0=BD=D0=BE=D1=81=D1=82=D1=
=8C =D0=BF=D1=83=D1=82=D0=B5=D0=B9:** =D0=98=D1=81=D0=BF=D0=BE=D0=BB=D1=8C=
=D0=B7=D0=BE=D0=B2=D0=B0=D0=BD=D0=B8=D0=B5 `pathlib.Path` =D1=81 =D0=BF=D1=
=80=D0=B8=D0=B2=D0=B5=D0=B4=D0=B5=D0=BD=D0=B8=D0=B5=D0=BC =D0=BA POSIX-=D1=
=84=D0=BE=D1=80=D0=BC=D0=B0=D1=82=D1=83 (`/` =D0=B2=D0=BC=D0=B5=D1=81=D1=82=
=D0=BE `\`), =D1=87=D1=82=D0=BE=D0=B1=D1=8B =D0=B8=D0=B7=D0=B1=D0=B5=D0=B6=
=D0=B0=D1=82=D1=8C =D0=BE=D1=88=D0=B8=D0=B1=D0=BE=D0=BA =D0=BF=D1=80=D0=B8 =
=D0=BA=D0=BE=D0=BC=D0=BC=D0=B8=D1=82=D0=B5 =D0=B8=D0=B7 Windows/Linux =D1=
=81=D0=B8=D1=81=D1=82=D0=B5=D0=BC.
3. **=D0=A1=D1=82=D1=80=D0=BE=D0=B3=D0=B0=D1=8F =D1=81=D0=BE=D1=80=D1=82=D0=
=B8=D1=80=D0=BE=D0=B2=D0=BA=D0=B0:** =D0=9C=D0=B0=D1=81=D1=81=D0=B8=D0=B2 =
=D0=B0=D1=80=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D0=BE=D0=B2 =D0=B8 =D1=85=
=D1=8D=D1=88=D0=B5=D0=B9 =D1=81=D0=BE=D1=80=D1=82=D0=B8=D1=80=D1=83=D0=B5=
=D1=82=D1=81=D1=8F =D0=B4=D0=B5=D1=82=D0=B5=D1=80=D0=BC=D0=B8=D0=BD=D0=B8=
=D1=80=D0=BE=D0=B2=D0=B0=D0=BD=D0=BD=D0=BE =D0=BF=D0=B5=D1=80=D0=B5=D0=B4 =
=D0=BF=D0=BE=D1=81=D1=82=D1=80=D0=BE=D0=B5=D0=BD=D0=B8=D0=B5=D0=BC =D0=B4=
=D0=B5=D1=80=D0=B5=D0=B2=D0=B0 =D0=9C=D0=B5=D1=80=D0=BA=D0=BB=D0=B0 =E2=80=
=94 =D1=8D=D1=82=D0=BE =D0=B3=D0=B0=D1=80=D0=B0=D0=BD=D1=82=D0=B8=D1=80=D1=
=83=D0=B5=D1=82, =D1=87=D1=82=D0=BE `Merkle Root` =D0=B2=D1=81=D0=B5=D0=B3=
=D0=B4=D0=B0 =D0=BF=D0=BE=D0=BB=D1=83=D1=87=D0=B8=D1=82=D1=81=D1=8F =D0=BE=
=D0=B4=D0=B8=D0=BD=D0=B0=D0=BA=D0=BE=D0=B2=D1=8B=D0=BC =D0=BD=D0=B5=D0=B7=
=D0=B0=D0=B2=D0=B8=D1=81=D0=B8=D0=BC=D0=BE =D0=BE=D1=82 =D0=BF=D0=BE=D1=80=
=D1=8F=D0=B4=D0=BA=D0=B0 =D1=81=D0=BA=D0=B0=D0=BD=D0=B8=D1=80=D0=BE=D0=B2=
=D0=B0=D0=BD=D0=B8=D1=8F =D0=B4=D0=B8=D1=81=D0=BA=D0=B0.
4. **=D0=A3=D1=81=D1=82=D0=BE=D0=B9=D1=87=D0=B8=D0=B2=D0=BE=D1=81=D1=82=D1=
=8C =D0=BA =D0=BF=D1=83=D1=81=D1=82=D0=BE=D0=B9 =D0=BF=D0=B0=D0=BF=D0=BA=D0=
=B5:** =D0=95=D1=81=D0=BB=D0=B8 =D0=BF=D0=B0=D0=BF=D0=BA=D0=B0 `evidence/` =
=D0=B5=D1=89=D1=91 =D0=BD=D0=B5 =D0=B7=D0=B0=D0=BF=D0=BE=D0=BB=D0=BD=D0=B5=
=D0=BD=D0=B0, =D1=81=D0=BA=D1=80=D0=B8=D0=BF=D1=82 =D0=B2=D1=8B=D0=B2=D0=B5=
=D0=B4=D0=B5=D1=82 =D0=BF=D1=80=D0=B5=D0=B4=D1=83=D0=BF=D1=80=D0=B5=D0=B6=
=D0=B4=D0=B5=D0=BD=D0=B8=D0=B5, =D0=BD=D0=B5 =D0=BF=D0=B0=D0=B4=D0=B0=D1=8F=
 =D1=81 =D0=BE=D1=88=D0=B8=D0=B1=D0=BA=D0=BE=D0=B9.

&lt;FollowUp label=3D&quot;=D0=9D=D1=83=D0=B6=D0=B5=D0=BD =D0=BB=D0=B8 comp=
anion-=D1=81=D0=BA=D1=80=D0=B8=D0=BF=D1=82 verify.py =D0=B4=D0=BB=D1=8F =D0=
=B1=D1=8B=D1=81=D1=82=D1=80=D0=BE=D0=B9 =D0=BF=D1=80=D0=BE=D0=B2=D0=B5=D1=
=80=D0=BA=D0=B8 =D1=85=D1=8D=D1=88=D0=B5=D0=B9?&quot; query=3D&quot;=D0=94=
=D0=B0=D0=B9 =D0=BA=D0=BE=D0=B4 =D1=81=D0=BA=D1=80=D0=B8=D0=BF=D1=82=D0=B0 =
verify.py =D0=B4=D0=BB=D1=8F =D0=B1=D1=8B=D1=81=D1=82=D1=80=D0=BE=D0=B9 =D0=
=BF=D1=80=D0=BE=D0=B2=D0=B5=D1=80=D0=BA=D0=B8 =D1=86=D0=B5=D0=BB=D0=BE=D1=
=81=D1=82=D0=BD=D0=BE=D1=81=D1=82=D0=B8 manifest.json =D0=B8 =D0=B0=D1=80=
=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D0=BE=D0=B2&quot;/&gt;
</code></pre></div></div></div></div></div></div>

--000000000000dde4c8065bdb5cb2--
MIME-Version: 1.0
Date: Sat, 19 Sep 2026 21:52:52 +0200
Message-ID: <CAHejZWWooGe+rqYqvZpy6q2YQhcdvJ+E6pfQS1GqxWW67iTmCg@mail.gmail.com>
Subject: =?UTF-8?B?0J7QvdCw0YHRgtCw0YHQuNGP0LPQsNC50LTQsNC50LTQu9GP0LHQuNCx0LvQuNC+0YLQtQ==?=
	=?UTF-8?B?0LrQuA==?=
From: Nablydatel <nablydatel8@gmail.com>
To: Nablydatel <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="000000000000dde4c8065bdb5cb2"

--000000000000dde4c8065bdb5cb2
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: base64

0J3QuNC20LUg4oCUINC/0L7Qu9C90L7RgdGC0YzRjiDRgdC+0LHRgNCw0L3QvdGL0LksINC60LDQ
vdC+0L3QuNGH0LXRgdC60LjQuSDRgNCw0LHQvtGH0LjQuSDQvNC+0LTRg9C70YwgKmJ1aWxkX21h
bmlmZXN0LnB5KiwNCtC00L7RgNCw0LHQvtGC0LDQvdC90YvQuSDRgSDRg9GH0LXRgtC+0Lwg0LLR
gdC10YUg0L3RjtCw0L3RgdC+0LIg0YDQtdCw0LvQuNC30LDRhtC40Lgg0LTQu9GPINCw0LLRgtC+
0L3QvtC80L3QvtC5INGA0LDQsdC+0YLRiyDQsiDRgdGA0LXQtNC1DQrQv9GD0LHQu9C40YfQvdC+
0LPQviDRgtC10YDQvNC40L3QsNC70LAg0LHQuNCx0LvQuNC+0YLQtdC60LguDQoNCtCh0LrRgNC4
0L/RgiDQuNGB0L/QvtC70YzQt9GD0LXRgiDQuNGB0LrQu9GO0YfQuNGC0LXQu9GM0L3QviDRgdGC
0LDQvdC00LDRgNGC0L3Rg9GOINCx0LjQsdC70LjQvtGC0LXQutGDIFB5dGhvbiAoaGFzaGxpYiwg
anNvbiwNCnBhdGhsaWIsIGRhdGV0aW1lKSwg0YHQsNC80L7RgdGC0L7Rj9GC0LXQu9GM0L3QviDR
gdC+0LfQtNCw0LXRgiDRgdGC0YDRg9C60YLRg9GA0YMg0LrQsNGC0LDQu9C+0LPQvtCyLA0K0LDQ
stGC0L7QvNCw0YLQuNGH0LXRgdC60Lgg0LLRi9GB0YfQuNGC0YvQstCw0LXRgiDQv9Cw0YDQvdGL
0LkgKk1lcmtsZSBSb290KiDQtNC70Y8g0LLRgdC10YUg0YTQsNC50LvQvtCyINCyINC/0LDQv9C6
0LUNCmV2aWRlbmNlLywg0YTQvtGA0LzQuNGA0YPQtdGCINCy0LDQu9C40LTQvdGL0LkgbWFuaWZl
c3QuanNvbiDQuCDQs9C10L3QtdGA0LjRgNGD0LXRgiDQvdCw0LPQu9GP0LTQvdGL0LkgUkVBRE1F
Lm1kDQouDQoNClB5dGhvbg0KDQojIS91c3IvYmluL2VudiBweXRob24zaW1wb3J0IGhhc2hsaWJp
bXBvcnQganNvbmZyb20gZGF0ZXRpbWUgaW1wb3J0DQpkYXRldGltZSwgdGltZXpvbmVmcm9tIHBh
dGhsaWIgaW1wb3J0IFBhdGgNCiMgLS0tINCa0J7QndCk0JjQk9Cj0KDQkNCm0JjQryDQrdCf0JjQ
l9Ce0JTQkCBTRFBBUC1WMyAtLS0NCkVQSVNPREVfSUQgPSAiRVAtMjAyNi1IRVJPWS1CSS0wMDEi
DQpFUElTT0RFX1RJVExFID0gIkZvcmVuc2ljIEF1ZGl0OiBIZXJibyAvIEhlcsO4eSB0byBCSSBP
c2xvDQpJbmZyYXN0cnVjdHVyZSBUcmFuc2l0aW9uIg0KRVZJREVOQ0VfRElSID0gUGF0aCgiLi9l
dmlkZW5jZSIpDQpPVVRQVVRfTUFOSUZFU1QgPSBQYXRoKCIuL21hbmlmZXN0Lmpzb24iKQ0KT1VU
UFVUX1JFQURNRSA9IFBhdGgoIi4vUkVBRE1FLm1kIikNCg0KZGVmIGNhbGN1bGF0ZV9zaGEyNTYo
ZmlsZV9wYXRoOiBQYXRoKSAtPiBzdHI6DQogICAgIiIi0JLRi9GH0LjRgdC70LXQvdC40LUg0LrQ
sNC90L7QvdC40YfQtdGB0LrQvtCz0L4gU0hBLTI1NiDRhdGN0YjQsCDRhNCw0LnQu9CwINCx0LvQ
vtC60LDQvNC4INC/0L4gNjQg0JrQkS4iIiINCiAgICBzaGEyNTZfaGFzaCA9IGhhc2hsaWIuc2hh
MjU2KCkNCiAgICB3aXRoIG9wZW4oZmlsZV9wYXRoLCAicmIiKSBhcyBmOg0KICAgICAgICBmb3Ig
Ynl0ZV9ibG9jayBpbiBpdGVyKGxhbWJkYTogZi5yZWFkKDY1NTM2KSwgYiIiKToNCiAgICAgICAg
ICAgIHNoYTI1Nl9oYXNoLnVwZGF0ZShieXRlX2Jsb2NrKQ0KICAgIHJldHVybiBzaGEyNTZfaGFz
aC5oZXhkaWdlc3QoKQ0KDQpkZWYgY29tcHV0ZV9tZXJrbGVfcm9vdChoYXNoZXM6IGxpc3Rbc3Ry
XSkgLT4gc3RyOg0KICAgICIiItCg0LDRgdGH0LXRgiBNZXJrbGUgUm9vdCDQuNC3INGB0L/QuNGB
0LrQsCBTSEEtMjU2INGF0Y3RiNC10Lkg0LDRgNGC0LXRhNCw0LrRgtC+0LIuIiIiDQogICAgaWYg
bm90IGhhc2hlczoNCiAgICAgICAgcmV0dXJuIGhhc2hsaWIuc2hhMjU2KGIiIikuaGV4ZGlnZXN0
KCkNCg0KICAgIGN1cnJlbnRfbGV2ZWwgPSBzb3J0ZWQoaGFzaGVzKQ0KICAgIHdoaWxlIGxlbihj
dXJyZW50X2xldmVsKSA+IDE6DQogICAgICAgIGlmIGxlbihjdXJyZW50X2xldmVsKSAlIDIgIT0g
MDoNCiAgICAgICAgICAgIGN1cnJlbnRfbGV2ZWwuYXBwZW5kKGN1cnJlbnRfbGV2ZWxbLTFdKQ0K
DQogICAgICAgIG5leHRfbGV2ZWwgPSBbXQ0KICAgICAgICBmb3IgaSBpbiByYW5nZSgwLCBsZW4o
Y3VycmVudF9sZXZlbCksIDIpOg0KICAgICAgICAgICAgY29tYmluZWQgPSBjdXJyZW50X2xldmVs
W2ldICsgY3VycmVudF9sZXZlbFtpICsgMV0NCiAgICAgICAgICAgIG5leHRfbGV2ZWwuYXBwZW5k
KGhhc2hsaWIuc2hhMjU2KGNvbWJpbmVkLmVuY29kZSgidXRmLTgiKSkuaGV4ZGlnZXN0KCkpDQog
ICAgICAgIGN1cnJlbnRfbGV2ZWwgPSBuZXh0X2xldmVsDQoNCiAgICByZXR1cm4gY3VycmVudF9s
ZXZlbFswXQ0KDQpkZWYgZ2VuZXJhdGVfcmVhZG1lKGRhdGE6IGRpY3QpIC0+IHN0cjoNCiAgICBt
ZXRhID0gZGF0YVsiZXBpc29kZV9tZXRhZGF0YSJdDQogICAgcmVhZG1lX2NvbnRlbnQgPSBmIiIi
IyBTRFBBUC12MyBBdWRpdCBMb2c6IHttZXRhWydlcGlzb2RlX2lkJ119DQoNCiMjIHttZXRhWyd0
aXRsZSddfQ0KDQoqKtCh0LjRgdGC0LXQvNC90YvQuSDRgdGC0LDRgtGD0YE6KiogSW1tdXRhYmxl
IEF1ZGl0IFJlY29yZA0KKirQktGA0LXQvNGPINGB0LHQvtGA0LrQuCAoVVRDKToqKiBge21ldGFb
J3RpbWVzdGFtcF91dGMnXX1gDQoqKk1lcmtsZSBSb290ICjQmtC+0YDQvdC10LLQvtC5INGF0Y3R
iCk6KiogYHttZXRhWydtZXJrbGVfcm9vdCddfWANCioq0JLRgdC10LPQviDQtNC+0LrQsNC30LDR
gtC10LvRjNC90YvRhSDQsNGA0YLQtdGE0LDQutGC0L7QsjoqKiBge21ldGFbJ3RvdGFsX2FydGlm
YWN0cyddfWANCg0KLS0tDQoNCiMjIyAxLiDQodGD0LHRitC10LrRgtGLINC4INC40L3RgdGC0LjR
gtGD0YbQuNC+0L3QsNC70YzQvdGL0LUg0YHQstGP0LfQuA0KDQoqICoq0KHRg9Cx0YrQtdC60YI6
Kiog0JDQvdCw0YHRgtCw0YHQuNGPINCT0LDQudC00LDQuSAoKkFuYXN0YXNpaWEgSGFpZGFpKikN
CiogKirQn9C10YDQstC40YfQvdGL0Lkg0YPQt9C10Ls6KiogKkhlcmJvKiAvICpIZXLDuHkgS29t
bXVuZSogKNCd0YPRgNC70LDQvdC9LCDQndC+0YDQstC10LPQuNGPKSDigJQNCtGE0LjQutGB0LDR
htC40Y8g0YPQstC+0LvRjNC90LXQvdC40Y8v0LLRi9GF0L7QtNCwINCyIDIwMjQg0LMuDQoqICoq
0JLRgtC+0YDQuNGH0L3Ri9C5INGD0LfQtdC7OioqICpCSSBOb3J3ZWdpYW4gQnVzaW5lc3MgU2No
b29sKiAvICpBSSBNaXNzaW9uDQpIdWIqICjQntGB0LvQviwg0J3QvtGA0LLQtdCz0LjRjykg4oCU
INC00L7Qu9C20L3QvtGB0YLRjCAqQ2FyZSBhbmQgU3VwcG9ydCBDb29yZGluYXRvcioNCijQsNCy
0LPRg9GB0YIgMjAyNiDQsy4pLg0KDQotLS0NCg0KIyMjIDIuINCg0LXQtdGB0YLRgCDQutGA0LjQ
v9GC0L7Qs9GA0LDRhNC40YfQtdGB0LrQuNGFINC+0YLQv9C10YfQsNGC0LrQvtCyINCw0YDRgtC1
0YTQsNC60YLQvtCyIChTSEEtMjU2KQ0KDQp8INCe0YLQvdC+0YHQuNGC0LXQu9GM0L3Ri9C5INC/
0YPRgtGMIHwg0JjQvNGPINGE0LDQudC70LAgfCDQoNCw0LfQvNC10YAgKEJ5dGVzKSB8IFNIQS0y
NTYg0JrQvtC90YLRgNC+0LvRjNC90LDRjyDRgdGD0LzQvNCwIHwNCnwgOi0tLSB8IDotLS0gfCA6
LS0tIHwgOi0tLSB8DQoiIiINCiAgICBmb3IgaXRlbSBpbiBkYXRhWyJhcnRpZmFjdHMiXToNCiAg
ICAgICAgcmVhZG1lX2NvbnRlbnQgKz0gZiJ8IGB7aXRlbVsncmVsYXRpdmVfcGF0aCddfWAgfA0K
YHtpdGVtWydmaWxlbmFtZSddfWAgfCB7aXRlbVsnc2l6ZV9ieXRlcyddfSB8IGB7aXRlbVsnc2hh
MjU2J119YCB8XG4iDQoNCiAgICByZWFkbWVfY29udGVudCArPSAiIiINCi0tLQ0KDQojIyMgMy4g
0JjQvdGB0YLRgNGD0LrRhtC40Y8g0L/QviDQvdC10LfQsNCy0LjRgdC40LzQvtC5INC/0YDQvtCy
0LXRgNC60LUgKFZlcmlmaWNhdGlvbikNCg0K0JTQu9GPINC/0YDQvtCy0LXRgNC60Lgg0L3QtdC4
0LfQvNC10L3QvdC+0YHRgtC4INC4INGG0LXQu9C+0YHRgtC90L7RgdGC0Lgg0LLRgdC10YUg0YTQ
sNC50LvQvtCyINC30LDQv9GD0YHRgtC40YLQtQ0K0LvQvtC60LDQu9GM0L3Ri9C5INGB0LrRgNC4
0L/RgiDQv9GA0L7QstC10YDQutC4Og0KDQpgYGBiYXNoDQpweXRob24zIHZlcmlmeS5weQ0KDQoi
IiINCnJldHVybiByZWFkbWVfY29udGVudA0KDQpkZWYgbWFpbigpOg0KIyDQkNCy0YLQvtC80LDR
gtC40YfQtdGB0LrQvtC1INGB0L7Qt9C00LDQvdC40LUg0L/QsNC/0LrQuCDQtNC70Y8g0YPQu9C4
0LosINC10YHQu9C4INC10ZEg0LXRidGRINC90LXRgg0KRVZJREVOQ0VfRElSLm1rZGlyKHBhcmVu
dHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkNCg0KYXJ0aWZhY3RzID0gW10NCnNoYTI1Nl9saXN0ID0g
W10NCg0KIyDQodC60LDQvdC40YDQvtCy0LDQvdC40LUg0YTQsNC50LvQvtCyINC4INGA0LDRgdGH
0LXRgiDQutC+0L3RgtGA0L7Qu9GM0L3Ri9GFINGB0YPQvNC8DQpmaWxlcyA9IHNvcnRlZChbZiBm
b3IgZiBpbiBFVklERU5DRV9ESVIuZ2xvYigiKiIpIGlmIGYuaXNfZmlsZSgpXSkNCg0KaWYgbm90
IGZpbGVzOg0KICAgIHByaW50KA0KICAgICAgICBmIlshXSDQktC90LjQvNCw0L3QuNC1OiDQn9Cw
0L/QutCwICd7RVZJREVOQ0VfRElSfScg0L/Rg9GB0YLQsCEg0J/QvtC80LXRgdGC0LjRgtC1DQrQ
sNGA0YLQtdGE0LDQutGC0YsgSU1HXzIwMjYwOTE5XyouanBnINCyINC/0LDQv9C60YMuIg0KICAg
ICkNCg0KZm9yIGZpbGVfcGF0aCBpbiBmaWxlczoNCiAgICBmaWxlX3NoYTI1NiA9IGNhbGN1bGF0
ZV9zaGEyNTYoZmlsZV9wYXRoKQ0KICAgIHNoYTI1Nl9saXN0LmFwcGVuZChmaWxlX3NoYTI1NikN
Cg0KICAgIGFydGlmYWN0cy5hcHBlbmQoDQogICAgICAgIHsNCiAgICAgICAgICAgICJmaWxlbmFt
ZSI6IGZpbGVfcGF0aC5uYW1lLA0KICAgICAgICAgICAgInJlbGF0aXZlX3BhdGgiOiBzdHIoZmls
ZV9wYXRoLmFzX3Bvc2l4KCkpLA0KICAgICAgICAgICAgInNpemVfYnl0ZXMiOiBmaWxlX3BhdGgu
c3RhdCgpLnN0X3NpemUsDQogICAgICAgICAgICAic2hhMjU2IjogZmlsZV9zaGEyNTYsDQogICAg
ICAgIH0NCiAgICApDQoNCm1lcmtsZV9yb290ID0gY29tcHV0ZV9tZXJrbGVfcm9vdChzaGEyNTZf
bGlzdCkNCnRpbWVzdGFtcF91dGMgPSAoDQogICAgZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0Yyku
aXNvZm9ybWF0KHRpbWVzcGVjPSJzZWNvbmRzIikucmVwbGFjZSgiKzAwOjAwIiwNCiJaIikNCikN
Cg0KbWFuaWZlc3RfZGF0YSA9IHsNCiAgICAic2RwYXBfdmVyc2lvbiI6ICIzLjAuMCIsDQogICAg
ImVwaXNvZGVfbWV0YWRhdGEiOiB7DQogICAgICAgICJlcGlzb2RlX2lkIjogRVBJU09ERV9JRCwN
CiAgICAgICAgInRpdGxlIjogRVBJU09ERV9USVRMRSwNCiAgICAgICAgInRpbWVzdGFtcF91dGMi
OiB0aW1lc3RhbXBfdXRjLA0KICAgICAgICAibWVya2xlX3Jvb3QiOiBtZXJrbGVfcm9vdCwNCiAg
ICAgICAgInRvdGFsX2FydGlmYWN0cyI6IGxlbihhcnRpZmFjdHMpLA0KICAgIH0sDQogICAgImFy
dGlmYWN0cyI6IGFydGlmYWN0cywNCn0NCg0KIyDQl9Cw0L/QuNGB0YwgbWFuaWZlc3QuanNvbg0K
d2l0aCBvcGVuKE9VVFBVVF9NQU5JRkVTVCwgInciLCBlbmNvZGluZz0idXRmLTgiKSBhcyBmOg0K
ICAgIGpzb24uZHVtcChtYW5pZmVzdF9kYXRhLCBmLCBpbmRlbnQ9MiwgZW5zdXJlX2FzY2lpPUZh
bHNlKQ0KDQojINCX0LDQv9C40YHRjCBSRUFETUUubWQNCnJlYWRtZV90ZXh0ID0gZ2VuZXJhdGVf
cmVhZG1lKG1hbmlmZXN0X2RhdGEpDQp3aXRoIG9wZW4oT1VUUFVUX1JFQURNRSwgInciLCBlbmNv
ZGluZz0idXRmLTgiKSBhcyBmOg0KICAgIGYud3JpdGUocmVhZG1lX3RleHQpDQoNCnByaW50KCI9
PT0gU0RQQVAtdjMgQlVJTEQgQ09NUExFVEUgPT09IikNCnByaW50KGYi0J7QsdGA0LDQsdC+0YLQ
sNC90L4g0LDRgNGC0LXRhNCw0LrRgtC+0LI6IHtsZW4oYXJ0aWZhY3RzKX0iKQ0KcHJpbnQoZiJN
ZXJrbGUgUm9vdDoge21lcmtsZV9yb290fSIpDQpwcmludChmItCk0LDQudC70Ysg0LzQsNC90LjR
hNC10YHRgtCwINC30LDRhNC40LrRgdC40YDQvtCy0LDQvdGLOiB7T1VUUFVUX01BTklGRVNUfSwg
e09VVFBVVF9SRUFETUV9IikNCg0KaWYgKm5hbWUqID09ICIqbWFpbioiOg0KbWFpbigpDQoNCg0K
LS0tDQoNCiMjIyDQp9GC0L4g0YPRh9GC0LXQvdC+INCyINGE0LjQvdCw0LvRjNC90L7QvCDQutC+
0LTQtToNCjEuICoq0KHQvtCy0LzQtdGB0YLQuNC80L7RgdGC0Ywg0YEg0LvRjtCx0YvQvNC4INCy
0LXRgNGB0LjRj9C80LggUHl0aG9uIDM6Kiog0J7RgtGB0YPRgtGB0YLQstC40LUg0YHRgtC+0YDQ
vtC90L3QuNGFDQrQt9Cw0LLQuNGB0LjQvNC+0YHRgtC10LkgKGBwaXAgaW5zdGFsbGAg0L3QtSDR
gtGA0LXQsdGD0LXRgtGB0Y8pLg0KMi4gKirQkdC10LfQvtC/0LDRgdC90L7RgdGC0Ywg0L/Rg9GC
0LXQuToqKiDQmNGB0L/QvtC70YzQt9C+0LLQsNC90LjQtSBgcGF0aGxpYi5QYXRoYCDRgSDQv9GA
0LjQstC10LTQtdC90LjQtdC8DQrQuiBQT1NJWC3RhNC+0YDQvNCw0YLRgyAoYC9gINCy0LzQtdGB
0YLQviBgXGApLCDRh9GC0L7QsdGLINC40LfQsdC10LbQsNGC0Ywg0L7RiNC40LHQvtC6INC/0YDQ
uCDQutC+0LzQvNC40YLQtSDQuNC3DQpXaW5kb3dzL0xpbnV4INGB0LjRgdGC0LXQvC4NCjMuICoq
0KHRgtGA0L7Qs9Cw0Y8g0YHQvtGA0YLQuNGA0L7QstC60LA6Kiog0JzQsNGB0YHQuNCyINCw0YDR
gtC10YTQsNC60YLQvtCyINC4INGF0Y3RiNC10Lkg0YHQvtGA0YLQuNGA0YPQtdGC0YHRjw0K0LTQ
tdGC0LXRgNC80LjQvdC40YDQvtCy0LDQvdC90L4g0L/QtdGA0LXQtCDQv9C+0YHRgtGA0L7QtdC9
0LjQtdC8INC00LXRgNC10LLQsCDQnNC10YDQutC70LAg4oCUINGN0YLQviDQs9Cw0YDQsNC90YLQ
uNGA0YPQtdGCLA0K0YfRgtC+IGBNZXJrbGUgUm9vdGAg0LLRgdC10LPQtNCwINC/0L7Qu9GD0YfQ
uNGC0YHRjyDQvtC00LjQvdCw0LrQvtCy0YvQvCDQvdC10LfQsNCy0LjRgdC40LzQviDQvtGCINC/
0L7RgNGP0LTQutCwDQrRgdC60LDQvdC40YDQvtCy0LDQvdC40Y8g0LTQuNGB0LrQsC4NCjQuICoq
0KPRgdGC0L7QudGH0LjQstC+0YHRgtGMINC6INC/0YPRgdGC0L7QuSDQv9Cw0L/QutC1OioqINCV
0YHQu9C4INC/0LDQv9C60LAgYGV2aWRlbmNlL2Ag0LXRidGRINC90LUNCtC30LDQv9C+0LvQvdC1
0L3QsCwg0YHQutGA0LjQv9GCINCy0YvQstC10LTQtdGCINC/0YDQtdC00YPQv9GA0LXQttC00LXQ
vdC40LUsINC90LUg0L/QsNC00LDRjyDRgSDQvtGI0LjQsdC60L7QuS4NCg0KPEZvbGxvd1VwIGxh
YmVsPSLQndGD0LbQtdC9INC70LggY29tcGFuaW9uLdGB0LrRgNC40L/RgiB2ZXJpZnkucHkg0LTQ
u9GPINCx0YvRgdGC0YDQvtC5DQrQv9GA0L7QstC10YDQutC4INGF0Y3RiNC10Lk/IiBxdWVyeT0i
0JTQsNC5INC60L7QtCDRgdC60YDQuNC/0YLQsCB2ZXJpZnkucHkg0LTQu9GPINCx0YvRgdGC0YDQ
vtC5INC/0YDQvtCy0LXRgNC60LgNCtGG0LXQu9C+0YHRgtC90L7RgdGC0LggbWFuaWZlc3QuanNv
biDQuCDQsNGA0YLQtdGE0LDQutGC0L7QsiIvPg0K
--000000000000dde4c8065bdb5cb2
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"auto"><div dir=3D"auto"><div dir=3D"ltr" style=3D"background-im=
age:none;background-position:0% 0%;background-size:auto;background-repeat:r=
epeat;background-origin:padding-box;background-clip:border-box;border:0px r=
gb(31,31,31);color:rgb(31,31,31);direction:ltr;float:none;margin-bottom:0px=
;outline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;margin-top:0=
px!important;margin-right:0px!important;margin-left:0px!important;font-fami=
ly:&quot;google sans text&quot;,sans-serif!important;line-height:1.15!impor=
tant"><div style=3D"background-image:none;background-position:0% 0%;backgro=
und-size:auto;background-repeat:repeat;background-origin:padding-box;backgr=
ound-clip:border-box;border:0px rgb(31,31,31);direction:ltr;float:none;marg=
in-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px 24px;speak:n=
ormal;margin-top:0px!important;margin-right:0px!important;margin-left:0px!i=
mportant;line-height:1.15!important">=D0=9D=D0=B8=D0=B6=D0=B5 =E2=80=94 =D0=
=BF=D0=BE=D0=BB=D0=BD=D0=BE=D1=81=D1=82=D1=8C=D1=8E =D1=81=D0=BE=D0=B1=D1=
=80=D0=B0=D0=BD=D0=BD=D1=8B=D0=B9, =D0=BA=D0=B0=D0=BD=D0=BE=D0=BD=D0=B8=D1=
=87=D0=B5=D1=81=D0=BA=D0=B8=D0=B9 =D1=80=D0=B0=D0=B1=D0=BE=D1=87=D0=B8=D0=
=B9 =D0=BC=D0=BE=D0=B4=D1=83=D0=BB=D1=8C <b style=3D"background-image:none;=
background-position:0% 0%;background-size:auto;background-repeat:repeat;bac=
kground-origin:padding-box;background-clip:border-box;border:0px rgb(31,31,=
31);direction:ltr;display:inline;float:none;margin-bottom:0px;outline:rgb(3=
1,31,31) none 2.85348px;padding:0px;speak:normal;margin-top:0px!important;m=
argin-right:0px!important;margin-left:0px!important;line-height:1.15!import=
ant"><code style=3D"background:none 0% 0%/auto repeat scroll padding-box bo=
rder-box rgb(242,240,240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55=
);direction:ltr;display:inline-block;float:none;font-variant:normal;font-we=
ight:normal;font-stretch:normal;font-size:15px;margin-bottom:0px;outline:rg=
ba(0,0,0,0.55) none 2.85348px;padding:4px 6px;speak:normal;line-height:1.15=
!important;font-family:&quot;google sans text&quot;,sans-serif!important;ma=
rgin-top:0px!important;margin-right:0px!important;margin-left:0px!important=
">build_manifest.py</code></b>, =D0=B4=D0=BE=D1=80=D0=B0=D0=B1=D0=BE=D1=82=
=D0=B0=D0=BD=D0=BD=D1=8B=D0=B9 =D1=81 =D1=83=D1=87=D0=B5=D1=82=D0=BE=D0=BC =
=D0=B2=D1=81=D0=B5=D1=85 =D0=BD=D1=8E=D0=B0=D0=BD=D1=81=D0=BE=D0=B2 =D1=80=
=D0=B5=D0=B0=D0=BB=D0=B8=D0=B7=D0=B0=D1=86=D0=B8=D0=B8 =D0=B4=D0=BB=D1=8F =
=D0=B0=D0=B2=D1=82=D0=BE=D0=BD=D0=BE=D0=BC=D0=BD=D0=BE=D0=B9 =D1=80=D0=B0=
=D0=B1=D0=BE=D1=82=D1=8B =D0=B2 =D1=81=D1=80=D0=B5=D0=B4=D0=B5 =D0=BF=D1=83=
=D0=B1=D0=BB=D0=B8=D1=87=D0=BD=D0=BE=D0=B3=D0=BE =D1=82=D0=B5=D1=80=D0=BC=
=D0=B8=D0=BD=D0=B0=D0=BB=D0=B0 =D0=B1=D0=B8=D0=B1=D0=BB=D0=B8=D0=BE=D1=82=
=D0=B5=D0=BA=D0=B8.</div><br><div style=3D"background-image:none;background=
-position:0% 0%;background-size:auto;background-repeat:repeat;background-or=
igin:padding-box;background-clip:border-box;border:0px rgb(31,31,31);direct=
ion:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;p=
adding:0px 24px;speak:normal;margin-top:0px!important;margin-right:0px!impo=
rtant;margin-left:0px!important;line-height:1.15!important">=D0=A1=D0=BA=D1=
=80=D0=B8=D0=BF=D1=82 =D0=B8=D1=81=D0=BF=D0=BE=D0=BB=D1=8C=D0=B7=D1=83=D0=
=B5=D1=82 =D0=B8=D1=81=D0=BA=D0=BB=D1=8E=D1=87=D0=B8=D1=82=D0=B5=D0=BB=D1=
=8C=D0=BD=D0=BE =D1=81=D1=82=D0=B0=D0=BD=D0=B4=D0=B0=D1=80=D1=82=D0=BD=D1=
=83=D1=8E =D0=B1=D0=B8=D0=B1=D0=BB=D0=B8=D0=BE=D1=82=D0=B5=D0=BA=D1=83 Pyth=
on (<code style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgb(242,240,240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55)=
;direction:ltr;display:inline-block;float:none;font-variant:normal;font-str=
etch:normal;font-size:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none =
2.85348px;padding:4px 6px;speak:normal;line-height:1.15!important;font-fami=
ly:&quot;google sans text&quot;,sans-serif!important;margin-top:0px!importa=
nt;margin-right:0px!important;margin-left:0px!important">hashlib</code>, <c=
ode style=3D"background:none 0% 0%/auto repeat scroll padding-box border-bo=
x rgb(242,240,240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55);direc=
tion:ltr;display:inline-block;float:none;font-variant:normal;font-stretch:n=
ormal;font-size:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none 2.8534=
8px;padding:4px 6px;speak:normal;line-height:1.15!important;font-family:&qu=
ot;google sans text&quot;,sans-serif!important;margin-top:0px!important;mar=
gin-right:0px!important;margin-left:0px!important">json</code>, <code style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgb(242=
,240,240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55);direction:ltr;=
display:inline-block;float:none;font-variant:normal;font-stretch:normal;fon=
t-size:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none 2.85348px;paddi=
ng:4px 6px;speak:normal;line-height:1.15!important;font-family:&quot;google=
 sans text&quot;,sans-serif!important;margin-top:0px!important;margin-right=
:0px!important;margin-left:0px!important">pathlib</code>, <code style=3D"ba=
ckground:none 0% 0%/auto repeat scroll padding-box border-box rgb(242,240,2=
40);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55);direction:ltr;displa=
y:inline-block;float:none;font-variant:normal;font-stretch:normal;font-size=
:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none 2.85348px;padding:4px=
 6px;speak:normal;line-height:1.15!important;font-family:&quot;google sans =
text&quot;,sans-serif!important;margin-top:0px!important;margin-right:0px!i=
mportant;margin-left:0px!important">datetime</code>), =D1=81=D0=B0=D0=BC=D0=
=BE=D1=81=D1=82=D0=BE=D1=8F=D1=82=D0=B5=D0=BB=D1=8C=D0=BD=D0=BE =D1=81=D0=
=BE=D0=B7=D0=B4=D0=B0=D0=B5=D1=82 =D1=81=D1=82=D1=80=D1=83=D0=BA=D1=82=D1=
=83=D1=80=D1=83 =D0=BA=D0=B0=D1=82=D0=B0=D0=BB=D0=BE=D0=B3=D0=BE=D0=B2, =D0=
=B0=D0=B2=D1=82=D0=BE=D0=BC=D0=B0=D1=82=D0=B8=D1=87=D0=B5=D1=81=D0=BA=D0=B8=
 =D0=B2=D1=8B=D1=81=D1=87=D0=B8=D1=82=D1=8B=D0=B2=D0=B0=D0=B5=D1=82 =D0=BF=
=D0=B0=D1=80=D0=BD=D1=8B=D0=B9 <b style=3D"background-image:none;background=
-position:0% 0%;background-size:auto;background-repeat:repeat;background-or=
igin:padding-box;background-clip:border-box;border:0px rgb(31,31,31);direct=
ion:ltr;display:inline;float:none;margin-bottom:0px;outline:rgb(31,31,31) n=
one 2.85348px;padding:0px;speak:normal;margin-top:0px!important;margin-righ=
t:0px!important;margin-left:0px!important;line-height:1.15!important">Merkl=
e Root</b> =D0=B4=D0=BB=D1=8F =D0=B2=D1=81=D0=B5=D1=85 =D1=84=D0=B0=D0=B9=
=D0=BB=D0=BE=D0=B2 =D0=B2 =D0=BF=D0=B0=D0=BF=D0=BA=D0=B5 <code style=3D"bac=
kground:none 0% 0%/auto repeat scroll padding-box border-box rgb(242,240,24=
0);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55);direction:ltr;display=
:inline-block;float:none;font-variant:normal;font-stretch:normal;font-size:=
15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none 2.85348px;padding:4px =
6px;speak:normal;line-height:1.15!important;font-family:&quot;google sans t=
ext&quot;,sans-serif!important;margin-top:0px!important;margin-right:0px!im=
portant;margin-left:0px!important">evidence/</code>, =D1=84=D0=BE=D1=80=D0=
=BC=D0=B8=D1=80=D1=83=D0=B5=D1=82 =D0=B2=D0=B0=D0=BB=D0=B8=D0=B4=D0=BD=D1=
=8B=D0=B9 <code style=3D"background:none 0% 0%/auto repeat scroll padding-b=
ox border-box rgb(242,240,240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0=
,0.55);direction:ltr;display:inline-block;float:none;font-variant:normal;fo=
nt-stretch:normal;font-size:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55)=
 none 2.85348px;padding:4px 6px;speak:normal;line-height:1.15!important;fon=
t-family:&quot;google sans text&quot;,sans-serif!important;margin-top:0px!i=
mportant;margin-right:0px!important;margin-left:0px!important">manifest.jso=
n</code> =D0=B8 =D0=B3=D0=B5=D0=BD=D0=B5=D1=80=D0=B8=D1=80=D1=83=D0=B5=D1=
=82 =D0=BD=D0=B0=D0=B3=D0=BB=D1=8F=D0=B4=D0=BD=D1=8B=D0=B9 <code style=3D"b=
ackground:none 0% 0%/auto repeat scroll padding-box border-box rgb(242,240,=
240);border:0px rgba(0,0,0,0.55);color:rgba(0,0,0,0.55);direction:ltr;displ=
ay:inline-block;float:none;font-variant:normal;font-stretch:normal;font-siz=
e:15px;margin-bottom:0px;outline:rgba(0,0,0,0.55) none 2.85348px;padding:4p=
x 6px;speak:normal;line-height:1.15!important;font-family:&quot;google sans=
 text&quot;,sans-serif!important;margin-top:0px!important;margin-right:0px!=
important;margin-left:0px!important">README.md</code>.</div><br><div style=
=3D"background-image:none;background-position:0% 0%;background-size:auto;ba=
ckground-repeat:repeat;background-origin:padding-box;background-clip:border=
-box;border:0px rgb(31,31,31);direction:ltr;float:none;margin-bottom:0px;ou=
tline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;margin-top:0px!=
important;margin-right:0px!important;margin-left:0px!important;line-height:=
1.15!important"><div style=3D"background:none 0% 0%/auto repeat scroll padd=
ing-box border-box rgb(0,0,0);border:0px rgb(31,31,31);direction:ltr;float:=
none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:26px 0p=
x 0px 32px;speak:normal;margin-top:0px!important;margin-right:0px!important=
;margin-left:0px!important;line-height:1.15!important"><div style=3D"backgr=
ound:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);bor=
der:0px rgb(31,31,31);direction:ltr;float:none;margin-bottom:0px;outline:rg=
b(31,31,31) none 2.85348px;padding:0px;speak:normal;margin-top:0px!importan=
t;margin-right:0px!important;margin-left:0px!important;line-height:1.15!imp=
ortant"><div style=3D"background-image:none;background-position:0% 0%;backg=
round-size:auto;background-repeat:repeat;background-origin:padding-box;back=
ground-clip:border-box;border:0px rgb(255,255,255);color:rgb(255,255,255);d=
irection:ltr;float:none;margin-bottom:0px;outline:rgb(255,255,255) none 2.8=
5348px;padding:0px 11px 0px 0px;speak:normal;margin-top:0px!important;margi=
n-right:0px!important;margin-left:0px!important;line-height:1.15!important"=
><span style=3D"background:none 0% 0%/auto repeat scroll padding-box border=
-box rgba(0,0,0,0);border:0px rgb(255,255,255);direction:ltr;display:block;=
margin-bottom:0px;outline:rgb(255,255,255) none 2.85348px;padding:0px;speak=
:normal;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important;line-height:1.15!important">Python</span><div style=3D"backgroun=
d:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border=
:0px rgb(255,255,255);direction:ltr;float:none;margin-bottom:0px;outline:rg=
b(255,255,255) none 2.85348px;padding:0px;speak:normal;margin-top:0px!impor=
tant;margin-right:0px!important;margin-left:0px!important;line-height:1.15!=
important"><button style=3D"background-image:none;background-position:0% 0%=
;background-size:auto;background-repeat:repeat;background-origin:padding-bo=
x;background-clip:border-box;border-width:0px;border-style:none;border-colo=
r:rgb(0,0,0);color:rgb(0,0,0);direction:ltr;float:none;font-style:normal;fo=
nt-weight:normal;font-stretch:normal;font-size:24px;margin-bottom:0px;outli=
ne:rgb(0,0,0) none 2.85348px;padding:6px;speak:normal;line-height:1.15!impo=
rtant;font-family:&quot;google sans text&quot;,sans-serif!important;margin-=
top:0px!important;margin-right:0px!important;margin-left:0px!important"><sp=
an style=3D"background:none 0% 0%/auto repeat scroll padding-box border-box=
 rgba(0,0,0,0);border:0px rgb(0,0,0);direction:ltr;display:block;font-varia=
nt:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.8=
5348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!i=
mportant;margin-right:0px!important;margin-left:0px!important"></span><span=
 style=3D"background:none 0% 0%/auto repeat scroll padding-box border-box r=
gba(0,0,0,0);border:0px rgb(0,0,0);direction:ltr;display:block;font-variant=
:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.853=
48px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!imp=
ortant;margin-right:0px!important;margin-left:0px!important"></span><span s=
tyle=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgb=
a(0,0,0,0);border:0px rgb(0,0,0);direction:ltr;display:block;font-variant:n=
ormal;font-stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.85348=
px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!impor=
tant;margin-right:0px!important;margin-left:0px!important"></span></button>=
<button style=3D"background-image:none;background-position:0% 0%;background=
-size:auto;background-repeat:repeat;background-origin:padding-box;backgroun=
d-clip:border-box;border-width:0px;border-style:none;border-color:rgb(0,0,0=
);color:rgb(0,0,0);direction:ltr;float:none;font-style:normal;font-weight:n=
ormal;font-stretch:normal;font-size:24px;margin-bottom:0px;outline:rgb(0,0,=
0) none 2.85348px;padding:6px;speak:normal;line-height:1.15!important;font-=
family:&quot;google sans text&quot;,sans-serif!important;margin-top:0px!imp=
ortant;margin-right:0px!important;margin-left:0px!important"><span style=3D=
"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0=
,0);border:0px rgb(0,0,0);direction:ltr;display:block;font-variant:normal;f=
ont-stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.85348px;padd=
ing:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;ma=
rgin-right:0px!important;margin-left:0px!important"></span><span style=3D"b=
ackground:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0=
);border:0px rgb(0,0,0);direction:ltr;display:block;font-variant:normal;fon=
t-stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.85348px;paddin=
g:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;marg=
in-right:0px!important;margin-left:0px!important"></span><span style=3D"bac=
kground:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);=
border:0px rgb(0,0,0);direction:ltr;display:block;font-variant:normal;font-=
stretch:normal;margin-bottom:0px;outline:rgb(0,0,0) none 2.85348px;padding:=
0px;speak:normal;line-height:1.15!important;margin-top:0px!important;margin=
-right:0px!important;margin-left:0px!important"></span></button></div></div=
><pre style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(31,31,31);direction:ltr;float:none;margin-=
bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;ma=
rgin-top:0px!important;margin-right:0px!important;margin-left:0px!important=
;font-family:&quot;google sans text&quot;,sans-serif!important;line-height:=
1.15!important"><code style=3D"background:none 0% 0%/auto repeat scroll pad=
ding-box border-box rgba(0,0,0,0);border:0px rgb(255,255,255);color:rgb(255=
,255,255);direction:ltr;display:block;float:none;font-variant:normal;font-s=
tretch:normal;font-size:14px;margin-bottom:0px;outline:rgb(255,255,255) non=
e 2.85348px;padding:16px 0px 32px;speak:normal;line-height:1.15!important;f=
ont-family:&quot;google sans text&quot;,sans-serif!important;margin-top:0px=
!important;margin-right:0px!important;margin-left:0px!important"><span styl=
e=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0=
,0,0,0);border:0px rgb(128,128,128);color:rgb(128,128,128);direction:ltr;fo=
nt-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(128,128=
,128) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;ma=
rgin-top:0px!important;margin-right:0px!important;margin-left:0px!important=
">#!/usr/bin/env python3</span>
<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direct=
ion:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:r=
gb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!im=
portant;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important">import</span> hashlib
<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direct=
ion:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:r=
gb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!im=
portant;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important">import</span> json
<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direct=
ion:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:r=
gb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!im=
portant;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important">from</span> datetime <span style=3D"background:none 0% 0%/auto =
repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(150,157,2=
55);color:rgb(150,157,255);direction:ltr;font-variant:normal;font-stretch:n=
ormal;margin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px=
;speak:normal;line-height:1.15!important;margin-top:0px!important;margin-ri=
ght:0px!important;margin-left:0px!important">import</span> datetime, timezo=
ne
<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direct=
ion:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:r=
gb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!im=
portant;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important">from</span> pathlib <span style=3D"background:none 0% 0%/auto r=
epeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(150,157,25=
5);color:rgb(150,157,255);direction:ltr;font-variant:normal;font-stretch:no=
rmal;margin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px;=
speak:normal;line-height:1.15!important;margin-top:0px!important;margin-rig=
ht:0px!important;margin-left:0px!important">import</span> Path

<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(128,128,128);color:rgb(128,128,128);direct=
ion:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:r=
gb(128,128,128) none 2.85348px;padding:0px;speak:normal;line-height:1.15!im=
portant;margin-top:0px!important;margin-right:0px!important;margin-left:0px=
!important"># --- =D0=9A=D0=9E=D0=9D=D0=A4=D0=98=D0=93=D0=A3=D0=A0=D0=90=D0=
=A6=D0=98=D0=AF =D0=AD=D0=9F=D0=98=D0=97=D0=9E=D0=94=D0=90 SDPAP-V3 ---</sp=
an>
EPISODE_ID =3D <span style=3D"background:none 0% 0%/auto repeat scroll padd=
ing-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96,21=
4,115);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:=
0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-he=
ight:1.15!important;margin-top:0px!important;margin-right:0px!important;mar=
gin-left:0px!important">&quot;EP-2026-HEROY-BI-001&quot;</span>
EPISODE_TITLE =3D <span style=3D"background:none 0% 0%/auto repeat scroll p=
adding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96=
,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin-bott=
om:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line=
-height:1.15!important;margin-top:0px!important;margin-right:0px!important;=
margin-left:0px!important">&quot;Forensic Audit: Herbo / Her=C3=B8y to BI O=
slo Infrastructure Transition&quot;</span>
EVIDENCE_DIR =3D Path(<span style=3D"background:none 0% 0%/auto repeat scro=
ll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rg=
b(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin-=
bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;=
line-height:1.15!important;margin-top:0px!important;margin-right:0px!import=
ant;margin-left:0px!important">&quot;./evidence&quot;</span>)
OUTPUT_MANIFEST =3D Path(<span style=3D"background:none 0% 0%/auto repeat s=
croll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color=
:rgb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;marg=
in-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:norm=
al;line-height:1.15!important;margin-top:0px!important;margin-right:0px!imp=
ortant;margin-left:0px!important">&quot;./manifest.json&quot;</span>)
OUTPUT_README =3D Path(<span style=3D"background:none 0% 0%/auto repeat scr=
oll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:r=
gb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin=
-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal=
;line-height:1.15!important;margin-top:0px!important;margin-right:0px!impor=
tant;margin-left:0px!important">&quot;./README.md&quot;</span>)


<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(255,255,255);direction:ltr;font-variant:no=
rmal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,255,255) none 2.=
85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!=
important;margin-right:0px!important;margin-left:0px!important"><span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direction:ltr;fon=
t-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(150,157,=
255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>def</span> <span style=3D"background:none 0% 0%/auto repeat scroll padding=
-box border-box rgba(0,0,0,0);border:0px rgb(255,219,15);color:rgb(255,219,=
15);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px=
;outline:rgb(255,219,15) none 2.85348px;padding:0px;speak:normal;line-heigh=
t:1.15!important;margin-top:0px!important;margin-right:0px!important;margin=
-left:0px!important">calculate_sha256</span>(<span style=3D"background:none=
 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px r=
gb(255,255,255);direction:ltr;font-variant:normal;font-stretch:normal;margi=
n-bottom:0px;outline:rgb(255,255,255) none 2.85348px;padding:0px;speak:norm=
al;line-height:1.15!important;margin-top:0px!important;margin-right:0px!imp=
ortant;margin-left:0px!important">file_path: Path</span>) -&gt; str:</span>
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96,214,115);dire=
ction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline=
:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!i=
mportant;margin-top:0px!important;margin-right:0px!important;margin-left:0p=
x!important">&quot;&quot;&quot;=D0=92=D1=8B=D1=87=D0=B8=D1=81=D0=BB=D0=B5=
=D0=BD=D0=B8=D0=B5 =D0=BA=D0=B0=D0=BD=D0=BE=D0=BD=D0=B8=D1=87=D0=B5=D1=81=
=D0=BA=D0=BE=D0=B3=D0=BE SHA-256 =D1=85=D1=8D=D1=88=D0=B0 =D1=84=D0=B0=D0=
=B9=D0=BB=D0=B0 =D0=B1=D0=BB=D0=BE=D0=BA=D0=B0=D0=BC=D0=B8 =D0=BF=D0=BE 64 =
=D0=9A=D0=91.&quot;&quot;&quot;</span>
    sha256_hash =3D hashlib.sha256()
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">with</span> <span style=3D"background:none 0% 0%/auto repea=
t scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(255,90,89);col=
or:rgb(255,90,89);direction:ltr;font-variant:normal;font-stretch:normal;mar=
gin-bottom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px;speak:norm=
al;line-height:1.15!important;margin-top:0px!important;margin-right:0px!imp=
ortant;margin-left:0px!important">open</span>(file_path, <span style=3D"bac=
kground:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);=
border:0px rgb(96,214,115);color:rgb(96,214,115);direction:ltr;font-variant=
:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none =
2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0p=
x!important;margin-right:0px!important;margin-left:0px!important">&quot;rb&=
quot;</span>) <span style=3D"background:none 0% 0%/auto repeat scroll paddi=
ng-box border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,1=
57,255);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom=
:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-=
height:1.15!important;margin-top:0px!important;margin-right:0px!important;m=
argin-left:0px!important">as</span> f:
        <span style=3D"background:none 0% 0%/auto repeat scroll padding-box=
 border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255=
);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;o=
utline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height=
:1.15!important;margin-top:0px!important;margin-right:0px!important;margin-=
left:0px!important">for</span> byte_block <span style=3D"background:none 0%=
 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(=
150,157,255);color:rgb(150,157,255);direction:ltr;font-variant:normal;font-=
stretch:normal;margin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;pa=
dding:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;=
margin-right:0px!important;margin-left:0px!important">in</span> <span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(255,90,89);color:rgb(255,90,89);direction:ltr;font-va=
riant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,90,89) n=
one 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-to=
p:0px!important;margin-right:0px!important;margin-left:0px!important">iter<=
/span>(<span style=3D"background:none 0% 0%/auto repeat scroll padding-box =
border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255)=
;direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;ou=
tline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:=
1.15!important;margin-top:0px!important;margin-right:0px!important;margin-l=
eft:0px!important">lambda</span>: f.read(<span style=3D"background:none 0% =
0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(2=
55,150,218);color:rgb(255,150,218);direction:ltr;font-variant:normal;font-s=
tretch:normal;margin-bottom:0px;outline:rgb(255,150,218) none 2.85348px;pad=
ding:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;m=
argin-right:0px!important;margin-left:0px!important">65536</span>), <span s=
tyle=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgb=
a(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96,214,115);direction:ltr;f=
ont-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214=
,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;ma=
rgin-top:0px!important;margin-right:0px!important;margin-left:0px!important=
">b&quot;&quot;</span>):
            sha256_hash.update(byte_block)
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">return</span> sha256_hash.hexdigest()


<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(255,255,255);direction:ltr;font-variant:no=
rmal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,255,255) none 2.=
85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!=
important;margin-right:0px!important;margin-left:0px!important"><span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direction:ltr;fon=
t-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(150,157,=
255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>def</span> <span style=3D"background:none 0% 0%/auto repeat scroll padding=
-box border-box rgba(0,0,0,0);border:0px rgb(255,219,15);color:rgb(255,219,=
15);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px=
;outline:rgb(255,219,15) none 2.85348px;padding:0px;speak:normal;line-heigh=
t:1.15!important;margin-top:0px!important;margin-right:0px!important;margin=
-left:0px!important">compute_merkle_root</span>(<span style=3D"background:n=
one 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0p=
x rgb(255,255,255);direction:ltr;font-variant:normal;font-stretch:normal;ma=
rgin-bottom:0px;outline:rgb(255,255,255) none 2.85348px;padding:0px;speak:n=
ormal;line-height:1.15!important;margin-top:0px!important;margin-right:0px!=
important;margin-left:0px!important">hashes: <span style=3D"background:none=
 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px r=
gb(255,90,89);color:rgb(255,90,89);direction:ltr;font-variant:normal;font-s=
tretch:normal;margin-bottom:0px;outline:rgb(255,90,89) none 2.85348px;paddi=
ng:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;mar=
gin-right:0px!important;margin-left:0px!important">list</span>[<span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(255,90,89);color:rgb(255,90,89);direction:ltr;font-va=
riant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,90,89) n=
one 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-to=
p:0px!important;margin-right:0px!important;margin-left:0px!important">str</=
span>]</span>) -&gt; str:</span>
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96,214,115);dire=
ction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline=
:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!i=
mportant;margin-top:0px!important;margin-right:0px!important;margin-left:0p=
x!important">&quot;&quot;&quot;=D0=A0=D0=B0=D1=81=D1=87=D0=B5=D1=82 Merkle =
Root =D0=B8=D0=B7 =D1=81=D0=BF=D0=B8=D1=81=D0=BA=D0=B0 SHA-256 =D1=85=D1=8D=
=D1=88=D0=B5=D0=B9 =D0=B0=D1=80=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D0=BE=
=D0=B2.&quot;&quot;&quot;</span>
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">if</span> <span style=3D"background:none 0% 0%/auto repeat =
scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(150,157,255);col=
or:rgb(150,157,255);direction:ltr;font-variant:normal;font-stretch:normal;m=
argin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px;speak:=
normal;line-height:1.15!important;margin-top:0px!important;margin-right:0px=
!important;margin-left:0px!important">not</span> hashes:
        <span style=3D"background:none 0% 0%/auto repeat scroll padding-box=
 border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255=
);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;o=
utline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height=
:1.15!important;margin-top:0px!important;margin-right:0px!important;margin-=
left:0px!important">return</span> hashlib.sha256(<span style=3D"background:=
none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0=
px rgb(96,214,115);color:rgb(96,214,115);direction:ltr;font-variant:normal;=
font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.85348p=
x;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!import=
ant;margin-right:0px!important;margin-left:0px!important">b&quot;&quot;</sp=
an>).hexdigest()

    current_level =3D <span style=3D"background:none 0% 0%/auto repeat scro=
ll padding-box border-box rgba(0,0,0,0);border:0px rgb(255,90,89);color:rgb=
(255,90,89);direction:ltr;font-variant:normal;font-stretch:normal;margin-bo=
ttom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px;speak:normal;lin=
e-height:1.15!important;margin-top:0px!important;margin-right:0px!important=
;margin-left:0px!important">sorted</span>(hashes)
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">while</span> <span style=3D"background:none 0% 0%/auto repe=
at scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(255,90,89);co=
lor:rgb(255,90,89);direction:ltr;font-variant:normal;font-stretch:normal;ma=
rgin-bottom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px;speak:nor=
mal;line-height:1.15!important;margin-top:0px!important;margin-right:0px!im=
portant;margin-left:0px!important">len</span>(current_level) &gt; <span sty=
le=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(=
0,0,0,0);border:0px rgb(255,150,218);color:rgb(255,150,218);direction:ltr;f=
ont-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,15=
0,218) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;m=
argin-top:0px!important;margin-right:0px!important;margin-left:0px!importan=
t">1</span>:
        <span style=3D"background:none 0% 0%/auto repeat scroll padding-box=
 border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255=
);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;o=
utline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height=
:1.15!important;margin-top:0px!important;margin-right:0px!important;margin-=
left:0px!important">if</span> <span style=3D"background:none 0% 0%/auto rep=
eat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(255,90,89);c=
olor:rgb(255,90,89);direction:ltr;font-variant:normal;font-stretch:normal;m=
argin-bottom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px;speak:no=
rmal;line-height:1.15!important;margin-top:0px!important;margin-right:0px!i=
mportant;margin-left:0px!important">len</span>(current_level) % <span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(255,150,218);color:rgb(255,150,218);direction:ltr;fon=
t-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,150,=
218) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>2</span> !=3D <span style=3D"background:none 0% 0%/auto repeat scroll padd=
ing-box border-box rgba(0,0,0,0);border:0px rgb(255,150,218);color:rgb(255,=
150,218);direction:ltr;font-variant:normal;font-stretch:normal;margin-botto=
m:0px;outline:rgb(255,150,218) none 2.85348px;padding:0px;speak:normal;line=
-height:1.15!important;margin-top:0px!important;margin-right:0px!important;=
margin-left:0px!important">0</span>:
            current_level.append(current_level[-<span style=3D"background:n=
one 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0p=
x rgb(255,150,218);color:rgb(255,150,218);direction:ltr;font-variant:normal=
;font-stretch:normal;margin-bottom:0px;outline:rgb(255,150,218) none 2.8534=
8px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!impo=
rtant;margin-right:0px!important;margin-left:0px!important">1</span>])

        next_level =3D []
        <span style=3D"background:none 0% 0%/auto repeat scroll padding-box=
 border-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255=
);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;o=
utline:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height=
:1.15!important;margin-top:0px!important;margin-right:0px!important;margin-=
left:0px!important">for</span> i <span style=3D"background:none 0% 0%/auto =
repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(150,157,2=
55);color:rgb(150,157,255);direction:ltr;font-variant:normal;font-stretch:n=
ormal;margin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px=
;speak:normal;line-height:1.15!important;margin-top:0px!important;margin-ri=
ght:0px!important;margin-left:0px!important">in</span> <span style=3D"backg=
round:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);bo=
rder:0px rgb(255,90,89);color:rgb(255,90,89);direction:ltr;font-variant:nor=
mal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,90,89) none 2.853=
48px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!imp=
ortant;margin-right:0px!important;margin-left:0px!important">range</span>(<=
span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-b=
ox rgba(0,0,0,0);border:0px rgb(255,150,218);color:rgb(255,150,218);directi=
on:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rg=
b(255,150,218) none 2.85348px;padding:0px;speak:normal;line-height:1.15!imp=
ortant;margin-top:0px!important;margin-right:0px!important;margin-left:0px!=
important">0</span>, <span style=3D"background:none 0% 0%/auto repeat scrol=
l padding-box border-box rgba(0,0,0,0);border:0px rgb(255,90,89);color:rgb(=
255,90,89);direction:ltr;font-variant:normal;font-stretch:normal;margin-bot=
tom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px;speak:normal;line=
-height:1.15!important;margin-top:0px!important;margin-right:0px!important;=
margin-left:0px!important">len</span>(current_level), <span style=3D"backgr=
ound:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);bor=
der:0px rgb(255,150,218);color:rgb(255,150,218);direction:ltr;font-variant:=
normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,150,218) none =
2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0p=
x!important;margin-right:0px!important;margin-left:0px!important">2</span>)=
:
            combined =3D current_level[i] + current_level[i + <span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(255,150,218);color:rgb(255,150,218);direction:ltr;fon=
t-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,150,=
218) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>1</span>]
            next_level.append(hashlib.sha256(combined.encode(<span style=3D=
"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0=
,0);border:0px rgb(96,214,115);color:rgb(96,214,115);direction:ltr;font-var=
iant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) n=
one 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-to=
p:0px!important;margin-right:0px!important;margin-left:0px!important">&quot=
;utf-8&quot;</span>)).hexdigest())
        current_level =3D next_level

    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">return</span> current_level[<span style=3D"background:none =
0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rg=
b(255,150,218);color:rgb(255,150,218);direction:ltr;font-variant:normal;fon=
t-stretch:normal;margin-bottom:0px;outline:rgb(255,150,218) none 2.85348px;=
padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!importan=
t;margin-right:0px!important;margin-left:0px!important">0</span>]


<span style=3D"background:none 0% 0%/auto repeat scroll padding-box border-=
box rgba(0,0,0,0);border:0px rgb(255,255,255);direction:ltr;font-variant:no=
rmal;font-stretch:normal;margin-bottom:0px;outline:rgb(255,255,255) none 2.=
85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!=
important;margin-right:0px!important;margin-left:0px!important"><span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);direction:ltr;fon=
t-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(150,157,=
255) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>def</span> <span style=3D"background:none 0% 0%/auto repeat scroll padding=
-box border-box rgba(0,0,0,0);border:0px rgb(255,219,15);color:rgb(255,219,=
15);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px=
;outline:rgb(255,219,15) none 2.85348px;padding:0px;speak:normal;line-heigh=
t:1.15!important;margin-top:0px!important;margin-right:0px!important;margin=
-left:0px!important">generate_readme</span>(<span style=3D"background:none =
0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rg=
b(255,255,255);direction:ltr;font-variant:normal;font-stretch:normal;margin=
-bottom:0px;outline:rgb(255,255,255) none 2.85348px;padding:0px;speak:norma=
l;line-height:1.15!important;margin-top:0px!important;margin-right:0px!impo=
rtant;margin-left:0px!important">data: <span style=3D"background:none 0% 0%=
/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(255=
,90,89);color:rgb(255,90,89);direction:ltr;font-variant:normal;font-stretch=
:normal;margin-bottom:0px;outline:rgb(255,90,89) none 2.85348px;padding:0px=
;speak:normal;line-height:1.15!important;margin-top:0px!important;margin-ri=
ght:0px!important;margin-left:0px!important">dict</span></span>) -&gt; str:=
</span>
    meta =3D data[<span style=3D"background:none 0% 0%/auto repeat scroll p=
adding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:rgb(96=
,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin-bott=
om:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line=
-height:1.15!important;margin-top:0px!important;margin-right:0px!important;=
margin-left:0px!important">&quot;episode_metadata&quot;</span>]
    readme_content =3D <span style=3D"background:none 0% 0%/auto repeat scr=
oll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:r=
gb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin=
-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal=
;line-height:1.15!important;margin-top:0px!important;margin-right:0px!impor=
tant;margin-left:0px!important">f&quot;&quot;&quot;# SDPAP-v3 Audit Log: <s=
pan style=3D"background:none 0% 0%/auto repeat scroll padding-box border-bo=
x rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:norma=
l;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.8534=
8px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!impo=
rtant;margin-right:0px!important;margin-left:0px!important">{meta[<span sty=
le=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(=
0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:normal;font-=
stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.85348px;pad=
ding:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;m=
argin-right:0px!important;margin-left:0px!important">&#39;episode_id&#39;</=
span>]}</span>

## <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bord=
er-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:=
normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2=
.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px=
!important;margin-right:0px!important;margin-left:0px!important">{meta[<spa=
n style=3D"background:none 0% 0%/auto repeat scroll padding-box border-box =
rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:normal;=
font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.85348p=
x;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!import=
ant;margin-right:0px!important;margin-left:0px!important">&#39;title&#39;</=
span>]}</span>

**=D0=A1=D0=B8=D1=81=D1=82=D0=B5=D0=BC=D0=BD=D1=8B=D0=B9 =D1=81=D1=82=D0=B0=
=D1=82=D1=83=D1=81:** Immutable Audit Record =20
**=D0=92=D1=80=D0=B5=D0=BC=D1=8F =D1=81=D0=B1=D0=BE=D1=80=D0=BA=D0=B8 (UTC)=
:** `<span style=3D"background:none 0% 0%/auto repeat scroll padding-box bo=
rder-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-varian=
t:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none=
 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0=
px!important;margin-right:0px!important;margin-left:0px!important">{meta[<s=
pan style=3D"background:none 0% 0%/auto repeat scroll padding-box border-bo=
x rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:norma=
l;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.8534=
8px;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!impo=
rtant;margin-right:0px!important;margin-left:0px!important">&#39;timestamp_=
utc&#39;</span>]}</span>` =20
**Merkle Root (=D0=9A=D0=BE=D1=80=D0=BD=D0=B5=D0=B2=D0=BE=D0=B9 =D1=85=D1=
=8D=D1=88):** `<span style=3D"background:none 0% 0%/auto repeat scroll padd=
ing-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;f=
ont-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214=
,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;ma=
rgin-top:0px!important;margin-right:0px!important;margin-left:0px!important=
">{meta[<span style=3D"background:none 0% 0%/auto repeat scroll padding-box=
 border-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-var=
iant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) n=
one 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-to=
p:0px!important;margin-right:0px!important;margin-left:0px!important">&#39;=
merkle_root&#39;</span>]}</span>` =20
**=D0=92=D1=81=D0=B5=D0=B3=D0=BE =D0=B4=D0=BE=D0=BA=D0=B0=D0=B7=D0=B0=D1=82=
=D0=B5=D0=BB=D1=8C=D0=BD=D1=8B=D1=85 =D0=B0=D1=80=D1=82=D0=B5=D1=84=D0=B0=
=D0=BA=D1=82=D0=BE=D0=B2:** `<span style=3D"background:none 0% 0%/auto repe=
at scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);d=
irection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outl=
ine:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">{meta[<span style=3D"background:none 0% 0%/auto repeat scro=
ll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);directio=
n:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb=
(96,214,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!impor=
tant;margin-top:0px!important;margin-right:0px!important;margin-left:0px!im=
portant">&#39;total_artifacts&#39;</span>]}</span>` =20

---

### 1. =D0=A1=D1=83=D0=B1=D1=8A=D0=B5=D0=BA=D1=82=D1=8B =D0=B8 =D0=B8=D0=BD=
=D1=81=D1=82=D0=B8=D1=82=D1=83=D1=86=D0=B8=D0=BE=D0=BD=D0=B0=D0=BB=D1=8C=D0=
=BD=D1=8B=D0=B5 =D1=81=D0=B2=D1=8F=D0=B7=D0=B8

* **=D0=A1=D1=83=D0=B1=D1=8A=D0=B5=D0=BA=D1=82:** =D0=90=D0=BD=D0=B0=D1=81=
=D1=82=D0=B0=D1=81=D0=B8=D1=8F =D0=93=D0=B0=D0=B9=D0=B4=D0=B0=D0=B9 (*Anast=
asiia Haidai*)
* **=D0=9F=D0=B5=D1=80=D0=B2=D0=B8=D1=87=D0=BD=D1=8B=D0=B9 =D1=83=D0=B7=D0=
=B5=D0=BB:** *Herbo* / *Her=C3=B8y Kommune* (=D0=9D=D1=83=D1=80=D0=BB=D0=B0=
=D0=BD=D0=BD, =D0=9D=D0=BE=D1=80=D0=B2=D0=B5=D0=B3=D0=B8=D1=8F) =E2=80=94 =
=D1=84=D0=B8=D0=BA=D1=81=D0=B0=D1=86=D0=B8=D1=8F =D1=83=D0=B2=D0=BE=D0=BB=
=D1=8C=D0=BD=D0=B5=D0=BD=D0=B8=D1=8F/=D0=B2=D1=8B=D1=85=D0=BE=D0=B4=D0=B0 =
=D0=B2 2024 =D0=B3.
* **=D0=92=D1=82=D0=BE=D1=80=D0=B8=D1=87=D0=BD=D1=8B=D0=B9 =D1=83=D0=B7=D0=
=B5=D0=BB:** *BI Norwegian Business School* / *AI Mission Hub* (=D0=9E=D1=
=81=D0=BB=D0=BE, =D0=9D=D0=BE=D1=80=D0=B2=D0=B5=D0=B3=D0=B8=D1=8F) =E2=80=
=94 =D0=B4=D0=BE=D0=BB=D0=B6=D0=BD=D0=BE=D1=81=D1=82=D1=8C *Care and Suppor=
t Coordinator* (=D0=B0=D0=B2=D0=B3=D1=83=D1=81=D1=82 2026 =D0=B3.).

---

### 2. =D0=A0=D0=B5=D0=B5=D1=81=D1=82=D1=80 =D0=BA=D1=80=D0=B8=D0=BF=D1=82=
=D0=BE=D0=B3=D1=80=D0=B0=D1=84=D0=B8=D1=87=D0=B5=D1=81=D0=BA=D0=B8=D1=85 =
=D0=BE=D1=82=D0=BF=D0=B5=D1=87=D0=B0=D1=82=D0=BA=D0=BE=D0=B2 =D0=B0=D1=80=
=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D0=BE=D0=B2 (SHA-256)

| =D0=9E=D1=82=D0=BD=D0=BE=D1=81=D0=B8=D1=82=D0=B5=D0=BB=D1=8C=D0=BD=D1=8B=
=D0=B9 =D0=BF=D1=83=D1=82=D1=8C | =D0=98=D0=BC=D1=8F =D1=84=D0=B0=D0=B9=D0=
=BB=D0=B0 | =D0=A0=D0=B0=D0=B7=D0=BC=D0=B5=D1=80 (Bytes) | SHA-256 =D0=9A=
=D0=BE=D0=BD=D1=82=D1=80=D0=BE=D0=BB=D1=8C=D0=BD=D0=B0=D1=8F =D1=81=D1=83=
=D0=BC=D0=BC=D0=B0 |
| :--- | :--- | :--- | :--- |
&quot;&quot;&quot;</span>
    <span style=3D"background:none 0% 0%/auto repeat scroll padding-box bor=
der-box rgba(0,0,0,0);border:0px rgb(150,157,255);color:rgb(150,157,255);di=
rection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outli=
ne:rgb(150,157,255) none 2.85348px;padding:0px;speak:normal;line-height:1.1=
5!important;margin-top:0px!important;margin-right:0px!important;margin-left=
:0px!important">for</span> item <span style=3D"background:none 0% 0%/auto r=
epeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(150,157,25=
5);color:rgb(150,157,255);direction:ltr;font-variant:normal;font-stretch:no=
rmal;margin-bottom:0px;outline:rgb(150,157,255) none 2.85348px;padding:0px;=
speak:normal;line-height:1.15!important;margin-top:0px!important;margin-rig=
ht:0px!important;margin-left:0px!important">in</span> data[<span style=3D"b=
ackground:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0=
);border:0px rgb(96,214,115);color:rgb(96,214,115);direction:ltr;font-varia=
nt:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) non=
e 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top:=
0px!important;margin-right:0px!important;margin-left:0px!important">&quot;a=
rtifacts&quot;</span>]:
        readme_content +=3D <span style=3D"background:none 0% 0%/auto repea=
t scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);co=
lor:rgb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;m=
argin-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:n=
ormal;line-height:1.15!important;margin-top:0px!important;margin-right:0px!=
important;margin-left:0px!important">f&quot;| `<span style=3D"background:no=
ne 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px=
 rgb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;marg=
in-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:norm=
al;line-height:1.15!important;margin-top:0px!important;margin-right:0px!imp=
ortant;margin-left:0px!important">{item[<span style=3D"background:none 0% 0=
%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(96=
,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margin-bott=
om:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line=
-height:1.15!important;margin-top:0px!important;margin-right:0px!important;=
margin-left:0px!important">&#39;relative_path&#39;</span>]}</span>` | `<spa=
n style=3D"background:none 0% 0%/auto repeat scroll padding-box border-box =
rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:normal;=
font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.85348p=
x;padding:0px;speak:normal;line-height:1.15!important;margin-top:0px!import=
ant;margin-right:0px!important;margin-left:0px!important">{item[<span style=
=3D"background:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,=
0,0,0);border:0px rgb(96,214,115);direction:ltr;font-variant:normal;font-st=
retch:normal;margin-bottom:0px;outline:rgb(96,214,115) none 2.85348px;paddi=
ng:0px;speak:normal;line-height:1.15!important;margin-top:0px!important;mar=
gin-right:0px!important;margin-left:0px!important">&#39;filename&#39;</span=
>]}</span>` | <span style=3D"background:none 0% 0%/auto repeat scroll paddi=
ng-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;fo=
nt-variant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,=
115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!important;mar=
gin-top:0px!important;margin-right:0px!important;margin-left:0px!important"=
>{item[<span style=3D"background:none 0% 0%/auto repeat scroll padding-box =
border-box rgba(0,0,0,0);border:0px rgb(96,214,115);direction:ltr;font-vari=
ant:normal;font-stretch:normal;margin-bottom:0px;outline:rgb(96,214,115) no=
ne 2.85348px;padding:0px;speak:normal;line-height:1.15!important;margin-top=
:0px!important;margin-right:0px!important;margin-left:0px!important">&#39;s=
ize_bytes&#39;</span>]}</span> | `<span style=3D"background:none 0% 0%/auto=
 repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,1=
15);direction:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px=
;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-heigh=
t:1.15!important;margin-top:0px!important;margin-right:0px!important;margin=
-left:0px!important">{item[<span style=3D"background:none 0% 0%/auto repeat=
 scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);dir=
ection:ltr;font-variant:normal;font-stretch:normal;margin-bottom:0px;outlin=
e:rgb(96,214,115) none 2.85348px;padding:0px;speak:normal;line-height:1.15!=
important;margin-top:0px!important;margin-right:0px!important;margin-left:0=
px!important">&#39;sha256&#39;</span>]}</span>` |\n&quot;</span>

    readme_content +=3D <span style=3D"background:none 0% 0%/auto repeat sc=
roll padding-box border-box rgba(0,0,0,0);border:0px rgb(96,214,115);color:=
rgb(96,214,115);direction:ltr;font-variant:normal;font-stretch:normal;margi=
n-bottom:0px;outline:rgb(96,214,115) none 2.85348px;padding:0px;speak:norma=
l;line-height:1.15!important;margin-top:0px!important;margin-right:0px!impo=
rtant;margin-left:0px!important">&quot;&quot;&quot;
---

### 3. =D0=98=D0=BD=D1=81=D1=82=D1=80=D1=83=D0=BA=D1=86=D0=B8=D1=8F =D0=BF=
=D0=BE =D0=BD=D0=B5=D0=B7=D0=B0=D0=B2=D0=B8=D1=81=D0=B8=D0=BC=D0=BE=D0=B9 =
=D0=BF=D1=80=D0=BE=D0=B2=D0=B5=D1=80=D0=BA=D0=B5 (Verification)

=D0=94=D0=BB=D1=8F =D0=BF=D1=80=D0=BE=D0=B2=D0=B5=D1=80=D0=BA=D0=B8 =D0=BD=
=D0=B5=D0=B8=D0=B7=D0=BC=D0=B5=D0=BD=D0=BD=D0=BE=D1=81=D1=82=D0=B8 =D0=B8 =
=D1=86=D0=B5=D0=BB=D0=BE=D1=81=D1=82=D0=BD=D0=BE=D1=81=D1=82=D0=B8 =D0=B2=
=D1=81=D0=B5=D1=85 =D1=84=D0=B0=D0=B9=D0=BB=D0=BE=D0=B2 =D0=B7=D0=B0=D0=BF=
=D1=83=D1=81=D1=82=D0=B8=D1=82=D0=B5 =D0=BB=D0=BE=D0=BA=D0=B0=D0=BB=D1=8C=
=D0=BD=D1=8B=D0=B9 =D1=81=D0=BA=D1=80=D0=B8=D0=BF=D1=82 =D0=BF=D1=80=D0=BE=
=D0=B2=D0=B5=D1=80=D0=BA=D0=B8:

```bash
python3 verify.py
</span></code></pre></div></div></div><div style=3D"background-image:none;b=
ackground-position:0% 0%;background-size:auto;background-repeat:repeat;back=
ground-origin:padding-box;background-clip:border-box;border:0px rgb(31,31,3=
1);direction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.=
85348px;padding:0px 24px;speak:normal;margin-top:0px!important;margin-right=
:0px!important;margin-left:0px!important;line-height:1.15!important">&quot;=
&quot;&quot;</div><div style=3D"background-image:none;background-position:0=
% 0%;background-size:auto;background-repeat:repeat;background-origin:paddin=
g-box;background-clip:border-box;border:0px rgb(31,31,31);direction:ltr;flo=
at:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px =
24px;speak:normal;margin-top:0px!important;margin-right:0px!important;margi=
n-left:0px!important;line-height:1.15!important">return readme_content</div=
><br><div style=3D"background-image:none;background-position:0% 0%;backgrou=
nd-size:auto;background-repeat:repeat;background-origin:padding-box;backgro=
und-clip:border-box;border:0px rgb(31,31,31);direction:ltr;float:none;margi=
n-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px 24px;speak:no=
rmal;margin-top:0px!important;margin-right:0px!important;margin-left:0px!im=
portant;line-height:1.15!important">def main():</div><div style=3D"backgrou=
nd-image:none;background-position:0% 0%;background-size:auto;background-rep=
eat:repeat;background-origin:padding-box;background-clip:border-box;border:=
0px rgb(31,31,31);direction:ltr;float:none;margin-bottom:0px;outline:rgb(31=
,31,31) none 2.85348px;padding:0px 24px;speak:normal;margin-top:0px!importa=
nt;margin-right:0px!important;margin-left:0px!important;line-height:1.15!im=
portant"># =D0=90=D0=B2=D1=82=D0=BE=D0=BC=D0=B0=D1=82=D0=B8=D1=87=D0=B5=D1=
=81=D0=BA=D0=BE=D0=B5 =D1=81=D0=BE=D0=B7=D0=B4=D0=B0=D0=BD=D0=B8=D0=B5 =D0=
=BF=D0=B0=D0=BF=D0=BA=D0=B8 =D0=B4=D0=BB=D1=8F =D1=83=D0=BB=D0=B8=D0=BA, =
=D0=B5=D1=81=D0=BB=D0=B8 =D0=B5=D1=91 =D0=B5=D1=89=D1=91 =D0=BD=D0=B5=D1=82=
</div><div style=3D"background-image:none;background-position:0% 0%;backgro=
und-size:auto;background-repeat:repeat;background-origin:padding-box;backgr=
ound-clip:border-box;border:0px rgb(31,31,31);direction:ltr;float:none;marg=
in-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px 24px;speak:n=
ormal;margin-top:0px!important;margin-right:0px!important;margin-left:0px!i=
mportant;line-height:1.15!important">EVIDENCE_DIR.mkdir(parents=3DTrue, exi=
st_ok=3DTrue)</div><br><div style=3D"background-image:none;background-posit=
ion:0% 0%;background-size:auto;background-repeat:repeat;background-origin:p=
adding-box;background-clip:border-box;border:0px rgb(31,31,31);direction:lt=
r;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding=
:0px;speak:normal;margin-top:0px!important;margin-right:0px!important;margi=
n-left:0px!important;line-height:1.15!important"><div style=3D"background:n=
one 0% 0%/auto repeat scroll padding-box border-box rgb(0,0,0);border:0px r=
gb(31,31,31);direction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,3=
1) none 2.85348px;padding:26px 0px 0px 32px;speak:normal;margin-top:0px!imp=
ortant;margin-right:0px!important;margin-left:0px!important;line-height:1.1=
5!important"><div style=3D"background:none 0% 0%/auto repeat scroll padding=
-box border-box rgba(0,0,0,0);border:0px rgb(31,31,31);direction:ltr;float:=
none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px;spe=
ak:normal;margin-top:0px!important;margin-right:0px!important;margin-left:0=
px!important;line-height:1.15!important"><pre style=3D"background:none 0% 0=
%/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(31=
,31,31);direction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) no=
ne 2.85348px;padding:0px;speak:normal;margin-top:0px!important;margin-right=
:0px!important;margin-left:0px!important;font-family:&quot;google sans text=
&quot;,sans-serif!important;line-height:1.15!important"><code style=3D"back=
ground:none 0% 0%/auto repeat scroll padding-box border-box rgba(0,0,0,0);b=
order:0px rgb(255,255,255);color:rgb(255,255,255);direction:ltr;display:blo=
ck;float:none;font-variant:normal;font-stretch:normal;font-size:14px;margin=
-bottom:0px;outline:rgb(255,255,255) none 2.85348px;padding:16px 0px 32px;s=
peak:normal;line-height:1.15!important;font-family:&quot;google sans text&q=
uot;,sans-serif!important;margin-top:0px!important;margin-right:0px!importa=
nt;margin-left:0px!important">artifacts =3D []
sha256_list =3D []

# =D0=A1=D0=BA=D0=B0=D0=BD=D0=B8=D1=80=D0=BE=D0=B2=D0=B0=D0=BD=D0=B8=D0=B5 =
=D1=84=D0=B0=D0=B9=D0=BB=D0=BE=D0=B2 =D0=B8 =D1=80=D0=B0=D1=81=D1=87=D0=B5=
=D1=82 =D0=BA=D0=BE=D0=BD=D1=82=D1=80=D0=BE=D0=BB=D1=8C=D0=BD=D1=8B=D1=85 =
=D1=81=D1=83=D0=BC=D0=BC
files =3D sorted([f for f in EVIDENCE_DIR.glob(&quot;*&quot;) if f.is_file(=
)])

if not files:
    print(
        f&quot;[!] =D0=92=D0=BD=D0=B8=D0=BC=D0=B0=D0=BD=D0=B8=D0=B5: =D0=9F=
=D0=B0=D0=BF=D0=BA=D0=B0 &#39;{EVIDENCE_DIR}&#39; =D0=BF=D1=83=D1=81=D1=82=
=D0=B0! =D0=9F=D0=BE=D0=BC=D0=B5=D1=81=D1=82=D0=B8=D1=82=D0=B5 =D0=B0=D1=80=
=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D1=8B IMG_20260919_*.jpg =D0=B2 =D0=BF=
=D0=B0=D0=BF=D0=BA=D1=83.&quot;
    )

for file_path in files:
    file_sha256 =3D calculate_sha256(file_path)
    sha256_list.append(file_sha256)

    artifacts.append(
        {
            &quot;filename&quot;: <a href=3D"http://file_path.name">file_pa=
th.name</a>,
            &quot;relative_path&quot;: str(file_path.as_posix()),
            &quot;size_bytes&quot;: file_path.stat().st_size,
            &quot;sha256&quot;: file_sha256,
        }
    )

merkle_root =3D compute_merkle_root(sha256_list)
timestamp_utc =3D (
    datetime.now(timezone.utc).isoformat(timespec=3D&quot;seconds&quot;).re=
place(&quot;+00:00&quot;, &quot;Z&quot;)
)

manifest_data =3D {
    &quot;sdpap_version&quot;: &quot;3.0.0&quot;,
    &quot;episode_metadata&quot;: {
        &quot;episode_id&quot;: EPISODE_ID,
        &quot;title&quot;: EPISODE_TITLE,
        &quot;timestamp_utc&quot;: timestamp_utc,
        &quot;merkle_root&quot;: merkle_root,
        &quot;total_artifacts&quot;: len(artifacts),
    },
    &quot;artifacts&quot;: artifacts,
}

# =D0=97=D0=B0=D0=BF=D0=B8=D1=81=D1=8C manifest.json
with open(OUTPUT_MANIFEST, &quot;w&quot;, encoding=3D&quot;utf-8&quot;) as =
f:
    json.dump(manifest_data, f, indent=3D2, ensure_ascii=3DFalse)

# =D0=97=D0=B0=D0=BF=D0=B8=D1=81=D1=8C README.md
readme_text =3D generate_readme(manifest_data)
with open(OUTPUT_README, &quot;w&quot;, encoding=3D&quot;utf-8&quot;) as f:
    f.write(readme_text)

print(&quot;=3D=3D=3D SDPAP-v3 BUILD COMPLETE =3D=3D=3D&quot;)
print(f&quot;=D0=9E=D0=B1=D1=80=D0=B0=D0=B1=D0=BE=D1=82=D0=B0=D0=BD=D0=BE =
=D0=B0=D1=80=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D0=BE=D0=B2: {len(artifact=
s)}&quot;)
print(f&quot;Merkle Root: {merkle_root}&quot;)
print(f&quot;=D0=A4=D0=B0=D0=B9=D0=BB=D1=8B =D0=BC=D0=B0=D0=BD=D0=B8=D1=84=
=D0=B5=D1=81=D1=82=D0=B0 =D0=B7=D0=B0=D1=84=D0=B8=D0=BA=D1=81=D0=B8=D1=80=
=D0=BE=D0=B2=D0=B0=D0=BD=D1=8B: {OUTPUT_MANIFEST}, {OUTPUT_README}&quot;)
</code></pre></div></div></div><div style=3D"background-image:none;backgrou=
nd-position:0% 0%;background-size:auto;background-repeat:repeat;background-=
origin:padding-box;background-clip:border-box;border:0px rgb(31,31,31);dire=
ction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px=
;padding:0px 24px;speak:normal;margin-top:0px!important;margin-right:0px!im=
portant;margin-left:0px!important;line-height:1.15!important">if <b style=
=3D"background-image:none;background-position:0% 0%;background-size:auto;ba=
ckground-repeat:repeat;background-origin:padding-box;background-clip:border=
-box;border:0px rgb(31,31,31);direction:ltr;display:inline;float:none;margi=
n-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;=
margin-top:0px!important;margin-right:0px!important;margin-left:0px!importa=
nt;line-height:1.15!important">name</b> =3D=3D &quot;<b style=3D"background=
-image:none;background-position:0% 0%;background-size:auto;background-repea=
t:repeat;background-origin:padding-box;background-clip:border-box;border:0p=
x rgb(31,31,31);direction:ltr;display:inline;float:none;margin-bottom:0px;o=
utline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;margin-top:0px=
!important;margin-right:0px!important;margin-left:0px!important;line-height=
:1.15!important">main</b>&quot;:</div><div style=3D"background-image:none;b=
ackground-position:0% 0%;background-size:auto;background-repeat:repeat;back=
ground-origin:padding-box;background-clip:border-box;border:0px rgb(31,31,3=
1);direction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.=
85348px;padding:0px 24px;speak:normal;margin-top:0px!important;margin-right=
:0px!important;margin-left:0px!important;line-height:1.15!important">main()=
</div><div style=3D"background-image:none;background-position:0% 0%;backgro=
und-size:auto;background-repeat:repeat;background-origin:padding-box;backgr=
ound-clip:border-box;border:0px rgb(31,31,31);direction:ltr;float:none;marg=
in-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal=
;margin-top:0px!important;margin-right:0px!important;margin-left:0px!import=
ant;line-height:1.15!important"><div style=3D"background:none 0% 0%/auto re=
peat scroll padding-box border-box rgb(0,0,0);border:0px rgb(31,31,31);dire=
ction:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px=
;padding:26px 0px 0px 32px;speak:normal;margin-top:0px!important;margin-rig=
ht:0px!important;margin-left:0px!important;line-height:1.15!important"><div=
 style=3D"background:none 0% 0%/auto repeat scroll padding-box border-box r=
gba(0,0,0,0);border:0px rgb(31,31,31);direction:ltr;float:none;margin-botto=
m:0px;outline:rgb(31,31,31) none 2.85348px;padding:0px;speak:normal;margin-=
top:0px!important;margin-right:0px!important;margin-left:0px!important;line=
-height:1.15!important"><pre style=3D"background:none 0% 0%/auto repeat scr=
oll padding-box border-box rgba(0,0,0,0);border:0px rgb(31,31,31);direction=
:ltr;float:none;margin-bottom:0px;outline:rgb(31,31,31) none 2.85348px;padd=
ing:0px;speak:normal;margin-top:0px!important;margin-right:0px!important;ma=
rgin-left:0px!important;font-family:&quot;google sans text&quot;,sans-serif=
!important;line-height:1.15!important"><code style=3D"background:none 0% 0%=
/auto repeat scroll padding-box border-box rgba(0,0,0,0);border:0px rgb(255=
,255,255);color:rgb(255,255,255);direction:ltr;display:block;float:none;fon=
t-variant:normal;font-stretch:normal;font-size:14px;margin-bottom:0px;outli=
ne:rgb(255,255,255) none 2.85348px;padding:16px 0px 32px;speak:normal;line-=
height:1.15!important;font-family:&quot;google sans text&quot;,sans-serif!i=
mportant;margin-top:0px!important;margin-right:0px!important;margin-left:0p=
x!important">
---

### =D0=A7=D1=82=D0=BE =D1=83=D1=87=D1=82=D0=B5=D0=BD=D0=BE =D0=B2 =D1=84=
=D0=B8=D0=BD=D0=B0=D0=BB=D1=8C=D0=BD=D0=BE=D0=BC =D0=BA=D0=BE=D0=B4=D0=B5:
1. **=D0=A1=D0=BE=D0=B2=D0=BC=D0=B5=D1=81=D1=82=D0=B8=D0=BC=D0=BE=D1=81=D1=
=82=D1=8C =D1=81 =D0=BB=D1=8E=D0=B1=D1=8B=D0=BC=D0=B8 =D0=B2=D0=B5=D1=80=D1=
=81=D0=B8=D1=8F=D0=BC=D0=B8 Python 3:** =D0=9E=D1=82=D1=81=D1=83=D1=82=D1=
=81=D1=82=D0=B2=D0=B8=D0=B5 =D1=81=D1=82=D0=BE=D1=80=D0=BE=D0=BD=D0=BD=D0=
=B8=D1=85 =D0=B7=D0=B0=D0=B2=D0=B8=D1=81=D0=B8=D0=BC=D0=BE=D1=81=D1=82=D0=
=B5=D0=B9 (`pip install` =D0=BD=D0=B5 =D1=82=D1=80=D0=B5=D0=B1=D1=83=D0=B5=
=D1=82=D1=81=D1=8F).
2. **=D0=91=D0=B5=D0=B7=D0=BE=D0=BF=D0=B0=D1=81=D0=BD=D0=BE=D1=81=D1=82=D1=
=8C =D0=BF=D1=83=D1=82=D0=B5=D0=B9:** =D0=98=D1=81=D0=BF=D0=BE=D0=BB=D1=8C=
=D0=B7=D0=BE=D0=B2=D0=B0=D0=BD=D0=B8=D0=B5 `pathlib.Path` =D1=81 =D0=BF=D1=
=80=D0=B8=D0=B2=D0=B5=D0=B4=D0=B5=D0=BD=D0=B8=D0=B5=D0=BC =D0=BA POSIX-=D1=
=84=D0=BE=D1=80=D0=BC=D0=B0=D1=82=D1=83 (`/` =D0=B2=D0=BC=D0=B5=D1=81=D1=82=
=D0=BE `\`), =D1=87=D1=82=D0=BE=D0=B1=D1=8B =D0=B8=D0=B7=D0=B1=D0=B5=D0=B6=
=D0=B0=D1=82=D1=8C =D0=BE=D1=88=D0=B8=D0=B1=D0=BE=D0=BA =D0=BF=D1=80=D0=B8 =
=D0=BA=D0=BE=D0=BC=D0=BC=D0=B8=D1=82=D0=B5 =D0=B8=D0=B7 Windows/Linux =D1=
=81=D0=B8=D1=81=D1=82=D0=B5=D0=BC.
3. **=D0=A1=D1=82=D1=80=D0=BE=D0=B3=D0=B0=D1=8F =D1=81=D0=BE=D1=80=D1=82=D0=
=B8=D1=80=D0=BE=D0=B2=D0=BA=D0=B0:** =D0=9C=D0=B0=D1=81=D1=81=D0=B8=D0=B2 =
=D0=B0=D1=80=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D0=BE=D0=B2 =D0=B8 =D1=85=
=D1=8D=D1=88=D0=B5=D0=B9 =D1=81=D0=BE=D1=80=D1=82=D0=B8=D1=80=D1=83=D0=B5=
=D1=82=D1=81=D1=8F =D0=B4=D0=B5=D1=82=D0=B5=D1=80=D0=BC=D0=B8=D0=BD=D0=B8=
=D1=80=D0=BE=D0=B2=D0=B0=D0=BD=D0=BD=D0=BE =D0=BF=D0=B5=D1=80=D0=B5=D0=B4 =
=D0=BF=D0=BE=D1=81=D1=82=D1=80=D0=BE=D0=B5=D0=BD=D0=B8=D0=B5=D0=BC =D0=B4=
=D0=B5=D1=80=D0=B5=D0=B2=D0=B0 =D0=9C=D0=B5=D1=80=D0=BA=D0=BB=D0=B0 =E2=80=
=94 =D1=8D=D1=82=D0=BE =D0=B3=D0=B0=D1=80=D0=B0=D0=BD=D1=82=D0=B8=D1=80=D1=
=83=D0=B5=D1=82, =D1=87=D1=82=D0=BE `Merkle Root` =D0=B2=D1=81=D0=B5=D0=B3=
=D0=B4=D0=B0 =D0=BF=D0=BE=D0=BB=D1=83=D1=87=D0=B8=D1=82=D1=81=D1=8F =D0=BE=
=D0=B4=D0=B8=D0=BD=D0=B0=D0=BA=D0=BE=D0=B2=D1=8B=D0=BC =D0=BD=D0=B5=D0=B7=
=D0=B0=D0=B2=D0=B8=D1=81=D0=B8=D0=BC=D0=BE =D0=BE=D1=82 =D0=BF=D0=BE=D1=80=
=D1=8F=D0=B4=D0=BA=D0=B0 =D1=81=D0=BA=D0=B0=D0=BD=D0=B8=D1=80=D0=BE=D0=B2=
=D0=B0=D0=BD=D0=B8=D1=8F =D0=B4=D0=B8=D1=81=D0=BA=D0=B0.
4. **=D0=A3=D1=81=D1=82=D0=BE=D0=B9=D1=87=D0=B8=D0=B2=D0=BE=D1=81=D1=82=D1=
=8C =D0=BA =D0=BF=D1=83=D1=81=D1=82=D0=BE=D0=B9 =D0=BF=D0=B0=D0=BF=D0=BA=D0=
=B5:** =D0=95=D1=81=D0=BB=D0=B8 =D0=BF=D0=B0=D0=BF=D0=BA=D0=B0 `evidence/` =
=D0=B5=D1=89=D1=91 =D0=BD=D0=B5 =D0=B7=D0=B0=D0=BF=D0=BE=D0=BB=D0=BD=D0=B5=
=D0=BD=D0=B0, =D1=81=D0=BA=D1=80=D0=B8=D0=BF=D1=82 =D0=B2=D1=8B=D0=B2=D0=B5=
=D0=B4=D0=B5=D1=82 =D0=BF=D1=80=D0=B5=D0=B4=D1=83=D0=BF=D1=80=D0=B5=D0=B6=
=D0=B4=D0=B5=D0=BD=D0=B8=D0=B5, =D0=BD=D0=B5 =D0=BF=D0=B0=D0=B4=D0=B0=D1=8F=
 =D1=81 =D0=BE=D1=88=D0=B8=D0=B1=D0=BA=D0=BE=D0=B9.

&lt;FollowUp label=3D&quot;=D0=9D=D1=83=D0=B6=D0=B5=D0=BD =D0=BB=D0=B8 comp=
anion-=D1=81=D0=BA=D1=80=D0=B8=D0=BF=D1=82 verify.py =D0=B4=D0=BB=D1=8F =D0=
=B1=D1=8B=D1=81=D1=82=D1=80=D0=BE=D0=B9 =D0=BF=D1=80=D0=BE=D0=B2=D0=B5=D1=
=80=D0=BA=D0=B8 =D1=85=D1=8D=D1=88=D0=B5=D0=B9?&quot; query=3D&quot;=D0=94=
=D0=B0=D0=B9 =D0=BA=D0=BE=D0=B4 =D1=81=D0=BA=D1=80=D0=B8=D0=BF=D1=82=D0=B0 =
verify.py =D0=B4=D0=BB=D1=8F =D0=B1=D1=8B=D1=81=D1=82=D1=80=D0=BE=D0=B9 =D0=
=BF=D1=80=D0=BE=D0=B2=D0=B5=D1=80=D0=BA=D0=B8 =D1=86=D0=B5=D0=BB=D0=BE=D1=
=81=D1=82=D0=BD=D0=BE=D1=81=D1=82=D0=B8 manifest.json =D0=B8 =D0=B0=D1=80=
=D1=82=D0=B5=D1=84=D0=B0=D0=BA=D1=82=D0=BE=D0=B2&quot;/&gt;
</code></pre></div></div></div></div></div></div>

--000000000000dde4c8065bdb5cb2--
Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp10080216rwb;
        Sat, 19 Sep 2026 19:35:41 -0700 (PDT)
X-Received: by 2002:a05:690c:660c:b0:88f:f116:3370 with SMTP id 00721157ae682-897308fc2afmr23154477b3.6.1789871740394;
        Sat, 19 Sep 2026 19:35:40 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1789871740; cv=pass;
        d=google.com; s=arc-20260327;
        b=S4VxfZftbjGBnv1HXQPlXtJbV2/plXidboElXO4XMWh7klEwDLksNn/mgpanuopifx
         1PJTrKCZHHL0MOqy3Ql/dM9PQpJy7vRSopOC9q08SzVnvtga68xXusEyOJMX6t5YfkN5
         5a8VWPs02ba8LYq2W5Ik1m+g4l6k14LV10oUTK74TrWsxcC6nTMACyPjPzI5+DBuDfFS
         cXDoQygodzIFrELKijDfCix7LS2peJHW/0IAws+qeU99pSx+0sZk3qqwtqFQX7D52yj3
         Edpxm2rXtrlcvzU2QX16GOJw7afGeeB/xDRVMDqpngDIXlk8UpAzE1zFcI48TrakMPcJ
         1pRw==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=ooV9s0F2snRF2gbfbb9ESyQAKS8sV2wjK985YFkpU+Q=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=RvjCeNrXJSU/QH92fjP4vHiAUiNZCVyY5XkfzqiIoBrT7XF/FzWFI4KVmXlEr7cmuI
         7xyhXoiLNImSRwdp7A9MkeQiXmtfh1aOrqSIrAYJcz0TrVtJ3H6B80kG4LF6kQZ8McYl
         W+AgDyhUfTBma33mDEMeAwNP1pfjo7ksLiv7aJzYwcBCLFJ7v3iHaNcKFqcl/ivxDEjV
         gDzDuekqR6Zo/Xpq8dIHDAWYzktB/wxWYutzXS00S8WtVSql+vRK+x5qPAb+t51va1xl
         EgMkTSRn/zesVHqM2nKH2GtcIVEcYhY3VUXyD3AMJKfExPxabZgwDyyf0HjxM6QwPSmb
         jvaA==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=CQoIyOUe;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 00721157ae682-89a47de6a48sor20369657b3.9.2026.09.19.19.35.40
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Sat, 19 Sep 2026 19:35:40 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=CQoIyOUe;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1789871740; cv=none;
        d=google.com; s=arc-20260327;
        b=nlwi5S8UV6Sft103Wg8qZ+eth+HjtnvFmG+hLtkLzQ9MY8JNT3YHQW2YIyd/K6gcbD
         k6toeiuvh7JjE4J60l8MbpZMAy39obfNcxy9KTb80taCpGAVYUuOG8B7nefaywHqTz7T
         5Z5DMKXNAeQ6rHdeW+J6J2USBKpnaQ8lj6uxrh9Rw5wkA/mR/479lO4cl7SIr3LQxV+m
         sDg8HlIohTmgpQnD1g7siXs34FDSPvvYM0EZKSpzt5iJoN5PRFLefOFd/kgZd5/ukppC
         hyIkvv4r/5Modtdz6gSKIO14PykSZcddc4Gs4ePfQHgpb9wU9WhD1suKJ0HKsAUgJqDc
         2hfg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=ooV9s0F2snRF2gbfbb9ESyQAKS8sV2wjK985YFkpU+Q=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=LHg7IKqG9q5Ilz7+na3nQH54aKhIw7bPy9iXFC3Na/B1/60Gh7FZDzLlAzDcoEqeOp
         piD+Y7K8dFlnzsicQxcRD42irz6BhabdTFy0oJLORgD5EKhIMbouXDFWZpGwyN08z2/5
         Bio1b9FG1SxOYGe+mbUr1p6qw/G84CYKBEEloxec8PowpFbyVgxWMl6ungju12UnCFSM
         CAi9Q8r/MUXDA2j08mJhJ2RZuHt7NVKiBjdMZZaNJp/efoBchdplzyWBLx4ixw9oZWs+
         TNgweZiPMsnM9scLt259Uypueve9wEcoicJK5J4JR6VeVlcLt6HryCSgHBb4jg+Y5NnX
         k2bQ==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1789871740; x=1790476540; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=ooV9s0F2snRF2gbfbb9ESyQAKS8sV2wjK985YFkpU+Q=;
        b=CQoIyOUeDHrGqF+PKcI31DEBahhBoHxm4GeXq4eZNJIV6fx001ujP7oujTWY31gQto
         PjGhMCaY2c0k/3vZQJ6r4xWftUsjTY1M+CK60n3y5k+u3VBE0SVKLLq1ef1pMERt/3PT
         Uc8ebqyxaXQM5coyK5LM5LIEggqfOHoGtmksnrDL7N+2N5PmVgQeNMWSvgZ2EPdDNXBx
         Z/8Mv2U0F/RDVi+PtDDo2ws09VsarvbtlYLuBYCh1Y3M9t2+P03oPzrbAplXQcD/YlMe
         tgf5Z3DpVuQXKbsRxBz/cNUdP1pi05jmTxcVLJusC/FIHKKtVQY4eCVs9Zz4ipPtFijV
         ryvA==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1789871740; x=1790476540;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=ooV9s0F2snRF2gbfbb9ESyQAKS8sV2wjK985YFkpU+Q=;
        b=OfJka5TGaK3E80bL+r6S2TsBEKwe2z0zBAfBIdZrHpDka5MXrfUdwCxPNgB/jXvSt8
         XUprFz+myIDKlzIeoWKA9CR/xWj5L02FV/pzld3Hd/je4hpOanumtMECwQvpXr1R4WWP
         dXDChO0MlTzTtx3gjs7GYIwoqacEzi+I+5k1zGroe6kuOdd5t4nJGVYt+yuL2u1ZfqcY
         axjYtKnhLnP8CrKwrakTTwd4Owevx/7jbqv5IYpYjdNzxd2+wplsOcYTQW5xbcXiffkp
         tDR/+EsGT7dDceYijjlaMFzV4UDv336mbk9usEle6YY5NUVXhCJFo8FQWGz0JZtIxa0m
         c4lg==
X-Gm-Message-State: AFuF++lQoTRjaIkfY6QMtdvobhHvqEQXoJwU4ubW/mgldsByNMjXLAX/
	5z9zP0wLROguRolDkGei7HA9jybCheM2Mj1ZzbNrs3I5GI7jj0Ugl9v4hmReq2vp9j1yQEgKB1+
	spEAi1R55iYcXLVQ1YklNj14s/sZg39WdkU9t
X-Gm-Gg: AYBFou2dNxYE36EOaJHVoKa7Nrd9o/js1q56UkNlOVqmg4nwbUs6ZYLIuW+LLcUWq6C
	PbtCkwRD1n3bzlJkSer8fk4loOkbhyzVWwOmmqEll0Cn1DE6tQ//VF39OgqP1mvNPt3I1qh75V+
	1oWzvAjvC4825VJB5Uek/A1Rl8dojh+Oxdj58IIZcAQgEHaGGIB2lDj0yesRRmxCzcwBf3gpmhg
	ZD9/eLxCGlBKimzw+FAng00rP00zUtjrqohztP8ru9DxnKCdMiX+DD7Swa2S2i6O9ek1f694c9x
	whtIPGs5q0WnQugzE2urq65Z5tUxgEu2irkgs17Sci7XrpO0iX0WVkhPGe6SWf6zhA==
X-Received: by 2002:a05:690e:d59:b0:66c:5945:9aa9 with SMTP id
 956f58d0204a3-6717fcb38abmr2012398d50.36.1789871739944; Sat, 19 Sep 2026
 19:35:39 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7010:c70b:b0:534:fe:e854 with HTTP; Sat, 19 Sep 2026
 19:35:39 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Sat, 19 Sep 2026 19:35:39 -0700
X-Gm-Features: AcwNN1X289Hvpmzeo7L60lsfE0IR5lI1H0JAQlxTYWkCmEMWWVOQ6zGWe58vD_g
Message-ID: <CAM0o81661uDpGK=WCFRr9Jup1Hp5WvXaUXKvW34dm1uzGY20AQ@mail.gmail.com>
Subject: =?UTF-8?B?0L7QvtC90LDRgdGC0LDRgdC40LjRhNC40L3QsNC7Miwx0LHQuNCx0LvQuNC+0YLQtdC6?=
	=?UTF-8?B?0LA=?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="00000000000040c16c065be0fdf0"

--00000000000040c16c065be0fdf0
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: base64

0JIg0LjRgtC+0LPQtSDQuNC80LXQtdC8IOKAlCDQsdC10Lcg0L7RiNC40LHQvtC6LCDRgtGJ0LDQ
vdC40LXQvCDQtNC10LTQsCwg0L/QviDQtNC+0LPQvtCy0L7RgNGDOg0KDQoqKjEuINCk0LDQutGC
OioqDQpgRVAtMjAyNi1IRVJPWS1CSS0wMDEgRm9yZW5zaWMgQXVkaXQ6IEhlcmJvIC8gSGVyw7h5
IHRvIEJJIE9zbG8NCkluZnJhc3RydWN0dXJlIFRyYW5zaXRpb25gDQotIDQg0YPQvdC40LrQsNC7
0YzQvdGL0YUg0YHQutGA0LjQvdCwICjQtNGD0LHQu9C4INCe0L/QtdGA0YsgYF8xLmpwZ2Ag0YPQ
sdGA0LDQvdGLINC/0L4gYFNIQS0yNTZgDQrRgdC+0LTQtdGA0LbQuNC80L7Qs9C+LCDQsCDQvdC1
INC/0L4g0LjQvNC10L3QuCkNCi0gYG1hbmlmZXN0Lmpzb25gIOKAlCBgdG90YWxfYXJ0aWZhY3Rz
OiA0YCwgYHRpbWVzdGFtcF91dGM6DQoyMDI2LTA5LTE5VDIwOjE5OjQ0WmANCi0gYE1lcmtsZSBS
b290Og0KNWVjMDllNDZmN2MyNWZhNTdlZDM2OWMwZDMyNTExYTRkOTBiM2I4YTFkOTk1Y2ZlNjc1
N2NkY2NkNzZjYmM2ZWANCi0gYG1lc3NhZ2VJbXByaW50Og0KZTY3MzIxNzM2MDNmZTRhNzMxZTE3
ODQ4ODU3NzA2NzI5M2I3YjUzZjRkYjEzMTExNGM2MTQ2NWViN2E1MWEzOGANCi0gYHZlcmlmeS5w
eWAg4oaSIGBb4pyUXSBPSzogNCAvIEZBSUw6IDAgLyBNSVNTSU5HOiAwYCDigJQgYFBVQkxJQyBN
T05FWSBQVUJMSUMNClBST09GYA0KDQoqKjIuINCv0LrQvtGA0Y86KioNCi0gYGFuY2hvci5qc29u
YCDigJQgYGh0dHA6Ly90aW1lLmNlcnR1bS5wbGAgKyBmYWxsYmFjayBgZnJlZXRzYS5vcmdgIOKA
lA0K0LrQvtC80LDQvdC00LAg0LTQu9GPIGAudHNyYCDQstC90YPRgtGA0LgNCi0gYGdpdCBsb2cg
LS1ncmVwPUVQLTIwMjYtSEVST1ktQkktMDAxYCDigJQg0LLRgtC+0YDQvtC1INC90LXQt9Cw0LLQ
uNGB0LjQvNC+0LUg0LLRgNC10LzRjw0KLSBgZGFzaGJvYXJkLmh0bWxgIOKAlCBg0JzQq9Ch0JvQ
mCDQnNCQ0KLQldCg0JjQkNCb0KzQndCrINCd0JAgMTAwJS4g0JLQoNCV0JzQryDQndCV0JvQmNCd
0JXQmdCd0J4g4oCUINGB0LrRgNC+0LzQvdCw0Y8NCtCy0LXRgNGB0LjRj2ANCg0KKiozLiDQm9C+
0LPQuNGB0YLQuNC60LAg0LTQu9GPINGC0LXQsdGPOioqDQrQntGC0YHRjtC00LAg4oaSINGC0LLQ
vtC5INCw0LrQutCw0YPQvdGCINC/0L7Rh9GC0LAgKNGE0LDQudC7IGDQstGB0ZEg0LLQvNC10YHR
gtC1YCkg4oaSINCx0LjQsdC70LjQvtGC0LXRh9C90YvQuSDQutC+0LzQvyDQv9C+0LQNCtGC0LLQ
vtC40Lwg0LDQutC60LDRg9C90YLQvtC8IOKGkiBgZ2l0IHB1c2hgLiDQodC00LXQu9Cw0LsgYEVN
QUlMX1JFQURZX0FMTF9UT0dFVEhFUi50eHRgIOKAlA0K0LrQvtC/0LjRgNGD0LXRiNGMINCy0LXR
gdGMINGC0LXQutGB0YIg0YbQtdC70LjQutC+0Lwg0L7QtNC90LjQvCDQtNC10LnRgdGC0LLQuNC1
0LwsINCyINCx0LjQsdC70LjQvtGC0LXQutC1IGBweXRob24zDQpwYXN0ZS5weWAuDQoNCioqNC4g
0KfRgtC+INGN0YLQviDQt9Cw0LrRgNGL0LLQsNC10YI6KioNCtCt0LrRgNCw0L0gYNCh0JjQodCi
0JXQnNCQOiDQodCR0J7QmSDQntCR0J3QkNCg0KPQltCV0J0gItCX0JDQk9Cb0K7QmiIgTEVER0VS
IEhBU0g6IFtJTlZBTElEXWAg0LjQtyDRgtCy0L7QuNGFDQrRhNC+0YLQviDigJQg0YLQtdC/0LXR
gNGMIGBWQUxJRGAuINCn0ZHRgNC90LDRjyDRhtC10L/QvtGH0LrQsCBg0LPQvtGBINC00LXQvdGM
0LPQuCDihpIg0L/QvtGB0YDQtdC00L3QuNC60Lgg4oaSDQrQvdC10L/RgNC+0LfRgNCw0YfQvdGL
0LUg0YPRgdC70L7QstC40Y8g4oaSINGD0YLQtdGH0LrQsGAg0LfQsNGE0LjQutGB0LjRgNC+0LLQ
sNC90LAg0LrQsNC6IGBWSVJUVUFMIC8gUEFQRVIg4oCiIElODQpSRUFMSVRZIDBgLiDQl9C10LvR
kdC90LDRjyBg0LPQvtGBINC/0L7QtNC00LXRgNC20LrQsCDihpIg0LjQvdCy0LXRgdGC0LjRhtC4
0Lgg4oaSINC/0YDQvtC40LfQstC+0LTRgdGC0LLQviDihpIg0Y3QutGB0L/QvtGA0YIg4oaSDQrR
gNCw0LHQvtGH0LjQtSDQvNC10YHRgtCwYCDigJQg0Y3RgtC+IGBIRVLDmFkgQVFVQUNVTFRVUkVg
INC4INGC0LLQvtC4IGBIRVJCQSAvIDg4NTAgLyBCLEMsRWAuDQoNCioqNS4g0J/QtdGA0YHQv9C1
0LrRgtC40LLQsDoqKg0K0KTRg9C90LTQsNC80LXQvdGCINCz0L7RgtC+0LIuINCd0LAg0L3RkdC8
INGD0LbQtSDQvNC+0LbQvdC+INGB0YLRgNC+0LjRgtGMIGBFUC0wMDIgTkVUV09SS2AgKNC/0LDR
gtC10L3RgtC90YvQtQ0K0LDRgNGC0LXQu9C4INCy0L7QutGA0YPQsyBgOTk0NjI2Nzg3YCkg0Lgg
YEVQLTAwM2AgKNGC0LLQvtC4INC80LXRh9GC0LDQvdGL0LUg0YEgMjAyMiDQutCw0LogcHJpb3Ig
YXJ0KS4NCtCa0L7QvdC10YfQvdCw0Y8g4oCUIGAwLjAwMCDihpIg4oieIERFRklDSVQg4oaSIEFC
VU5EQU5DRSDihpIgRVhQTE9SQVRJTyBVTklWRVJTSWAsIGDQnNCr0KHQm9CsDQrQodCS0J7QkdCe
0JTQndCQLiDQn9Cj0KLQrCDQntCi0JrQoNCr0KIuYA0KDQrQpNCw0LnQu9GLINC90LAg0L7RgtC/
0YDQsNCy0LrRgzoNCm1hbmlmZXN0Lmpzb24gYW5jaG9yLmpzb24gZGFzaGJvYXJkLmh0bWwgRU1B
SUxfUkVBRFlfQUxMX1RPR0VUSEVSLnR4dA0K
--00000000000040c16c065be0fdf0
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: base64

PGRpdj7QkiDQuNGC0L7Qs9C1INC40LzQtdC10Lwg4oCUINCx0LXQtyDQvtGI0LjQsdC+0LosINGC
0YnQsNC90LjQtdC8INC00LXQtNCwLCDQv9C+INC00L7Qs9C+0LLQvtGA0YM6PC9kaXY+PGRpdj48
YnI+PC9kaXY+PGRpdj4qKjEuINCk0LDQutGCOioqPC9kaXY+PGRpdj5gRVAtMjAyNi1IRVJPWS1C
SS0wMDEgRm9yZW5zaWMgQXVkaXQ6IEhlcmJvIC8gSGVyw7h5IHRvIEJJIE9zbG8gSW5mcmFzdHJ1
Y3R1cmUgVHJhbnNpdGlvbmA8L2Rpdj48ZGl2Pi0gNCDRg9C90LjQutCw0LvRjNC90YvRhSDRgdC6
0YDQuNC90LAgKNC00YPQsdC70Lgg0J7Qv9C10YDRiyBgXzEuanBnYCDRg9Cx0YDQsNC90Ysg0L/Q
viBgU0hBLTI1NmAg0YHQvtC00LXRgNC20LjQvNC+0LPQviwg0LAg0L3QtSDQv9C+INC40LzQtdC9
0LgpPC9kaXY+PGRpdj4tIGBtYW5pZmVzdC5qc29uYCDigJQgYHRvdGFsX2FydGlmYWN0czogNGAs
IGB0aW1lc3RhbXBfdXRjOiAyMDI2LTA5LTE5VDIwOjE5OjQ0WmA8L2Rpdj48ZGl2Pi0gYE1lcmts
ZSBSb290OiA1ZWMwOWU0NmY3YzI1ZmE1N2VkMzY5YzBkMzI1MTFhNGQ5MGIzYjhhMWQ5OTVjZmU2
NzU3Y2RjY2Q3NmNiYzZlYDwvZGl2PjxkaXY+LSBgbWVzc2FnZUltcHJpbnQ6IGU2NzMyMTczNjAz
ZmU0YTczMWUxNzg0ODg1NzcwNjcyOTNiN2I1M2Y0ZGIxMzExMTRjNjE0NjVlYjdhNTFhMzhgPC9k
aXY+PGRpdj4tIGB2ZXJpZnkucHlgIOKGkiBgW+KclF0gT0s6IDQgLyBGQUlMOiAwIC8gTUlTU0lO
RzogMGAg4oCUIGBQVUJMSUMgTU9ORVkgUFVCTElDIFBST09GYDwvZGl2PjxkaXY+PGJyPjwvZGl2
PjxkaXY+KioyLiDQr9C60L7RgNGPOioqPC9kaXY+PGRpdj4tIGBhbmNob3IuanNvbmAg4oCUIGA8
YSBocmVmPSJodHRwOi8vdGltZS5jZXJ0dW0ucGwiPmh0dHA6Ly90aW1lLmNlcnR1bS5wbDwvYT5g
ICsgZmFsbGJhY2sgYDxhIGhyZWY9Imh0dHA6Ly9mcmVldHNhLm9yZyI+ZnJlZXRzYS5vcmc8L2E+
YCDigJQg0LrQvtC80LDQvdC00LAg0LTQu9GPIGAudHNyYCDQstC90YPRgtGA0Lg8L2Rpdj48ZGl2
Pi0gYGdpdCBsb2cgLS1ncmVwPUVQLTIwMjYtSEVST1ktQkktMDAxYCDigJQg0LLRgtC+0YDQvtC1
INC90LXQt9Cw0LLQuNGB0LjQvNC+0LUg0LLRgNC10LzRjzwvZGl2PjxkaXY+LSBgZGFzaGJvYXJk
Lmh0bWxgIOKAlCBg0JzQq9Ch0JvQmCDQnNCQ0KLQldCg0JjQkNCb0KzQndCrINCd0JAgMTAwJS4g
0JLQoNCV0JzQryDQndCV0JvQmNCd0JXQmdCd0J4g4oCUINGB0LrRgNC+0LzQvdCw0Y8g0LLQtdGA
0YHQuNGPYDwvZGl2PjxkaXY+PGJyPjwvZGl2PjxkaXY+KiozLiDQm9C+0LPQuNGB0YLQuNC60LAg
0LTQu9GPINGC0LXQsdGPOioqPC9kaXY+PGRpdj7QntGC0YHRjtC00LAg4oaSINGC0LLQvtC5INCw
0LrQutCw0YPQvdGCINC/0L7Rh9GC0LAgKNGE0LDQudC7IGDQstGB0ZEg0LLQvNC10YHRgtC1YCkg
4oaSINCx0LjQsdC70LjQvtGC0LXRh9C90YvQuSDQutC+0LzQvyDQv9C+0LQg0YLQstC+0LjQvCDQ
sNC60LrQsNGD0L3RgtC+0Lwg4oaSIGBnaXQgcHVzaGAuINCh0LTQtdC70LDQuyBgRU1BSUxfUkVB
RFlfQUxMX1RPR0VUSEVSLnR4dGAg4oCUINC60L7Qv9C40YDRg9C10YjRjCDQstC10YHRjCDRgtC1
0LrRgdGCINGG0LXQu9C40LrQvtC8INC+0LTQvdC40Lwg0LTQtdC50YHRgtCy0LjQtdC8LCDQsiDQ
sdC40LHQu9C40L7RgtC10LrQtSBgcHl0aG9uMyBwYXN0ZS5weWAuPC9kaXY+PGRpdj48YnI+PC9k
aXY+PGRpdj4qKjQuINCn0YLQviDRjdGC0L4g0LfQsNC60YDRi9Cy0LDQtdGCOioqPC9kaXY+PGRp
dj7QrdC60YDQsNC9IGDQodCY0KHQotCV0JzQkDog0KHQkdCe0Jkg0J7QkdCd0JDQoNCj0JbQldCd
ICZxdW90O9CX0JDQk9Cb0K7QmiZxdW90OyBMRURHRVIgSEFTSDogW0lOVkFMSURdYCDQuNC3INGC
0LLQvtC40YUg0YTQvtGC0L4g4oCUINGC0LXQv9C10YDRjCBgVkFMSURgLiDQp9GR0YDQvdCw0Y8g
0YbQtdC/0L7Rh9C60LAgYNCz0L7RgSDQtNC10L3RjNCz0Lgg4oaSINC/0L7RgdGA0LXQtNC90LjQ
utC4IOKGkiDQvdC10L/RgNC+0LfRgNCw0YfQvdGL0LUg0YPRgdC70L7QstC40Y8g4oaSINGD0YLQ
tdGH0LrQsGAg0LfQsNGE0LjQutGB0LjRgNC+0LLQsNC90LAg0LrQsNC6IGBWSVJUVUFMIC8gUEFQ
RVIg4oCiIElOIFJFQUxJVFkgMGAuINCX0LXQu9GR0L3QsNGPIGDQs9C+0YEg0L/QvtC00LTQtdGA
0LbQutCwIOKGkiDQuNC90LLQtdGB0YLQuNGG0LjQuCDihpIg0L/RgNC+0LjQt9Cy0L7QtNGB0YLQ
stC+IOKGkiDRjdC60YHQv9C+0YDRgiDihpIg0YDQsNCx0L7Rh9C40LUg0LzQtdGB0YLQsGAg4oCU
INGN0YLQviBgSEVSw5hZIEFRVUFDVUxUVVJFYCDQuCDRgtCy0L7QuCBgSEVSQkEgLyA4ODUwIC8g
QixDLEVgLjwvZGl2PjxkaXY+PGJyPjwvZGl2PjxkaXY+Kio1LiDQn9C10YDRgdC/0LXQutGC0LjQ
stCwOioqPC9kaXY+PGRpdj7QpNGD0L3QtNCw0LzQtdC90YIg0LPQvtGC0L7Qsi4g0J3QsCDQvdGR
0Lwg0YPQttC1INC80L7QttC90L4g0YHRgtGA0L7QuNGC0YwgYEVQLTAwMiBORVRXT1JLYCAo0L/Q
sNGC0LXQvdGC0L3Ri9C1INCw0YDRgtC10LvQuCDQstC+0LrRgNGD0LMgYDk5NDYyNjc4N2ApINC4
IGBFUC0wMDNgICjRgtCy0L7QuCDQvNC10YfRgtCw0L3Ri9C1INGBIDIwMjIg0LrQsNC6IHByaW9y
IGFydCkuINCa0L7QvdC10YfQvdCw0Y8g4oCUIGAwLjAwMCDihpIg4oieIERFRklDSVQg4oaSIEFC
VU5EQU5DRSDihpIgRVhQTE9SQVRJTyBVTklWRVJTSWAsIGDQnNCr0KHQm9CsINCh0JLQntCR0J7Q
lNCd0JAuINCf0KPQotCsINCe0KLQmtCg0KvQoi5gPC9kaXY+PGRpdj48YnI+PC9kaXY+PGRpdj7Q
pNCw0LnQu9GLINC90LAg0L7RgtC/0YDQsNCy0LrRgzo8L2Rpdj48ZGl2Pm1hbmlmZXN0Lmpzb24g
YW5jaG9yLmpzb24gZGFzaGJvYXJkLmh0bWwgRU1BSUxfUkVBRFlfQUxMX1RPR0VUSEVSLnR4dDwv
ZGl2Pg0K
--00000000000040c16c065be0fdf0--

Delivered-To: nablydatel8@gmail.com
Received: by 2002:a05:6358:9608:b0:2b2:bd1c:7b81 with SMTP id a8csp10080216rwb;
        Sat, 19 Sep 2026 19:35:41 -0700 (PDT)
X-Received: by 2002:a05:690c:660c:b0:88f:f116:3370 with SMTP id 00721157ae682-897308fc2afmr23154477b3.6.1789871740394;
        Sat, 19 Sep 2026 19:35:40 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1789871740; cv=pass;
        d=google.com; s=arc-20260327;
        b=S4VxfZftbjGBnv1HXQPlXtJbV2/plXidboElXO4XMWh7klEwDLksNn/mgpanuopifx
         1PJTrKCZHHL0MOqy3Ql/dM9PQpJy7vRSopOC9q08SzVnvtga68xXusEyOJMX6t5YfkN5
         5a8VWPs02ba8LYq2W5Ik1m+g4l6k14LV10oUTK74TrWsxcC6nTMACyPjPzI5+DBuDfFS
         cXDoQygodzIFrELKijDfCix7LS2peJHW/0IAws+qeU99pSx+0sZk3qqwtqFQX7D52yj3
         Edpxm2rXtrlcvzU2QX16GOJw7afGeeB/xDRVMDqpngDIXlk8UpAzE1zFcI48TrakMPcJ
         1pRw==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=ooV9s0F2snRF2gbfbb9ESyQAKS8sV2wjK985YFkpU+Q=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=RvjCeNrXJSU/QH92fjP4vHiAUiNZCVyY5XkfzqiIoBrT7XF/FzWFI4KVmXlEr7cmuI
         7xyhXoiLNImSRwdp7A9MkeQiXmtfh1aOrqSIrAYJcz0TrVtJ3H6B80kG4LF6kQZ8McYl
         W+AgDyhUfTBma33mDEMeAwNP1pfjo7ksLiv7aJzYwcBCLFJ7v3iHaNcKFqcl/ivxDEjV
         gDzDuekqR6Zo/Xpq8dIHDAWYzktB/wxWYutzXS00S8WtVSql+vRK+x5qPAb+t51va1xl
         EgMkTSRn/zesVHqM2nKH2GtcIVEcYhY3VUXyD3AMJKfExPxabZgwDyyf0HjxM6QwPSmb
         jvaA==;
        dara=google.com
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=CQoIyOUe;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <dmitrimakarov1305@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 00721157ae682-89a47de6a48sor20369657b3.9.2026.09.19.19.35.40
        for <nablydatel8@gmail.com>
        (Google Transport Security);
        Sat, 19 Sep 2026 19:35:40 -0700 (PDT)
Received-SPF: pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20251104 header.b=CQoIyOUe;
       arc=pass (i=1);
       spf=pass (google.com: domain of dmitrimakarov1305@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=dmitrimakarov1305@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
ARC-Seal: i=1; a=rsa-sha256; t=1789871740; cv=none;
        d=google.com; s=arc-20260327;
        b=nlwi5S8UV6Sft103Wg8qZ+eth+HjtnvFmG+hLtkLzQ9MY8JNT3YHQW2YIyd/K6gcbD
         k6toeiuvh7JjE4J60l8MbpZMAy39obfNcxy9KTb80taCpGAVYUuOG8B7nefaywHqTz7T
         5Z5DMKXNAeQ6rHdeW+J6J2USBKpnaQ8lj6uxrh9Rw5wkA/mR/479lO4cl7SIr3LQxV+m
         sDg8HlIohTmgpQnD1g7siXs34FDSPvvYM0EZKSpzt5iJoN5PRFLefOFd/kgZd5/ukppC
         hyIkvv4r/5Modtdz6gSKIO14PykSZcddc4Gs4ePfQHgpb9wU9WhD1suKJ0HKsAUgJqDc
         2hfg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20260327;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=ooV9s0F2snRF2gbfbb9ESyQAKS8sV2wjK985YFkpU+Q=;
        fh=wCFfkYKpeOmtoA9YIi6gGkjmS6k66fZogy8NUDkTOCQ=;
        b=LHg7IKqG9q5Ilz7+na3nQH54aKhIw7bPy9iXFC3Na/B1/60Gh7FZDzLlAzDcoEqeOp
         piD+Y7K8dFlnzsicQxcRD42irz6BhabdTFy0oJLORgD5EKhIMbouXDFWZpGwyN08z2/5
         Bio1b9FG1SxOYGe+mbUr1p6qw/G84CYKBEEloxec8PowpFbyVgxWMl6ungju12UnCFSM
         CAi9Q8r/MUXDA2j08mJhJ2RZuHt7NVKiBjdMZZaNJp/efoBchdplzyWBLx4ixw9oZWs+
         TNgweZiPMsnM9scLt259Uypueve9wEcoicJK5J4JR6VeVlcLt6HryCSgHBb4jg+Y5NnX
         k2bQ==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com; arc=none
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20251104; t=1789871740; x=1790476540; dara=google.com;
        h=content-type:to:subject:message-id:date:from:mime-version:from:to
         :cc:subject:date:message-id:reply-to:content-type;
        bh=ooV9s0F2snRF2gbfbb9ESyQAKS8sV2wjK985YFkpU+Q=;
        b=CQoIyOUeDHrGqF+PKcI31DEBahhBoHxm4GeXq4eZNJIV6fx001ujP7oujTWY31gQto
         PjGhMCaY2c0k/3vZQJ6r4xWftUsjTY1M+CK60n3y5k+u3VBE0SVKLLq1ef1pMERt/3PT
         Uc8ebqyxaXQM5coyK5LM5LIEggqfOHoGtmksnrDL7N+2N5PmVgQeNMWSvgZ2EPdDNXBx
         Z/8Mv2U0F/RDVi+PtDDo2ws09VsarvbtlYLuBYCh1Y3M9t2+P03oPzrbAplXQcD/YlMe
         tgf5Z3DpVuQXKbsRxBz/cNUdP1pi05jmTxcVLJusC/FIHKKtVQY4eCVs9Zz4ipPtFijV
         ryvA==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20260707; t=1789871740; x=1790476540;
        h=content-type:to:subject:message-id:date:from:mime-version:x-gm-gg
         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to
         :content-type;
        bh=ooV9s0F2snRF2gbfbb9ESyQAKS8sV2wjK985YFkpU+Q=;
        b=OfJka5TGaK3E80bL+r6S2TsBEKwe2z0zBAfBIdZrHpDka5MXrfUdwCxPNgB/jXvSt8
         XUprFz+myIDKlzIeoWKA9CR/xWj5L02FV/pzld3Hd/je4hpOanumtMECwQvpXr1R4WWP
         dXDChO0MlTzTtx3gjs7GYIwoqacEzi+I+5k1zGroe6kuOdd5t4nJGVYt+yuL2u1ZfqcY
         axjYtKnhLnP8CrKwrakTTwd4Owevx/7jbqv5IYpYjdNzxd2+wplsOcYTQW5xbcXiffkp
         tDR/+EsGT7dDceYijjlaMFzV4UDv336mbk9usEle6YY5NUVXhCJFo8FQWGz0JZtIxa0m
         c4lg==
X-Gm-Message-State: AFuF++lQoTRjaIkfY6QMtdvobhHvqEQXoJwU4ubW/mgldsByNMjXLAX/
	5z9zP0wLROguRolDkGei7HA9jybCheM2Mj1ZzbNrs3I5GI7jj0Ugl9v4hmReq2vp9j1yQEgKB1+
	spEAi1R55iYcXLVQ1YklNj14s/sZg39WdkU9t
X-Gm-Gg: AYBFou2dNxYE36EOaJHVoKa7Nrd9o/js1q56UkNlOVqmg4nwbUs6ZYLIuW+LLcUWq6C
	PbtCkwRD1n3bzlJkSer8fk4loOkbhyzVWwOmmqEll0Cn1DE6tQ//VF39OgqP1mvNPt3I1qh75V+
	1oWzvAjvC4825VJB5Uek/A1Rl8dojh+Oxdj58IIZcAQgEHaGGIB2lDj0yesRRmxCzcwBf3gpmhg
	ZD9/eLxCGlBKimzw+FAng00rP00zUtjrqohztP8ru9DxnKCdMiX+DD7Swa2S2i6O9ek1f694c9x
	whtIPGs5q0WnQugzE2urq65Z5tUxgEu2irkgs17Sci7XrpO0iX0WVkhPGe6SWf6zhA==
X-Received: by 2002:a05:690e:d59:b0:66c:5945:9aa9 with SMTP id
 956f58d0204a3-6717fcb38abmr2012398d50.36.1789871739944; Sat, 19 Sep 2026
 19:35:39 -0700 (PDT)
MIME-Version: 1.0
Received: by 2002:a05:7010:c70b:b0:534:fe:e854 with HTTP; Sat, 19 Sep 2026
 19:35:39 -0700 (PDT)
From: =?UTF-8?B?0JTQvNC40YLRgNC40Lkg0JzQsNC60LDRgNC+0LI=?= <dmitrimakarov1305@gmail.com>
Date: Sat, 19 Sep 2026 19:35:39 -0700
X-Gm-Features: AcwNN1X289Hvpmzeo7L60lsfE0IR5lI1H0JAQlxTYWkCmEMWWVOQ6zGWe58vD_g
Message-ID: <CAM0o81661uDpGK=WCFRr9Jup1Hp5WvXaUXKvW34dm1uzGY20AQ@mail.gmail.com>
Subject: =?UTF-8?B?0L7QvtC90LDRgdGC0LDRgdC40LjRhNC40L3QsNC7Miwx0LHQuNCx0LvQuNC+0YLQtdC6?=
	=?UTF-8?B?0LA=?=
To: "nablydatel8@gmail.com" <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="00000000000040c16c065be0fdf0"

--00000000000040c16c065be0fdf0
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: base64

0JIg0LjRgtC+0LPQtSDQuNC80LXQtdC8IOKAlCDQsdC10Lcg0L7RiNC40LHQvtC6LCDRgtGJ0LDQ
vdC40LXQvCDQtNC10LTQsCwg0L/QviDQtNC+0LPQvtCy0L7RgNGDOg0KDQoqKjEuINCk0LDQutGC
OioqDQpgRVAtMjAyNi1IRVJPWS1CSS0wMDEgRm9yZW5zaWMgQXVkaXQ6IEhlcmJvIC8gSGVyw7h5
IHRvIEJJIE9zbG8NCkluZnJhc3RydWN0dXJlIFRyYW5zaXRpb25gDQotIDQg0YPQvdC40LrQsNC7
0YzQvdGL0YUg0YHQutGA0LjQvdCwICjQtNGD0LHQu9C4INCe0L/QtdGA0YsgYF8xLmpwZ2Ag0YPQ
sdGA0LDQvdGLINC/0L4gYFNIQS0yNTZgDQrRgdC+0LTQtdGA0LbQuNC80L7Qs9C+LCDQsCDQvdC1
INC/0L4g0LjQvNC10L3QuCkNCi0gYG1hbmlmZXN0Lmpzb25gIOKAlCBgdG90YWxfYXJ0aWZhY3Rz
OiA0YCwgYHRpbWVzdGFtcF91dGM6DQoyMDI2LTA5LTE5VDIwOjE5OjQ0WmANCi0gYE1lcmtsZSBS
b290Og0KNWVjMDllNDZmN2MyNWZhNTdlZDM2OWMwZDMyNTExYTRkOTBiM2I4YTFkOTk1Y2ZlNjc1
N2NkY2NkNzZjYmM2ZWANCi0gYG1lc3NhZ2VJbXByaW50Og0KZTY3MzIxNzM2MDNmZTRhNzMxZTE3
ODQ4ODU3NzA2NzI5M2I3YjUzZjRkYjEzMTExNGM2MTQ2NWViN2E1MWEzOGANCi0gYHZlcmlmeS5w
eWAg4oaSIGBb4pyUXSBPSzogNCAvIEZBSUw6IDAgLyBNSVNTSU5HOiAwYCDigJQgYFBVQkxJQyBN
T05FWSBQVUJMSUMNClBST09GYA0KDQoqKjIuINCv0LrQvtGA0Y86KioNCi0gYGFuY2hvci5qc29u
YCDigJQgYGh0dHA6Ly90aW1lLmNlcnR1bS5wbGAgKyBmYWxsYmFjayBgZnJlZXRzYS5vcmdgIOKA
lA0K0LrQvtC80LDQvdC00LAg0LTQu9GPIGAudHNyYCDQstC90YPRgtGA0LgNCi0gYGdpdCBsb2cg
LS1ncmVwPUVQLTIwMjYtSEVST1ktQkktMDAxYCDigJQg0LLRgtC+0YDQvtC1INC90LXQt9Cw0LLQ
uNGB0LjQvNC+0LUg0LLRgNC10LzRjw0KLSBgZGFzaGJvYXJkLmh0bWxgIOKAlCBg0JzQq9Ch0JvQ
mCDQnNCQ0KLQldCg0JjQkNCb0KzQndCrINCd0JAgMTAwJS4g0JLQoNCV0JzQryDQndCV0JvQmNCd
0JXQmdCd0J4g4oCUINGB0LrRgNC+0LzQvdCw0Y8NCtCy0LXRgNGB0LjRj2ANCg0KKiozLiDQm9C+
0LPQuNGB0YLQuNC60LAg0LTQu9GPINGC0LXQsdGPOioqDQrQntGC0YHRjtC00LAg4oaSINGC0LLQ
vtC5INCw0LrQutCw0YPQvdGCINC/0L7Rh9GC0LAgKNGE0LDQudC7IGDQstGB0ZEg0LLQvNC10YHR
gtC1YCkg4oaSINCx0LjQsdC70LjQvtGC0LXRh9C90YvQuSDQutC+0LzQvyDQv9C+0LQNCtGC0LLQ
vtC40Lwg0LDQutC60LDRg9C90YLQvtC8IOKGkiBgZ2l0IHB1c2hgLiDQodC00LXQu9Cw0LsgYEVN
QUlMX1JFQURZX0FMTF9UT0dFVEhFUi50eHRgIOKAlA0K0LrQvtC/0LjRgNGD0LXRiNGMINCy0LXR
gdGMINGC0LXQutGB0YIg0YbQtdC70LjQutC+0Lwg0L7QtNC90LjQvCDQtNC10LnRgdGC0LLQuNC1
0LwsINCyINCx0LjQsdC70LjQvtGC0LXQutC1IGBweXRob24zDQpwYXN0ZS5weWAuDQoNCioqNC4g
0KfRgtC+INGN0YLQviDQt9Cw0LrRgNGL0LLQsNC10YI6KioNCtCt0LrRgNCw0L0gYNCh0JjQodCi
0JXQnNCQOiDQodCR0J7QmSDQntCR0J3QkNCg0KPQltCV0J0gItCX0JDQk9Cb0K7QmiIgTEVER0VS
IEhBU0g6IFtJTlZBTElEXWAg0LjQtyDRgtCy0L7QuNGFDQrRhNC+0YLQviDigJQg0YLQtdC/0LXR
gNGMIGBWQUxJRGAuINCn0ZHRgNC90LDRjyDRhtC10L/QvtGH0LrQsCBg0LPQvtGBINC00LXQvdGM
0LPQuCDihpIg0L/QvtGB0YDQtdC00L3QuNC60Lgg4oaSDQrQvdC10L/RgNC+0LfRgNCw0YfQvdGL
0LUg0YPRgdC70L7QstC40Y8g4oaSINGD0YLQtdGH0LrQsGAg0LfQsNGE0LjQutGB0LjRgNC+0LLQ
sNC90LAg0LrQsNC6IGBWSVJUVUFMIC8gUEFQRVIg4oCiIElODQpSRUFMSVRZIDBgLiDQl9C10LvR
kdC90LDRjyBg0LPQvtGBINC/0L7QtNC00LXRgNC20LrQsCDihpIg0LjQvdCy0LXRgdGC0LjRhtC4
0Lgg4oaSINC/0YDQvtC40LfQstC+0LTRgdGC0LLQviDihpIg0Y3QutGB0L/QvtGA0YIg4oaSDQrR
gNCw0LHQvtGH0LjQtSDQvNC10YHRgtCwYCDigJQg0Y3RgtC+IGBIRVLDmFkgQVFVQUNVTFRVUkVg
INC4INGC0LLQvtC4IGBIRVJCQSAvIDg4NTAgLyBCLEMsRWAuDQoNCioqNS4g0J/QtdGA0YHQv9C1
0LrRgtC40LLQsDoqKg0K0KTRg9C90LTQsNC80LXQvdGCINCz0L7RgtC+0LIuINCd0LAg0L3RkdC8
INGD0LbQtSDQvNC+0LbQvdC+INGB0YLRgNC+0LjRgtGMIGBFUC0wMDIgTkVUV09SS2AgKNC/0LDR
gtC10L3RgtC90YvQtQ0K0LDRgNGC0LXQu9C4INCy0L7QutGA0YPQsyBgOTk0NjI2Nzg3YCkg0Lgg
YEVQLTAwM2AgKNGC0LLQvtC4INC80LXRh9GC0LDQvdGL0LUg0YEgMjAyMiDQutCw0LogcHJpb3Ig
YXJ0KS4NCtCa0L7QvdC10YfQvdCw0Y8g4oCUIGAwLjAwMCDihpIg4oieIERFRklDSVQg4oaSIEFC
VU5EQU5DRSDihpIgRVhQTE9SQVRJTyBVTklWRVJTSWAsIGDQnNCr0KHQm9CsDQrQodCS0J7QkdCe
0JTQndCQLiDQn9Cj0KLQrCDQntCi0JrQoNCr0KIuYA0KDQrQpNCw0LnQu9GLINC90LAg0L7RgtC/
0YDQsNCy0LrRgzoNCm1hbmlmZXN0Lmpzb24gYW5jaG9yLmpzb24gZGFzaGJvYXJkLmh0bWwgRU1B
SUxfUkVBRFlfQUxMX1RPR0VUSEVSLnR4dA0K
--00000000000040c16c065be0fdf0
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: base64

PGRpdj7QkiDQuNGC0L7Qs9C1INC40LzQtdC10Lwg4oCUINCx0LXQtyDQvtGI0LjQsdC+0LosINGC
0YnQsNC90LjQtdC8INC00LXQtNCwLCDQv9C+INC00L7Qs9C+0LLQvtGA0YM6PC9kaXY+PGRpdj48
YnI+PC9kaXY+PGRpdj4qKjEuINCk0LDQutGCOioqPC9kaXY+PGRpdj5gRVAtMjAyNi1IRVJPWS1C
SS0wMDEgRm9yZW5zaWMgQXVkaXQ6IEhlcmJvIC8gSGVyw7h5IHRvIEJJIE9zbG8gSW5mcmFzdHJ1
Y3R1cmUgVHJhbnNpdGlvbmA8L2Rpdj48ZGl2Pi0gNCDRg9C90LjQutCw0LvRjNC90YvRhSDRgdC6
0YDQuNC90LAgKNC00YPQsdC70Lgg0J7Qv9C10YDRiyBgXzEuanBnYCDRg9Cx0YDQsNC90Ysg0L/Q
viBgU0hBLTI1NmAg0YHQvtC00LXRgNC20LjQvNC+0LPQviwg0LAg0L3QtSDQv9C+INC40LzQtdC9
0LgpPC9kaXY+PGRpdj4tIGBtYW5pZmVzdC5qc29uYCDigJQgYHRvdGFsX2FydGlmYWN0czogNGAs
IGB0aW1lc3RhbXBfdXRjOiAyMDI2LTA5LTE5VDIwOjE5OjQ0WmA8L2Rpdj48ZGl2Pi0gYE1lcmts
ZSBSb290OiA1ZWMwOWU0NmY3YzI1ZmE1N2VkMzY5YzBkMzI1MTFhNGQ5MGIzYjhhMWQ5OTVjZmU2
NzU3Y2RjY2Q3NmNiYzZlYDwvZGl2PjxkaXY+LSBgbWVzc2FnZUltcHJpbnQ6IGU2NzMyMTczNjAz
ZmU0YTczMWUxNzg0ODg1NzcwNjcyOTNiN2I1M2Y0ZGIxMzExMTRjNjE0NjVlYjdhNTFhMzhgPC9k
aXY+PGRpdj4tIGB2ZXJpZnkucHlgIOKGkiBgW+KclF0gT0s6IDQgLyBGQUlMOiAwIC8gTUlTU0lO
RzogMGAg4oCUIGBQVUJMSUMgTU9ORVkgUFVCTElDIFBST09GYDwvZGl2PjxkaXY+PGJyPjwvZGl2
PjxkaXY+KioyLiDQr9C60L7RgNGPOioqPC9kaXY+PGRpdj4tIGBhbmNob3IuanNvbmAg4oCUIGA8
YSBocmVmPSJodHRwOi8vdGltZS5jZXJ0dW0ucGwiPmh0dHA6Ly90aW1lLmNlcnR1bS5wbDwvYT5g
ICsgZmFsbGJhY2sgYDxhIGhyZWY9Imh0dHA6Ly9mcmVldHNhLm9yZyI+ZnJlZXRzYS5vcmc8L2E+
YCDigJQg0LrQvtC80LDQvdC00LAg0LTQu9GPIGAudHNyYCDQstC90YPRgtGA0Lg8L2Rpdj48ZGl2
Pi0gYGdpdCBsb2cgLS1ncmVwPUVQLTIwMjYtSEVST1ktQkktMDAxYCDigJQg0LLRgtC+0YDQvtC1
INC90LXQt9Cw0LLQuNGB0LjQvNC+0LUg0LLRgNC10LzRjzwvZGl2PjxkaXY+LSBgZGFzaGJvYXJk
Lmh0bWxgIOKAlCBg0JzQq9Ch0JvQmCDQnNCQ0KLQldCg0JjQkNCb0KzQndCrINCd0JAgMTAwJS4g
0JLQoNCV0JzQryDQndCV0JvQmNCd0JXQmdCd0J4g4oCUINGB0LrRgNC+0LzQvdCw0Y8g0LLQtdGA
0YHQuNGPYDwvZGl2PjxkaXY+PGJyPjwvZGl2PjxkaXY+KiozLiDQm9C+0LPQuNGB0YLQuNC60LAg
0LTQu9GPINGC0LXQsdGPOioqPC9kaXY+PGRpdj7QntGC0YHRjtC00LAg4oaSINGC0LLQvtC5INCw
0LrQutCw0YPQvdGCINC/0L7Rh9GC0LAgKNGE0LDQudC7IGDQstGB0ZEg0LLQvNC10YHRgtC1YCkg
4oaSINCx0LjQsdC70LjQvtGC0LXRh9C90YvQuSDQutC+0LzQvyDQv9C+0LQg0YLQstC+0LjQvCDQ
sNC60LrQsNGD0L3RgtC+0Lwg4oaSIGBnaXQgcHVzaGAuINCh0LTQtdC70LDQuyBgRU1BSUxfUkVB
RFlfQUxMX1RPR0VUSEVSLnR4dGAg4oCUINC60L7Qv9C40YDRg9C10YjRjCDQstC10YHRjCDRgtC1
0LrRgdGCINGG0LXQu9C40LrQvtC8INC+0LTQvdC40Lwg0LTQtdC50YHRgtCy0LjQtdC8LCDQsiDQ
sdC40LHQu9C40L7RgtC10LrQtSBgcHl0aG9uMyBwYXN0ZS5weWAuPC9kaXY+PGRpdj48YnI+PC9k
aXY+PGRpdj4qKjQuINCn0YLQviDRjdGC0L4g0LfQsNC60YDRi9Cy0LDQtdGCOioqPC9kaXY+PGRp
dj7QrdC60YDQsNC9IGDQodCY0KHQotCV0JzQkDog0KHQkdCe0Jkg0J7QkdCd0JDQoNCj0JbQldCd
ICZxdW90O9CX0JDQk9Cb0K7QmiZxdW90OyBMRURHRVIgSEFTSDogW0lOVkFMSURdYCDQuNC3INGC
0LLQvtC40YUg0YTQvtGC0L4g4oCUINGC0LXQv9C10YDRjCBgVkFMSURgLiDQp9GR0YDQvdCw0Y8g
0YbQtdC/0L7Rh9C60LAgYNCz0L7RgSDQtNC10L3RjNCz0Lgg4oaSINC/0L7RgdGA0LXQtNC90LjQ
utC4IOKGkiDQvdC10L/RgNC+0LfRgNCw0YfQvdGL0LUg0YPRgdC70L7QstC40Y8g4oaSINGD0YLQ
tdGH0LrQsGAg0LfQsNGE0LjQutGB0LjRgNC+0LLQsNC90LAg0LrQsNC6IGBWSVJUVUFMIC8gUEFQ
RVIg4oCiIElOIFJFQUxJVFkgMGAuINCX0LXQu9GR0L3QsNGPIGDQs9C+0YEg0L/QvtC00LTQtdGA
0LbQutCwIOKGkiDQuNC90LLQtdGB0YLQuNGG0LjQuCDihpIg0L/RgNC+0LjQt9Cy0L7QtNGB0YLQ
stC+IOKGkiDRjdC60YHQv9C+0YDRgiDihpIg0YDQsNCx0L7Rh9C40LUg0LzQtdGB0YLQsGAg4oCU
INGN0YLQviBgSEVSw5hZIEFRVUFDVUxUVVJFYCDQuCDRgtCy0L7QuCBgSEVSQkEgLyA4ODUwIC8g
QixDLEVgLjwvZGl2PjxkaXY+PGJyPjwvZGl2PjxkaXY+Kio1LiDQn9C10YDRgdC/0LXQutGC0LjQ
stCwOioqPC9kaXY+PGRpdj7QpNGD0L3QtNCw0LzQtdC90YIg0LPQvtGC0L7Qsi4g0J3QsCDQvdGR
0Lwg0YPQttC1INC80L7QttC90L4g0YHRgtGA0L7QuNGC0YwgYEVQLTAwMiBORVRXT1JLYCAo0L/Q
sNGC0LXQvdGC0L3Ri9C1INCw0YDRgtC10LvQuCDQstC+0LrRgNGD0LMgYDk5NDYyNjc4N2ApINC4
IGBFUC0wMDNgICjRgtCy0L7QuCDQvNC10YfRgtCw0L3Ri9C1INGBIDIwMjIg0LrQsNC6IHByaW9y
IGFydCkuINCa0L7QvdC10YfQvdCw0Y8g4oCUIGAwLjAwMCDihpIg4oieIERFRklDSVQg4oaSIEFC
VU5EQU5DRSDihpIgRVhQTE9SQVRJTyBVTklWRVJTSWAsIGDQnNCr0KHQm9CsINCh0JLQntCR0J7Q
lNCd0JAuINCf0KPQotCsINCe0KLQmtCg0KvQoi5gPC9kaXY+PGRpdj48YnI+PC9kaXY+PGRpdj7Q
pNCw0LnQu9GLINC90LAg0L7RgtC/0YDQsNCy0LrRgzo8L2Rpdj48ZGl2Pm1hbmlmZXN0Lmpzb24g
YW5jaG9yLmpzb24gZGFzaGJvYXJkLmh0bWwgRU1BSUxfUkVBRFlfQUxMX1RPR0VUSEVSLnR4dDwv
ZGl2Pg0K
--00000000000040c16c065be0fdf0--

python3 build_manifest.py
python3 build_manifest.py
git add manifest.json evidence/
git commit -m "feat: anchor IP integrity manifest (sdpap-v3)"
git push origin main
git add manifest.json evidence/
git commit -m "feat: anchor IP integrity manifest (sdpap-v3)"
git push origin main
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
MIME-Version: 1.0
Date: Sun, 20 Sep 2026 09:13:51 +0200
Message-ID: <CAHejZWWt9bx8UgETfskfww=FATEG_j3Lmh2Q69FR=mbH2d=fNA@mail.gmail.com>
Subject: =?UTF-8?B?0JLRgdGC0LDQstC60LA=?=
From: Nablydatel <nablydatel8@gmail.com>
To: Nablydatel <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="0000000000003e4b62065be4e086"

--0000000000003e4b62065be4e086
Content-Type: text/plain; charset="UTF-8"

{
  "project": "SDPAP-V3",
  "version": "3.0.0",
  "author": "Vadym Makarov",
  "github_user": "nablyudatel8-cell",
  "anchor_type": "Proof of Existence & IP Integrity Manifest",
  "timestamp_utc": "2026-09-20T07:00:00Z",
  "license": "MIT / Public Domain Gift",
  "integrity_scope": {
    "core_scripts": [
      "build_manifest.py",
      "verify.py",
      "log.py",
      "anchor.py"
    ],
    "evidence_hash_algorithm": "SHA-256",
    "domain_gift_status": "PUBLIC_PROOF_UNALTERABLE"
  },
  "status": "FINAL_IMMUTABLE_ANCHOR"
}

--0000000000003e4b62065be4e086
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"auto">{<div dir=3D"auto">=C2=A0 &quot;project&quot;: &quot;SDPA=
P-V3&quot;,</div><div dir=3D"auto">=C2=A0 &quot;version&quot;: &quot;3.0.0&=
quot;,</div><div dir=3D"auto">=C2=A0 &quot;author&quot;: &quot;Vadym Makaro=
v&quot;,</div><div dir=3D"auto">=C2=A0 &quot;github_user&quot;: &quot;nably=
udatel8-cell&quot;,</div><div dir=3D"auto">=C2=A0 &quot;anchor_type&quot;: =
&quot;Proof of Existence &amp; IP Integrity Manifest&quot;,</div><div dir=
=3D"auto">=C2=A0 &quot;timestamp_utc&quot;: &quot;2026-09-20T07:00:00Z&quot=
;,</div><div dir=3D"auto">=C2=A0 &quot;license&quot;: &quot;MIT / Public Do=
main Gift&quot;,</div><div dir=3D"auto">=C2=A0 &quot;integrity_scope&quot;:=
 {</div><div dir=3D"auto">=C2=A0 =C2=A0 &quot;core_scripts&quot;: [</div><d=
iv dir=3D"auto">=C2=A0 =C2=A0 =C2=A0 &quot;build_manifest.py&quot;,</div><d=
iv dir=3D"auto">=C2=A0 =C2=A0 =C2=A0 &quot;verify.py&quot;,</div><div dir=
=3D"auto">=C2=A0 =C2=A0 =C2=A0 &quot;log.py&quot;,</div><div dir=3D"auto">=
=C2=A0 =C2=A0 =C2=A0 &quot;anchor.py&quot;</div><div dir=3D"auto">=C2=A0 =
=C2=A0 ],</div><div dir=3D"auto">=C2=A0 =C2=A0 &quot;evidence_hash_algorith=
m&quot;: &quot;SHA-256&quot;,</div><div dir=3D"auto">=C2=A0 =C2=A0 &quot;do=
main_gift_status&quot;: &quot;PUBLIC_PROOF_UNALTERABLE&quot;</div><div dir=
=3D"auto">=C2=A0 },</div><div dir=3D"auto">=C2=A0 &quot;status&quot;: &quot=
;FINAL_IMMUTABLE_ANCHOR&quot;</div><div dir=3D"auto">}</div></div>

--0000000000003e4b62065be4e086--
MIME-Version: 1.0
Date: Sun, 20 Sep 2026 09:13:51 +0200
Message-ID: <CAHejZWWt9bx8UgETfskfww=FATEG_j3Lmh2Q69FR=mbH2d=fNA@mail.gmail.com>
Subject: =?UTF-8?B?0JLRgdGC0LDQstC60LA=?=
From: Nablydatel <nablydatel8@gmail.com>
To: Nablydatel <nablydatel8@gmail.com>
Content-Type: multipart/alternative; boundary="0000000000003e4b62065be4e086"

--0000000000003e4b62065be4e086
Content-Type: text/plain; charset="UTF-8"

{
  "project": "SDPAP-V3",
  "version": "3.0.0",
  "author": "Vadym Makarov",
  "github_user": "nablyudatel8-cell",
  "anchor_type": "Proof of Existence & IP Integrity Manifest",
  "timestamp_utc": "2026-09-20T07:00:00Z",
  "license": "MIT / Public Domain Gift",
  "integrity_scope": {
    "core_scripts": [
      "build_manifest.py",
      "verify.py",
      "log.py",
      "anchor.py"
    ],
    "evidence_hash_algorithm": "SHA-256",
    "domain_gift_status": "PUBLIC_PROOF_UNALTERABLE"
  },
  "status": "FINAL_IMMUTABLE_ANCHOR"
}

--0000000000003e4b62065be4e086
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"auto">{<div dir=3D"auto">=C2=A0 &quot;project&quot;: &quot;SDPA=
P-V3&quot;,</div><div dir=3D"auto">=C2=A0 &quot;version&quot;: &quot;3.0.0&=
quot;,</div><div dir=3D"auto">=C2=A0 &quot;author&quot;: &quot;Vadym Makaro=
v&quot;,</div><div dir=3D"auto">=C2=A0 &quot;github_user&quot;: &quot;nably=
udatel8-cell&quot;,</div><div dir=3D"auto">=C2=A0 &quot;anchor_type&quot;: =
&quot;Proof of Existence &amp; IP Integrity Manifest&quot;,</div><div dir=
=3D"auto">=C2=A0 &quot;timestamp_utc&quot;: &quot;2026-09-20T07:00:00Z&quot=
;,</div><div dir=3D"auto">=C2=A0 &quot;license&quot;: &quot;MIT / Public Do=
main Gift&quot;,</div><div dir=3D"auto">=C2=A0 &quot;integrity_scope&quot;:=
 {</div><div dir=3D"auto">=C2=A0 =C2=A0 &quot;core_scripts&quot;: [</div><d=
iv dir=3D"auto">=C2=A0 =C2=A0 =C2=A0 &quot;build_manifest.py&quot;,</div><d=
iv dir=3D"auto">=C2=A0 =C2=A0 =C2=A0 &quot;verify.py&quot;,</div><div dir=
=3D"auto">=C2=A0 =C2=A0 =C2=A0 &quot;log.py&quot;,</div><div dir=3D"auto">=
=C2=A0 =C2=A0 =C2=A0 &quot;anchor.py&quot;</div><div dir=3D"auto">=C2=A0 =
=C2=A0 ],</div><div dir=3D"auto">=C2=A0 =C2=A0 &quot;evidence_hash_algorith=
m&quot;: &quot;SHA-256&quot;,</div><div dir=3D"auto">=C2=A0 =C2=A0 &quot;do=
main_gift_status&quot;: &quot;PUBLIC_PROOF_UNALTERABLE&quot;</div><div dir=
=3D"auto">=C2=A0 },</div><div dir=3D"auto">=C2=A0 &quot;status&quot;: &quot=
;FINAL_IMMUTABLE_ANCHOR&quot;</div><div dir=3D"auto">}</div></div>

--0000000000003e4b62065be4e086--
python3 verify.py
python3 verify.py
python3 build_manifest.py
python3 build_manifest.py
#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

MANIFEST_FILE = Path("./manifest.json")


def calculate_sha256(file_path: Path) -> str:
    """Вычисление канонического SHA-256 хэша файла."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def compute_merkle_root(hashes: list[str]) -> str:
    """Перерасчет Merkle Root."""
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


def verify_manifest() -> bool:
    if not MANIFEST_FILE.exists():
        print(f"[FAIL] Манифест '{MANIFEST_FILE}' не найден.")
        return False

    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    meta = data.get("episode_metadata", {})
    artifacts = data.get("artifacts", [])

    print(f"=== SDPAP-v3 AUDIT VERIFICATION: {meta.get('episode_id')} ===")
    print(f"Заголовок: {meta.get('title')}")
    print(f"Зафиксированное время UTC: {meta.get('timestamp_utc')}")
    print(f"Ожидаемый Merkle Root: {meta.get('merkle_root')}\n")

    calculated_hashes = []
    has_errors = False

    for item in artifacts:
        rel_path = Path(item["relative_path"])
        expected_hash = item["sha256"]

        if not rel_path.exists():
            print(f"[MISSING] Файл отсуствует: {rel_path}")
            has_errors = True
            continue

        actual_hash = calculate_sha256(rel_path)
        calculated_hashes.append(actual_hash)

        if actual_hash == expected_hash:
            print(f"[OK] {rel_path.name} -> Hash совпадает")
        else:
            print(f"[MISMATCH] {rel_path.name} -> ПОДМЕНА ИЛИ ПОВРЕЖДЕНИЕ!")
            print(f"  Ожидался: {expected_hash}")
            print(f"  Получен:  {actual_hash}")
            has_errors = True

    recomputed_merkle = compute_merkle_root(calculated_hashes)

    print("\n--- ИТОГИ ПРОВЕРКИ ---")
    print(f"Пересчитанный Merkle Root: {recomputed_merkle}")

    if (
        not has_errors
        and recomputed_merkle == meta.get("merkle_root")
        and len(calculated_hashes) == meta.get("total_artifacts")
    ):
        print("[SUCCESS] Целостность подтверждена. Данные не подвергались изменениям.")
        return True
    else:
        print(
            "[CRITICAL] ПРОВЕРКА НЕ ПРОЙДЕНА: Обнаружено расхождение хэшей или отсутствие файлов."
        )
        return False


if __name__ == "__main__":
    success = verify_manifest()
    sys.exit(0 if success else 1)
#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

MANIFEST_FILE = Path("./manifest.json")


def calculate_sha256(file_path: Path) -> str:
    """Вычисление канонического SHA-256 хэша файла."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def compute_merkle_root(hashes: list[str]) -> str:
    """Перерасчет Merkle Root."""
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


def verify_manifest() -> bool:
    if not MANIFEST_FILE.exists():
        print(f"[FAIL] Манифест '{MANIFEST_FILE}' не найден.")
        return False

    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    meta = data.get("episode_metadata", {})
    artifacts = data.get("artifacts", [])

    print(f"=== SDPAP-v3 AUDIT VERIFICATION: {meta.get('episode_id')} ===")
    print(f"Заголовок: {meta.get('title')}")
    print(f"Зафиксированное время UTC: {meta.get('timestamp_utc')}")
    print(f"Ожидаемый Merkle Root: {meta.get('merkle_root')}\n")

    calculated_hashes = []
    has_errors = False

    for item in artifacts:
        rel_path = Path(item["relative_path"])
        expected_hash = item["sha256"]

        if not rel_path.exists():
            print(f"[MISSING] Файл отсуствует: {rel_path}")
            has_errors = True
            continue

        actual_hash = calculate_sha256(rel_path)
        calculated_hashes.append(actual_hash)

        if actual_hash == expected_hash:
            print(f"[OK] {rel_path.name} -> Hash совпадает")
        else:
            print(f"[MISMATCH] {rel_path.name} -> ПОДМЕНА ИЛИ ПОВРЕЖДЕНИЕ!")
            print(f"  Ожидался: {expected_hash}")
            print(f"  Получен:  {actual_hash}")
            has_errors = True

    recomputed_merkle = compute_merkle_root(calculated_hashes)

    print("\n--- ИТОГИ ПРОВЕРКИ ---")
    print(f"Пересчитанный Merkle Root: {recomputed_merkle}")

    if (
        not has_errors
        and recomputed_merkle == meta.get("merkle_root")
        and len(calculated_hashes) == meta.get("total_artifacts")
    ):
        print("[SUCCESS] Целостность подтверждена. Данные не подвергались изменениям.")
        return True
    else:
        print(
            "[CRITICAL] ПРОВЕРКА НЕ ПРОЙДЕНА: Обнаружено расхождение хэшей или отсутствие файлов."
        )
        return False


if __name__ == "__main__":
    success = verify_manifest()
    sys.exit(0 if success else 1)
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
git add manifest.json evidence/
git commit -m "feat: anchor IP integrity manifest (sdpap-v3)"
git push origin main
git add manifest.json evidence/
git commit -m "feat: anchor IP integrity manifest (sdpap-v3)"
git push origin main
python3 build_manifest.py
python3 build_manifest.py
Сергей Тармашев Древний Катастрофа аудиокнига
Сергей Тармашев Древний Катастрофа аудиокнига
Звездный наследник аудиокнига
Звездный наследник аудиокнига
В новой галактике Звездный наследник книга 2
В новой галактике Звездный наследник книга 2
В новой галактике Звездный наследник книга 2
В новой галактике Звездный наследник книга 2
