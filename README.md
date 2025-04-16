# 🛡️ DDoS Detection System

A real-time **DDoS attack detection** tool built using Python and Scapy. This lightweight script monitors network packets and identifies potential DDoS attacks based on request rate thresholds.

---

## 🚀 Features

- 📡 Real-time packet sniffing using Scapy
- ⚠️ DDoS detection based on customizable thresholds
- 🧠 Intelligent IP tracking with timestamped logs
- 📁 Logs alerts in `alerts.log` and tracks IP activity in `IP_tracker.json`
- 💡 Easy to configure and run

---

## 📂 Project Structure

```
DDoS-Detection/
│
├── main.py              # Main Python script for detection
├── alerts.log           # (Auto-generated) Log of DDoS alerts
├── IP_tracker.json      # (Auto-generated) Tracks suspicious IPs
└── README.md            # Project documentation
```

---

## 🧰 Requirements

- Python 3.x
- Scapy

Install dependencies:

```bash
pip install scapy
```

---

## ⚙️ How It Works

- Listens to all incoming IP packets.
- Logs each request from a source IP with a timestamp.
- If the number of requests from one IP exceeds a defined **threshold** in a short **time window**, it's flagged as a DDoS attempt.
- Triggers an alert and updates the IP tracker.

---

## 📝 Configuration

You can tweak detection sensitivity in `main.py`:

```python
THRESHOLD = 100      # Max requests allowed in time window
TIME_WINDOW = 10     # Time window in seconds
```

---

## 🛠️ Running the Script

```bash
sudo python main.py
```

> Use `sudo` if you're on Linux/macOS, since sniffing may require root access.

---

## 📒 Output Example

```
[*] Starting real-time DDoS detection...
🚨 DDoS ALERT: IP 192.168.1.101 made 120 requests in 10 seconds!
```

All alerts are stored in `alerts.log`  
All IP activity is logged in `IP_tracker.json`

---

## 📌 Use Cases

- Educational/Academic projects
- Small-scale network defense simulations
- Lightweight home router monitoring

---

## 🧠 Author

**Mehere Aniket Vitthal**  
GitHub: [aniketmehere](https://github.com/aniketmehere)

---

## 🛡️ Disclaimer

This project is intended for **educational purposes** only. Use responsibly and only on networks you own or have permission to monitor.

---
