import random

ips = ["192.168.1.10", "10.0.0.5", "172.16.0.3", "192.168.1.20"]
events = [
    "Failed password for root from {}",
    "Accepted password for user from {}",
    "Invalid user admin from {}",
    "scan from {}",
    "SELECT * FROM users",
    "DROP TABLE users;"
]

with open("logs/large.log", "w") as f:
    for _ in range(100000):  # change number for bigger file
        event = random.choice(events)
        if "{}" in event:
            event = event.format(random.choice(ips))
        f.write(event + "\n")

print("Large log file created!")