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

### 1. Install Termux and Termux:API
- Install Termux from F-Droid (recommended)
- Install the **Termux:API** app from F-Droid or Play Store

Grant **Location permission** to Termux:API in Android settings.

---

### 2. Install Required Packages in Termux
```bash
pkg update && pkg upgrade
pkg install python termux-api git
```

---

### 3. Verify GPS Access
Run:
```bash
termux-location
```

You should see JSON output with latitude and longitude.

If this fails:
- Enable location services on your phone
- Grant location permission to Termux

---

### 4. Clone the Repository
```bash
git clone https://github.com/sri443/Location-Alarm-On-Android-Using-Termux.git
cd Location-Alarm-On-Android-Using-Termux
```

---

### 5. Install Python Dependencies
```bash
pip install -r requirements.txt
```

## 🔊 Custom Ringtone Setup

By default, the script expects a ringtone file path. You need to update this to match a valid audio file on your device.

### 📍 Step 1: Add Your Ringtone

Place an audio file (e.g. `.mp3`, `.wav`) somewhere accessible on your device.

Example locations:
- `/sdcard/Download/alarm.mp3`
- `/storage/emulated/0/Music/alarm.mp3`

---

### 🛠️ Step 2: Update the File Path

Open `main.py` and find the line where the audio file is used.

Replace it with your file path:

```python
RINGTONE = os.path.expanduser("~/storage/downloads/your-ringtone.mp3") 
```

Make sure:
- The path is correct
- The file exists

---

### ▶️ Step 3: Test Audio Playback

Run this command in Termux:

```bash
termux-media-player play /sdcard/Download/alarm.mp3
```

If the audio plays, you're good.

---

## ❗ Troubleshooting

### Audio not playing

- Check file path is correct
- Ensure file format is supported (`.mp3` recommended)
- Verify file exists:
  ```bash
  ls /sdcard/Download/
  ```

---

### Permission issues

Run:
```bash
termux-setup-storage
```

Then restart Termux and try again.

---

### Command not found (termux-media-player)

Install required package:
```bash
pkg install termux-api
```

Also ensure the **Termux:API app** is installed on your phone.

---

### No sound even though command runs

- Check phone volume
- Make sure media volume is not muted
- Try a different audio file

---

## ⚠️ Notes

- Absolute file paths are required (relative paths may fail)
- Keep the file in internal storage (not restricted app folders)

---

## ▶️ Usage

Run the script:
```bash
python main.py
```

### Steps:
1. Enter destination coordinates  
   Example:
   ```
   13.0827,80.2707
   ```

2. Choose travel mode or set a custom distance  
   (This determines how far from the destination the alarm triggers)

3. The system will continuously track your location

4. Alarm will trigger when:
   - You are within the selected distance  
   - OR you pass the destination

---

## ❗ Troubleshooting

- **No GPS data**
  - Ensure location is enabled on your phone
  - Check permissions for Termux and Termux:API
  - Run `termux-location` manually to verify

- **Command not found (termux-*)**
  - Make sure `termux-api` package is installed

- **Script errors**
  - Reinstall dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## ⚠️ Notes

- Works only on Android (Termux environment)
- GPS accuracy depends on device and surroundings
- Uses a wakelock to keep running even when the screen is off
- Not a true background service — may stop if Termux is closed or restricted by Android

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
