def calculate_journey_cost(zone_map, entry_station, exit_station):
    """
    Calculate the cost of a journey based on entry and exit zones.

    Args:
        zone_map (dict): Mapping of stations to their respective zones.
        entry_station (str): The station where the journey starts.
        exit_station (str): The station where the journey ends.

    Returns:
        float: The total cost of the journey.
    """
    base_fee = 2.00  # Base fee for any journey
    entry_zone = zone_map.get(entry_station, 0)  # Get the zone of the entry station
    exit_zone = zone_map.get(exit_station, 0)  # Get the zone of the exit station

    # Additional costs based on zones
    additional_costs = {
        1: 0.80,
        2: 0.50,
        3: 0.50,
        4: 0.30,
        5: 0.30,
        6: 0.10,
        7: 0.10
    }

    # Get the additional cost for the entry and exit zones
    entry_cost = additional_costs.get(entry_zone, 0.10)
    exit_cost = additional_costs.get(exit_zone, 0.10)

    # Calculate the total cost of the journey
    return base_fee + entry_cost + exit_cost