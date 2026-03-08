def analyze_log(filename):
    failed_counts = {}

    threshold = int(input("Enter failed login threshold: "))

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) < 4:
                continue

            status = parts[2]
            ip_address = parts[3]

            if status == "FAILED_LOGIN":
                if ip_address in failed_counts:
                    failed_counts[ip_address] += 1
                else:
                    failed_counts[ip_address] = 1

    print("\nFailed login summary:")
    for ip, count in failed_counts.items():
        print(f"{ip}: {count} failed login attempt(s)")

    print("\nSuspicious IP addresses:")
    found_suspicious = False

    with open("alerts.txt", "w") as alert_file:
        for ip, count in failed_counts.items():
            if count >= threshold:
                message = f"ALERT: {ip} had {count} failed login attempts"
                print(message)
                alert_file.write(message + "\n")
                found_suspicious = True

    if not found_suspicious:
        print("No suspicious activity detected.")

    max_ip = ""
    max_count = 0

    for ip, count in failed_counts.items():
        if count > max_count:
            max_count = count
            max_ip = ip

    if max_ip != "":
        print(f"\nMost suspicious IP: {max_ip} with {max_count} failed attempts")


analyze_log("sample_logtext.py")