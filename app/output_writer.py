import csv

def write_output(file_path, user_bills):
    """
    Write user billing amounts to a CSV file, including daily breakdown.

    Args:
        file_path (str): Path to the output CSV file.
        user_bills (dict): A dictionary containing billing information for each user.
    """
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['user_id', 'total_billing_amount', 'daily_breakdown'])

        # Iterate through each user's billing information
        for user_id, user_bill in sorted(user_bills.items()):
            # Format daily breakdown as a string
            daily_breakdown = ', '.join(
                [f"{date}: £{amount:.2f}" for date, amount in sorted(user_bill['daily_breakdown'].items())]
            )
            # Write the user's billing information to the CSV file
            writer.writerow([user_id, f"{user_bill['total_amount']:.2f}", daily_breakdown])