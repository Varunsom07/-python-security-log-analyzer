# Python Security Log Analyzer

A Python-based cybersecurity tool that analyzes authentication logs and detects suspicious IP addresses with repeated failed login attempts.

## Features
- Parses authentication log files
- Counts failed login attempts by IP address
- Detects possible brute-force login attacks
- Generates alerts for suspicious activity

## Example Log Format
2026-03-07 10:15:23 FAILED_LOGIN 192.168.1.10

## How to Run

1. Clone the repository
2. Run the script:

python log_analyzer.py

3. Enter the threshold for failed login attempts when prompted.

## Technologies
- Python
