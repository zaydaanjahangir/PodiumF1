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

turn_1_entry = 706.6451251521764
turn_1_exit = 722.031111111111
turn_2_entry = 823.7483786060384
turn_2_exit = 835.0956221068886
turn_3_entry = 1071.506075767782
turn_3_exit = 1102.6209578863834
turn_4_entry = 1211.1057882534876
turn_4_exit = 1234.0657647131866
turn_5_entry = 1357.2393008143877
turn_5_exit = 1379.5038888888882
turn_6_entry = 1527.8592545492193
turn_6_exit = 1541.563925899424
turn_7_entry = 1843.0659718839352
turn_7_exit = 1874.3439953421162
turn_8_entry = 2263.012911281292
turn_8_exit = 2276.488570730334
turn_9_entry = 2416.451873337459
turn_9_exit = 2428.8574999999983
turn_10_entry = 2727.266361062603
turn_10_exit = 2744.9737040363943
turn_11_entry = 2883.8254592312824
turn_11_exit = 2889.6130555555546
turn_12_entry = 3135.106724571304
turn_12_exit = 3156.995403427153
turn_13_entry = 3758.3316936640317
turn_13_exit = 3786.039722222221
turn_14_entry = 3925.792449201479
turn_14_exit = 3939.979444444443
turn_15_entry = 4960.519768491383
turn_15_exit = 4985.434239774502
turn_16_entry = 5347.343253964975
turn_16_exit = 5351.6353808055965
turn_17_entry = 5399.581762146599
turn_17_exit = 5408.41287999769
turn_18_entry = 5572.951764006372
turn_18_exit = 5585.344166666664

def get_corner_telemetry( corner_entry, corner_exit, telemetry_data=all_laps_telemetry):
    return telemetry_data.loc[(telemetry_data['Distance'] >= corner_entry) & (telemetry_data['Distance'] <= corner_exit)]

turn_1_telemetry = get_corner_telemetry(turn_1_entry, turn_1_exit)
turn_2_telemetry = get_corner_telemetry(turn_2_entry, turn_2_exit)
turn_3_telemetry = get_corner_telemetry(turn_3_entry, turn_3_exit)
turn_4_telemetry = get_corner_telemetry(turn_4_entry, turn_4_exit)
turn_5_telemetry = get_corner_telemetry(turn_5_entry, turn_5_exit)
turn_6_telemetry = get_corner_telemetry(turn_6_entry, turn_6_exit)
turn_7_telemetry = get_corner_telemetry(turn_7_entry, turn_7_exit)
turn_8_telemetry = get_corner_telemetry(turn_8_entry, turn_8_exit)
turn_9_telemetry = get_corner_telemetry(turn_9_entry, turn_9_exit)
turn_10_telemetry = get_corner_telemetry(turn_10_entry, turn_10_exit)
turn_11_telemetry = get_corner_telemetry(turn_11_entry, turn_11_exit)
turn_12_telemetry = get_corner_telemetry(turn_12_entry, turn_12_exit)
turn_13_telemetry = get_corner_telemetry(turn_13_entry, turn_13_exit)
turn_14_telemetry = get_corner_telemetry(turn_14_entry, turn_14_exit)
turn_15_telemetry = get_corner_telemetry(turn_15_entry, turn_15_exit)
turn_16_telemetry = get_corner_telemetry(turn_16_entry, turn_16_exit)
turn_17_telemetry = get_corner_telemetry(turn_17_entry, turn_17_exit)
turn_18_telemetry = get_corner_telemetry(turn_18_entry, turn_18_exit)

ver_min_speed_turn_1 = turn_1_telemetry['Speed'].min()
ver_min_speed_turn_2 = turn_2_telemetry['Speed'].min()
ver_min_speed_turn_3 = turn_3_telemetry['Speed'].min()
ver_min_speed_turn_4 = turn_4_telemetry['Speed'].min()
ver_min_speed_turn_5 = turn_5_telemetry['Speed'].min()
ver_min_speed_turn_6 = turn_6_telemetry['Speed'].min()
ver_min_speed_turn_7 = turn_7_telemetry['Speed'].min()
ver_min_speed_turn_8 = turn_8_telemetry['Speed'].min()
ver_min_speed_turn_9 = turn_9_telemetry['Speed'].min()
ver_min_speed_turn_10 = turn_10_telemetry['Speed'].min()
ver_min_speed_turn_11 = turn_11_telemetry['Speed'].min()
ver_min_speed_turn_12 = turn_12_telemetry['Speed'].min()
ver_min_speed_turn_13 = turn_13_telemetry['Speed'].min()
ver_min_speed_turn_14 = turn_14_telemetry['Speed'].min()
ver_min_speed_turn_15 = turn_15_telemetry['Speed'].min()
ver_min_speed_turn_16 = turn_16_telemetry['Speed'].min()
ver_min_speed_turn_17 = turn_17_telemetry['Speed'].min()
ver_min_speed_turn_18 = turn_18_telemetry['Speed'].min()

