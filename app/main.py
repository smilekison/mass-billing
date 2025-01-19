import sys
from data_loader import load_zone_map, load_journey_data
from billing_aggregator import aggregate_bills
from output_writer import write_output

def main(zone_map_path, journey_data_path, output_path):
    """
    Main function to load data, aggregate bills, and write output.

    Args:
        zone_map_path (str): Path to the CSV file containing station-to-zone mappings.
        journey_data_path (str): Path to the CSV file containing journey data.
        output_path (str): Path to the output CSV file where billing information will be written.
    """
    # Load input data
    zone_map = load_zone_map(zone_map_path)
    journeys = load_journey_data(journey_data_path)

    # Aggregate bills
    user_bills = aggregate_bills(journeys, zone_map)

    # Write output
    write_output(output_path, user_bills)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python main.py <zone_map.csv> <journey_data.csv> <output.csv>")
        sys.exit(1)

    # Parse command-line arguments
    zone_map_path = sys.argv[1]
    journey_data_path = sys.argv[2]
    output_path = sys.argv[3]

    # Run the main function
    main(zone_map_path, journey_data_path, output_path)