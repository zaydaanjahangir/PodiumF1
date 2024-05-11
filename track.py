import fastf1
import numpy as np

# Load the session, ensuring data is loaded as well
session = fastf1.get_session(2024, 'Japan', 'Q')
session.load(telemetry=True)

circuit_info = session.get_circuit_info()
corners_df = circuit_info.corners

# Get telemetry data (using the fastest lap for example)
telemetry = session.laps.pick_fastest().get_telemetry()


def find_corner_end(corner_start_distance, telemetry_data, corner_threshold=10):
    """
    Finds the approximate end distance marker for a corner based on telemetry data.

    Args:
        corner_start_distance: The distance marker where the corner starts.
        telemetry_data: The telemetry data for the lap.
        corner_threshold: The distance threshold (in meters) used to determine the end of the corner.

    Returns:
        The approximate distance marker where the corner ends.
    """

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


# Iterate over the corners and find their start and end distances
for index, corner in corners_df.iterrows():
    corner_number = corner['Number']
    corner_letter = corner['Letter']
    corner_start_distance = corner['Distance']

    corner_end_distance = find_corner_end(corner_start_distance, telemetry)
    print(f"Corner {corner_number}{corner_letter}: Start - {corner_start_distance}m, End - {corner_end_distance}m")
