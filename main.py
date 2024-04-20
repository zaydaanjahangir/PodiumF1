from urllib.request import urlopen
import json
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

driver_numbers = [1,2,3,4,10,11,14,16,18,20,22,23,24,27,31,44,55,63,77,81]
driver_names = {
    1: "Max Verstappen",
    2: "Logan Sargeant",
    3: "Daniel Ricciardo",
    4: "Lando Norris",
    10: "Pierre Gasly",
    11: "Sergio Pérez",
    14: "Fernando Alonso",
    16: "Charles Leclerc",
    18: "Lance Stroll",
    20: "Kevin Magnussen",
    22: "Yuki Tsunoda",
    23: "Alexander Albon",
    24: "Zhou Guanyu",
    27: "Nico Hülkenberg",
    31: "Esteban Ocon",
    44: "Lewis Hamilton",
    55: "Carlos Sainz Jr.",
    63: "George Russell",
    77: "Valtteri Bottas",
    81: "Oscar Piastri"
}



def get_leaderboard_data(meeting_key='latest'):
    """Fetches and processes leaderboard data for the given meeting key."""
    leaderboard = []
    for driver_number in driver_numbers:
        url = f"https://api.openf1.org/v1/position?meeting_key={meeting_key}&driver_number={driver_number}&session_key={meeting_key}"

        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))

            # Sort data in reverse chronological order (most recent first)
            data.sort(key=lambda item: item['date'], reverse=True) 

            if data: 
                leaderboard.append({
                    'driver_number': driver_number,
                    'position': data[0]['position']  # Take the first (latest) position 
                })
        except Exception as e:
            print(f"Error fetching data for driver {driver_number}: {e}")

    return leaderboard


count = 0
while True:
    count +=1

    # Fetch Updated Data (Using the latest meeting_key)
    leaderboard_data = get_leaderboard_data('latest')

    # Process and Display Leaderboard
    print("----- Leaderboard -----")

    # Sort leaderboard_data by the 'position' key
    leaderboard_data.sort(key=lambda item: item['position'])

    for index, entry in enumerate(leaderboard_data):
        driver_name = driver_names.get(entry['driver_number'], "Unknown Driver")
        print(f"{index + 1}  | {driver_name}")

    print("------------------")
    print(count)
    time.sleep(10) 
