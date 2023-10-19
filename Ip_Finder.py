import os
import sys
import time

def send_ping(ip_address):
    response = os.system(f"ping -n 1 -w 50 {ip_address}")
    return response == 0

def ping_range(start, end):
    successes = []
    total_ips = end - start + 1
    print(f"Pinging IP addresses in range {start} to {end}...")

    for i in range(start, end + 1):
        ip_address = f"192.168.15.{i}"
        if send_ping(ip_address):
            successes.append(ip_address)

        # Update progress every 10 pings
        if i % 10 == 0:
            progress = '#' * int(len(successes) * 100 / total_ips)
            spaces = ' ' * (100 - len(progress))
            sys.stdout.write(f"\rProgress: [{progress}{spaces}] {len(successes)}/{total_ips}")
            sys.stdout.flush()

    sys.stdout.write('\n')
    print(f"Pinged {len(successes)}/{total_ips} IP addresses successfully.")

    with open("alive.txt", "w") as file:
        for ip in successes:
            file.write(f"{ip}\n")

if __name__ == "__main__":
    start_ip = 1  # Start IP address
    end_ip = 225  # End IP address

    ping_range(start_ip, end_ip)
