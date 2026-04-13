import os
import time
import json
from geopy.distance import geodesic

RINGTONE = os.path.expanduser("~/storage/downloads/your-ringtone.mp3")  #Replace the path with your own path

# ==============================
# GET CURRENT GPS LOCATION
# ==============================

def get_current_location():
    try:
        output = os.popen("termux-location").read()
        data = json.loads(output)
        return (data["latitude"], data["longitude"])
    except Exception as e:
        print("GPS error:", e)
        return None


# ==============================
# USER DESTINATION INPUT
# ==============================

def get_target_coordinates():
    coords = input("\nEnter destination coordinates (lat,lon): ")

    try:
        lat, lon = coords.split(",")
        lat = float(lat)
        lon = float(lon)

        print(f"\nDestination set to: {lat}, {lon}")
        return lat, lon

    except:
        print("Invalid format. Use: latitude,longitude")
        exit()


# ==============================
# TRAVEL MODE
# ==============================

def choose_mode():
    print("\nSelect travel mode:")
    print("1. Walk (100m)")
    print("2. Cycle (200m)")
    print("3. Car (500m)")
    print("4. Train / Bus (800m)")
    print("5. Custom")

    choice = input("Choice: ")

    modes = {
        "1": 100,
        "2": 200,
        "3": 500,
        "4": 800
    }

    if choice == "5":
        return int(input("Enter trigger distance (meters): "))

    return modes.get(choice, 300)


# ==============================
# ALARM
# ==============================

def start_alarm():
    print("\n🎯 Destination reached!")

    os.system(
        "termux-notification "
        "--title 'Location Alarm' "
        "--content 'Destination reached!' "
        "--button1 'STOP' "
        "--action 'echo stop > alarm_stop.txt'"
    )

    os.system(f"termux-media-player play {RINGTONE}")

    while True:
        os.system("termux-vibrate -d 1000")
        time.sleep(2)

        if os.path.exists("alarm_stop.txt"):
            os.system("termux-media-player stop")
            os.remove("alarm_stop.txt")
            break


# ==============================
# MAIN
# ==============================

def main():
    os.system("termux-wake-lock")

    print("\n==============================")
    print("   LOCATION BASED ALARM")
    print("==============================")

    target_lat, target_lon = get_target_coordinates()
    trigger_distance_m = choose_mode()

    print(f"\nAlarm will trigger within {trigger_distance_m} m")
    last_distance = None

    print("\nTracking location...\n")

    while True:
        # Use real GPS (recommended)
        location = get_current_location()

        # If you want manual testing, comment above and use below:
        # lat = float(input("Current latitude: "))
        # lon = float(input("Current longitude: "))
        # location = (lat, lon)

        if location:
            distance = geodesic(location, (target_lat, target_lon)).meters
            print(f"Distance: {int(distance)} meters")

            if distance <= trigger_distance_m:
                start_alarm()
                break

            if last_distance and distance > last_distance:
                print("⚠ Passed destination. Triggering alarm.")
                start_alarm()
                break

            last_distance = distance
        else:
            print("Failed to get location")

        if last_distance and last_distance < 1000:
            time.sleep(3)
        else:
            time.sleep(10)

    print("\nReleasing wake lock...")
    os.system("termux-wake-unlock")
    print("Alarm finished.")


# ==============================

if __name__ == "__main__":
    main()
