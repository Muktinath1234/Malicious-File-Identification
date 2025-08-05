project/
│malware
├── malware_hashes.json
├── scan_target/             # Folder containing test files
│   ├── test1.exe
│   └── eicar_test.txt
└── malware_scan.py
Scanning folder: ./scan_target

[SAFE] test1.exe
[ALERT] Malicious file found: ./scan_target/eicar_test.txt

Scan complete.

Flagged malicious files:
- ./scan_target/eicar_test.txt (SHA-256: ...)
