import fastf1
import numpy as np
import pandas as pd

# Load the session, ensuring data is loaded as well
session = fastf1.get_session(2024, 'Miami', 'R')
session.load(telemetry=True)

circuit_info = session.get_circuit_info()
corners_df = circuit_info.corners

def find_corner_end(corner_start_distance, telemetry_data, corner_threshold=10):
    # Filter telemetry data after the corner start
    telemetry_data_after_corner = telemetry_data.loc[telemetry_data['Distance'] > corner_start_distance]
    # Calculate distance differences between consecutive points
    distance_differences = telemetry_data_after_corner['Distance'].diff()
    # Find the index where the distance difference drops below the threshold (indicating the end of the corner)
    end_index = np.where(distance_differences < corner_threshold)[0]
    # If an index is found, return the corresponding distance
    if end_index.size > 0:
        return telemetry_data_after_corner['Distance'].iloc[end_index[0]]
    else:
        # If no index is found, return the last distance in telemetry (end of the track)
        return telemetry_data['Distance'].iloc[-1]

def get_corner_telemetry( corner_entry, corner_exit, telemetry_data):
    return telemetry_data.loc[(telemetry_data['Distance'] >= corner_entry) & (telemetry_data['Distance'] <= corner_exit)]

track_profile = {
    'slow_corners': ['turn_1', 'turn_8', 'turn_11', 'turn_12', 'turn_14', 'turn_15', 'turn_16', 'turn_17'],
    'fast_corners': ['turn_2', 'turn_3', 'turn_4', 'turn_5', 'turn_6', 'turn_7', 'turn_9', 'turn_10', 'turn_13'],
}

drivers = ['4', '1', '16', '11', '55', '44', '22', '63', '14', '31', '27', '10', '81', '24', '3', '77', '18', '23', '20', '2']
# Dictionary to store results for all drivers
all_drivers_data = {}

# Iterate over drivers
for driver in drivers:
    # Get telemetry data for the current driver.
    driver_laps = session.laps.pick_driver(driver)
    driver_telemetry = driver_laps.get_telemetry()  # Get telemetry for just this driver's laps

    # Create a dictionary for corner entry and exit distances
    corner_distances = {}
    for index, corner in corners_df.iterrows():
        corner_name = f"turn_{corner['Number']}{corner['Letter']}"
        corner_distances[corner_name] = {
            "entry": corner['Distance'],
            "exit": find_corner_end(corner['Distance'], driver_telemetry)
        }

    # Create a dictionary to store average speeds for this driver
    corner_type_avg_speeds = {
        'slow_corners': [],
        'fast_corners': []
    }

    # Loop through corners and calculate average speeds
    for corner_name, distances in corner_distances.items():
        corner_telemetry = get_corner_telemetry(distances['entry'], distances['exit'], driver_telemetry)
        if not corner_telemetry.empty:  # Check if telemetry data exists
            avg_speed = corner_telemetry['Speed'].mean()
            for corner_type, corners in track_profile.items():
                if corner_name in corners:
                    corner_type_avg_speeds[corner_type].append(avg_speed)
                    break
        else:
            # Handle cases where no telemetry data is available
            for corner_type, corners in track_profile.items():
                if corner_name in corners:
                    corner_type_avg_speeds[corner_type].append(np.nan)
                    break

    # Calculate average speeds for each type, excluding NaN values
    for corner_type, speeds in corner_type_avg_speeds.items():
        valid_speeds = [speed for speed in speeds if not pd.isna(speed)]
        if valid_speeds:
            avg_speed = sum(valid_speeds) / len(valid_speeds)
            corner_type_avg_speeds[corner_type] = avg_speed
        else:
            corner_type_avg_speeds[corner_type] = np.nan
    # Store the results for the current driver
    all_drivers_data[driver] = corner_type_avg_speeds

# Create a DataFrame from the results
results_df = pd.DataFrame(all_drivers_data).transpose()
# Export to CSV
results_df.drop(columns=['medium_corners'], errors='ignore', inplace=True)  # Drop if it exists
results_df.to_csv("corners.csv")
