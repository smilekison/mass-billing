from datetime import date
from pricing_calculator import calculate_journey_cost

def aggregate_bills(journeys, zone_map):
    """
    Aggregate journey costs for each user and apply daily and monthly caps.
    Track daily billing amounts for each user.

    Args:
        journeys (list): List of journey records (dictionaries with user_id, station, direction, time).
        zone_map (dict): Mapping of stations to their respective zones.

    Returns:
        dict: A dictionary where keys are user_ids and values are dictionaries containing
              total_amount, daily_amount, monthly_amount, and daily_breakdown.
    """
    # Dictionary to store billing information for each user
    user_bills = {}

    # Iterate through each journey record
    for journey in journeys:
        user_id = journey['user_id']

        # Initialize the user's billing record if it doesn't exist
        if user_id not in user_bills:
            user_bills[user_id] = {
                'total_amount': 0.0,  # Total billing amount for the user
                'daily_amount': 0.0,  # Daily billing amount for the user
                'monthly_amount': 0.0,  # Monthly billing amount for the user
                'current_entry': None,  # Tracks the current IN journey for the user
                'last_journey_date': None,  # Tracks the date of the last journey
                'daily_breakdown': {}  # Tracks daily billing amounts
            }

        # Get the user's billing record
        user_bill = user_bills[user_id]

        # Handle IN direction journeys
        if journey['direction'] == 'IN':
            # If there's already an IN without an OUT, charge £5.00 for the erroneous journey
            if user_bill['current_entry']:
                user_bill['total_amount'] += 5.00
                user_bill['daily_amount'] += 5.00
                user_bill['monthly_amount'] += 5.00

                # Update daily breakdown
                journey_date = journey['time'].date()
                if journey_date not in user_bill['daily_breakdown']:
                    user_bill['daily_breakdown'][journey_date] = 0.0
                user_bill['daily_breakdown'][journey_date] += 5.00

            # Set the current IN journey
            user_bill['current_entry'] = journey

        # Handle OUT direction journeys
        elif journey['direction'] == 'OUT':
            if user_bill['current_entry']:
                # Calculate the cost of the journey
                entry_station = user_bill['current_entry']['station']
                exit_station = journey['station']
                cost = calculate_journey_cost(zone_map, entry_station, exit_station)

                # Check if the date has changed (new day)
                journey_date = journey['time'].date()
                if user_bill['last_journey_date'] and journey_date != user_bill['last_journey_date']:
                    user_bill['daily_amount'] = 0.0  # Reset daily amount for the new day

                # Apply daily and monthly caps
                if user_bill['daily_amount'] + cost > 15.00:
                    cost = max(0, 15.00 - user_bill['daily_amount'])
                if user_bill['monthly_amount'] + cost > 100.00:
                    cost = max(0, 100.00 - user_bill['monthly_amount'])

                # Update billing amounts
                user_bill['total_amount'] += cost
                user_bill['daily_amount'] += cost
                user_bill['monthly_amount'] += cost

                # Update daily breakdown
                if journey_date not in user_bill['daily_breakdown']:
                    user_bill['daily_breakdown'][journey_date] = 0.0
                user_bill['daily_breakdown'][journey_date] += cost

                # Update the last journey date
                user_bill['last_journey_date'] = journey_date

                # Clear the current IN journey
                user_bill['current_entry'] = None
            else:
                # Handle erroneous journeys (missing IN)
                user_bill['total_amount'] += 5.00
                user_bill['daily_amount'] += 5.00
                user_bill['monthly_amount'] += 5.00

                # Update daily breakdown
                journey_date = journey['time'].date()
                if journey_date not in user_bill['daily_breakdown']:
                    user_bill['daily_breakdown'][journey_date] = 0.0
                user_bill['daily_breakdown'][journey_date] += 5.00

    # Handle any remaining incomplete journeys (IN without OUT)
    for user_bill in user_bills.values():
        if user_bill['current_entry']:
            user_bill['total_amount'] += 5.00
            user_bill['daily_amount'] += 5.00
            user_bill['monthly_amount'] += 5.00

            # Update daily breakdown
            journey_date = user_bill['current_entry']['time'].date()
            if journey_date not in user_bill['daily_breakdown']:
                user_bill['daily_breakdown'][journey_date] = 0.0
            user_bill['daily_breakdown'][journey_date] += 5.00

    return user_bills