ver_avg_speed_turn_1 = turn_1_telemetry['Speed'].mean()
ver_avg_speed_turn_2 = turn_2_telemetry['Speed'].mean()
ver_avg_speed_turn_3 = turn_3_telemetry['Speed'].mean()
ver_avg_speed_turn_4 = turn_4_telemetry['Speed'].mean()
ver_avg_speed_turn_5 = turn_5_telemetry['Speed'].mean()
ver_avg_speed_turn_6 = turn_6_telemetry['Speed'].mean()
ver_avg_speed_turn_7 = turn_7_telemetry['Speed'].mean()
ver_avg_speed_turn_8 = turn_8_telemetry['Speed'].mean()
ver_avg_speed_turn_9 = turn_9_telemetry['Speed'].mean()
ver_avg_speed_turn_10 = turn_10_telemetry['Speed'].mean()
ver_avg_speed_turn_11 = turn_11_telemetry['Speed'].mean()
ver_avg_speed_turn_12 = turn_12_telemetry['Speed'].mean()
ver_avg_speed_turn_13 = turn_13_telemetry['Speed'].mean()
ver_avg_speed_turn_14 = turn_14_telemetry['Speed'].mean()
ver_avg_speed_turn_15 = turn_15_telemetry['Speed'].mean()
ver_avg_speed_turn_16 = turn_16_telemetry['Speed'].mean()
ver_avg_speed_turn_17 = turn_17_telemetry['Speed'].mean()
ver_avg_speed_turn_18 = turn_18_telemetry['Speed'].mean()

track_profile = {
    'slow_corners': ['turn_2', 'turn_11', 'turn_16'],
    'medium_corners': ['turn_3', 'turn_5', 'turn_7', 'turn_8', 'turn_10'],
    'fast_corners': ['turn_1', 'turn_4', 'turn_6', 'turn_9', 'turn_12', 'turn_13', 'turn_14', 'turn_15', 'turn_17', 'turn_18'],
}
# Create dictionaries to store average speeds for each corner type
ver_slow_corner_avg_speeds = {}
ver_medium_corner_avg_speeds = {}
ver_fast_corner_avg_speeds = {}

# Populate dictionaries
for corner_name in track_profile['slow_corners']:
    ver_slow_corner_avg_speeds[corner_name] = globals()["ver_avg_speed_" + corner_name]

for corner_name in track_profile['medium_corners']:
    ver_medium_corner_avg_speeds[corner_name] = globals()["ver_avg_speed_" + corner_name]

for corner_name in track_profile['fast_corners']:
    ver_fast_corner_avg_speeds[corner_name] = globals()["ver_avg_speed_" + corner_name]

# Calculate average speeds for each type
ver_avg_slow_corner_speed = sum(ver_slow_corner_avg_speeds.values()) / len(ver_slow_corner_avg_speeds)
ver_avg_medium_corner_speed = sum(ver_medium_corner_avg_speeds.values()) / len(ver_medium_corner_avg_speeds)
ver_avg_fast_corner_speed = sum(ver_fast_corner_avg_speeds.values()) / len(ver_fast_corner_avg_speeds)

# Filter out NaN values before calculating the sum
valid_fast_corner_speeds = [speed for speed in ver_fast_corner_avg_speeds.values() if not np.isnan(speed)]
ver_avg_fast_corner_speed = sum(valid_fast_corner_speeds) / len(valid_fast_corner_speeds)

print(f"Verstappen's Average Speeds:")
print(f"  Slow Corners: {ver_avg_slow_corner_speed:.2f} km/h")
print(f"  Medium Corners: {ver_avg_medium_corner_speed:.2f} km/h")
print(f"  Fast Corners: {ver_avg_fast_corner_speed:.2f} km/h")

