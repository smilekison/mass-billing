import csv
from datetime import datetime

def load_zone_map(file_path):
    """
    Load station to zone mapping from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing station-to-zone mappings.

    Returns:
        dict: A dictionary where keys are station names and values are zone numbers.
    """
    zone_map = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            zone_map[row['station']] = int(row['zone'])
    return zone_map

def load_journey_data(file_path):
    """
    Load journey data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing journey data.

    Returns:
        list: A list of dictionaries, where each dictionary represents a journey.
    """
    journeys = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Parse the timestamp using the correct format
            try:
                time = datetime.strptime(row['time'], '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                # Fallback to another format if needed
                time = datetime.strptime(row['time'], '%Y-%m-%d %H:%M:%S')
            journeys.append({
                'user_id': row['user_id'],
                'station': row['station'],
                'direction': row['direction'],
                'time': time
            })
    return journeys