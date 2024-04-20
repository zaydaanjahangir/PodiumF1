from urllib.request import urlopen
import json
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

driver_numbers = [1,2,3,4,10,11,14,16,18,20,22,23,24,27,31,44,55,63,77,81]

def get_leaderboard_data(meeting_key='latest'):
    leaderboard = []
    for driver_number in driver_numbers:
        url = f"https://api.openf1.org/v1/position?meeting_key={meeting_key}&driver_number={driver_number}"

        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))

            if data:  # If there's a valid position
                leaderboard.append({
                    'driver_number': driver_number,
                    'position': data[0]['position']  
                })
        except Exception as e:
            print(f"Error fetching data for driver {driver_number}: {e}")

    return leaderboard

while True:
    leaderboard_data = get_leaderboard_data()

    print("----- Leaderboard -----")

    for entry in leaderboard_data:
        print(f"Driver: {entry['driver_number']}, Position: {entry['position']}")

    print("-------------------")
    time.sleep(5)  # Update every 5 seconds
