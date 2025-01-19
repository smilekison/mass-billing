# Journey Billing Aggregator

This project is designed to calculate and aggregate billing amounts for users based on their journey data. It applies daily and monthly caps to the billing amounts and provides a detailed breakdown of costs per user. The system is modular, with separate components for loading data, calculating costs, aggregating bills, and writing the output.

## Table of Contents

1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [How It Works](#how-it-works)
4. [Usage](#usage)
5. [Input Files](#input-files)
6. [Output File](#output-file)
7. [Dependencies](#dependencies)
8. [Example](#example)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)

## Overview

The system processes journey data for users, calculates the cost of each journey based on the zones of the entry and exit stations, and aggregates the billing amounts while applying daily (\u00a315) and monthly (\u00a3100) caps. It also tracks daily billing amounts for each user and writes the results to an output file.

## File Structure

The project consists of the following files:

- `main.py`: The entry point of the application. It loads data, aggregates bills, and writes the output.
- `data_loader.py`: Handles loading station-to-zone mappings and journey data from CSV files.
- `billing_aggregator.py`: Aggregates billing amounts for each user, applies caps, and tracks daily breakdowns.
- `pricing_calculator.py`: Calculates the cost of a journey based on entry and exit zones.
- `output_writer.py`: Writes the aggregated billing information to a CSV file.
- `README.md`: This file, providing an overview of the project and instructions for use.

## How It Works

### Data Loading

- The `data_loader.py` module reads the station-to-zone mapping and journey data from CSV files.
- The journey data includes `user_id`, `station`, `direction` (IN or OUT), and `time`.

### Cost Calculation

- The `pricing_calculator.py` module calculates the cost of each journey based on the zones of the entry and exit stations.
- A base fee of \u00a32.00 is applied, with additional costs depending on the zones.

### Billing Aggregation

- The `billing_aggregator.py` module aggregates the billing amounts for each user.
- It applies daily (\u00a315) and monthly (\u00a3100) caps to the billing amounts.
- It also handles erroneous journeys (e.g., missing IN or OUT) by charging a flat fee of \u00a35.00.

### Output Writing

- The `output_writer.py` module writes the aggregated billing information to a CSV file.
- The output includes the total billing amount and a daily breakdown for each user.

## Usage

To run the project, use the following command:

```bash
python main.py <zone_map.csv> <journey_data.csv> <output.csv>
```

### Arguments

- `<zone_map.csv>`: Path to the CSV file containing station-to-zone mappings.
- `<journey_data.csv>`: Path to the CSV file containing journey data.
- `<output.csv>`: Path to the output CSV file where the billing information will be written.

## Input Files

### 1. Zone Map CSV (`zone_map.csv`)

This file maps each station to a zone. The format is as follows:

| station    | zone |
|------------|------|
| Station_A  | 1    |
| Station_B  | 2    |
| Station_C  | 3    |

### 2. Journey Data CSV (`journey_data.csv`)

This file contains the journey records for users. The format is as follows:

| user_id | station    | direction | time                |
|---------|------------|-----------|---------------------|
| 1       | Station_A  | IN        | 2023-10-01T08:00:00 |
| 1       | Station_B  | OUT       | 2023-10-01T08:30:00 |
| 2       | Station_C  | IN        | 2023-10-01T09:00:00 |

## Output File

The output file (`output.csv`) contains the aggregated billing information for each user. The format is as follows:

| user_id | total_billing_amount | daily_breakdown         |
|---------|-----------------------|-------------------------|
| 1       | 12.50                | 2023-10-01: \u00a312.50 |
| 2       | 5.00                 | 2023-10-01: \u00a35.00  |

- **`total_billing_amount`**: The total billing amount for the user after applying daily and monthly caps.
- **`daily_breakdown`**: A comma-separated list of dates and corresponding billing amounts for each day.

## Dependencies

The project requires Python 3.x and the following modules:

- `csv`: For reading and writing CSV files.
- `datetime`: For handling timestamps in the journey data.

No external libraries are required.

## Example

### Input Files

#### `zone_map.csv`:

| station    | zone |
|------------|------|
| Station_A  | 1    |
| Station_B  | 2    |
| Station_C  | 3    |

#### `journey_data.csv`:

| user_id | station    | direction | time                |
|---------|------------|-----------|---------------------|
| 1       | Station_A  | IN        | 2023-10-01T08:00:00 |
| 1       | Station_B  | OUT       | 2023-10-01T08:30:00 |
| 2       | Station_C  | IN        | 2023-10-01T09:00:00 |

### Command:

```bash
python main.py zone_map.csv journey_data.csv output.csv
```

### Output File (`output.csv`):

| user_id | total_billing_amount | daily_breakdown         |
|---------|-----------------------|-------------------------|
| 1       | 3.30                 | 2023-10-01: \u00a33.30  |
| 2       | 5.00                 | 2023-10-01: \u00a35.00  |
