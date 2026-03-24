# Location-Based Alarm System Using Termux
(Personal project to trigger alarm when near destination (to avoid missing stops), coded in termux environment to use quickly without deployment).

A lightweight, terminal-driven **location-aware alert system** designed for Android environments using Termux.

This application continuously monitors the user’s GPS position and triggers an alert when approaching a predefined destination.

---

## ✨ Features

- 📡 Real-time GPS tracking via Termux API  
- 🎯 Distance-based trigger using geodesic calculations  
- 🚶 Multiple travel modes:
  - Walk (100m)
  - Cycle (200m)
  - Car (500m)
  - Public Transport (800m)
  - Custom distance  
- 🔔 Multi-modal alert system:
  - Notification
  - Audio playback
  - Vibration loop  
- ⚠️ Overshoot detection  

---
## 🏗️ System Architecture

| Component             | Technology Used        |
|----------------------|-----------------------|
| Location Fetching    | termux-location       |
| Distance Calculation | geopy (geodesic)      |
| Notifications        | termux-notification   |
| Audio Alerts         | termux-media-player   |
| Vibration            | termux-vibrate        |

---

## ⚙️ Installation

### 1. Install Termux Packages

    pkg update && pkg upgrade
    pkg install python termux-api

### 2. Clone Repository

    git clone https://github.com/yourusername/location-alarm-termux.git
    cd location-alarm-termux

### 3. Install Dependencies

    pip install -r requirements.txt

---

## ▶️ Usage

    python main.py

### Steps:

1. Enter destination coordinates (`latitude,longitude`)
2. Choose travel mode or custom distance
3. The system will track your movement
4. Alarm triggers when you reach or pass destination

---
## 📂 Project Structure

    location-alarm-termux/
    │
    ├── main.py
    ├── README.md
    ├── requirements.txt
    ├── .gitignore
    ├── LICENSE
    │
    ├── assets/
    │   └── demo.png
    │
    └── docs/
        └── architecture.md

---

## 🚧 Limitations

- Requires Termux environment (Android only)
- GPS accuracy depends on device hardware
- No background execution

---

## 🔮 Future Enhancements

- Background service support  
- Map API integration  
- ETA-based smart alerts  
- Custom alarm profiles  
- Travel analytics  

---

## 💼 Use Cases

- Daily commuting  
- Travel navigation  
- Location-based reminders  
- Accessibility support  

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

---

## 📄 License

MIT License

---

## 🧠 Summary

A practical **location-triggered alert system** integrating mobile utilities with geospatial computation.
