import fastf1
import numpy as np

# Load the session, ensuring data is loaded as well
session = fastf1.get_session(2024, 'Japan', 'Q')
session.load(telemetry=True)

circuit_info = session.get_circuit_info()
corners_df = circuit_info.corners
all_laps_telemetry = session.laps.pick_driver('VER').get_telemetry()

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

# # Iterate over the corners and find their start and end distances
# for index, corner in corners_df.iterrows():
#     corner_number = corner['Number']
#     corner_letter = corner['Letter']
#     corner_start_distance = corner['Distance']
#
#     corner_end_distance = find_corner_end(corner_start_distance, telemetry)
#     print(f"Corner {corner_number}{corner_letter}: Start - {corner_start_distance}m, End - {corner_end_distance}m")

track_profile = {
    'slow_corners': ['turn_2', 'turn_11', 'turn_16'],
    'medium_corners': ['turn_3', 'turn_5', 'turn_7', 'turn_8', 'turn_10'],
    'fast_corners': ['turn_1', 'turn_4', 'turn_6', 'turn_9', 'turn_12', 'turn_13', 'turn_14', 'turn_15', 'turn_17', 'turn_18'],
}
def get_corner_telemetry( corner_entry, corner_exit, telemetry_data=all_laps_telemetry):
    return telemetry_data.loc[(telemetry_data['Distance'] >= corner_entry) & (telemetry_data['Distance'] <= corner_exit)]

# Create a dictionary for corner entry and exit distances
corner_distances = {}
for index, corner in corners_df.iterrows():
    corner_name = f"turn_{corner['Number']}{corner['Letter']}"
    corner_distances[corner_name] = {
        "entry": corner['Distance'],
        "exit": find_corner_end(corner['Distance'], all_laps_telemetry)
    }

# Create a dictionary to store average speeds for each corner type
corner_type_avg_speeds = {
    'slow_corners': [],
    'medium_corners': [],
    'fast_corners': []
}

# Loop through corners and calculate average speeds
for corner_name, distances in corner_distances.items():
    corner_telemetry = get_corner_telemetry(distances['entry'], distances['exit'])
    avg_speed = corner_telemetry['Speed'].mean()

    # Add average speed to the appropriate list based on corner type
    for corner_type, corners in track_profile.items():
        if corner_name in corners:
            corner_type_avg_speeds[corner_type].append(avg_speed)
            break  # Exit loop once the corner type is found

# Calculate average speeds for each corner type, excluding NaN values
for corner_type, speeds in corner_type_avg_speeds.items():
    valid_speeds = [speed for speed in speeds if not np.isnan(speed)]
    avg_speed = sum(valid_speeds) / len(valid_speeds)
    print(f"Verstappen's Average Speed in {corner_type}: {avg_speed:.2f} km/h")

