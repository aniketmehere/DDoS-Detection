
from scapy.all import *
import time
import json
from datetime import datetime
import winsound  # ✅ Added for sound alert

# Set a threshold and time window for DDoS detection
THRESHOLD = 100  # Example threshold: 100 requests
TIME_WINDOW = 10  # 10 seconds

ip_request_log = {}

# ✅ Sound function
def play_alert_sound():
    winsound.Beep(1000, 500)  # Frequency: 1000Hz, Duration: 500ms

# Initialize the IP tracker
def update_ip_tracker(ip):
    try:
        # Attempt to read the IP tracker file
        with open("IP_tracker.json", "r") as file:
            try:
                ip_tracker = json.load(file)  # Try loading the existing JSON data
            except json.JSONDecodeError:
                # If the file is empty or invalid JSON, initialize it as an empty dict
                ip_tracker = {}
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty tracker
        ip_tracker = {}

    if ip in ip_tracker:
        ip_tracker[ip]["request_count"] += 1
        ip_tracker[ip]["last_request_time"] = str(datetime.now())
    else:
        ip_tracker[ip] = {
            "request_count": 1,
            "last_request_time": str(datetime.now())
        }

    try:
        # Try writing the updated data back to the file
        with open("IP_tracker.json", "w") as file:
            json.dump(ip_tracker, file, indent=4)
    except Exception as e:
        print(f"Error writing to IP_tracker.json: {e}")

def detect_ddos(pkt):
    if IP in pkt:
        ip_src = pkt[IP].src  # Get the source IP of the packet
        
        current_time = time.time()
        
        # Initialize the log for the IP address if it's not already present
        if ip_src not in ip_request_log:
            ip_request_log[ip_src] = []
        
        # Add the current timestamp to the log for this IP
        ip_request_log[ip_src].append(current_time)
        
        # Clean up timestamps older than the time window
        ip_request_log[ip_src] = [t for t in ip_request_log[ip_src] if current_time - t < TIME_WINDOW]
        
        # Check if the number of requests exceeds the threshold
        if len(ip_request_log[ip_src]) > THRESHOLD:
            alert = f"🚨 DDoS ALERT: IP {ip_src} made {len(ip_request_log[ip_src])} requests in {TIME_WINDOW} seconds!"
            print(alert)  # Printing to console

            # ✅ Play sound on alert
            play_alert_sound()

            # Try to log to file
            try:
                with open("alerts.log", "a", encoding="utf-8") as f:
                    f.write(alert + "\n")
            except Exception as e:
                print(f"[!] Failed to log/send alert: {e}")

            # Update IP Tracker after alert
            update_ip_tracker(ip_src)

# Start sniffing network traffic and call detect_ddos function for each packet
print("[*] Starting real-time DDoS detection...")
sniff(filter="ip", prn=detect_ddos, store=0)
