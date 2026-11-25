sample_logs = """
2026-11-25 09:12:01 INFO User admin logged in successfully from 192.168.1.10
2026-11-25 09:14:22 WARN Failed password for user root from 45.33.32.156
2026-11-25 09:14:25 WARN Failed password for user root from 45.33.32.156
2026-11-25 09:15:10 INFO User rahul logged in successfully from 192.168.1.15
2026-11-25 09:16:02 WARN Failed password for user admin from 45.33.32.156
"""

failed_count = 0

for line in sample_logs.splitlines():
    if "Failed password" in line:
        failed_count += 1
        print("Alert found:", line)

print("\nTotal failed login attempts detected:", 
