import pandas as pd
import sys

def print_unique_values_with_counts_grouped(csv_file, genus_column, species_column=None):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # If species_column is provided, group by both "genus" and "species" columns
    if species_column:
        grouped_columns = [genus_column, species_column]
    else:
        # If species_column is not provided, group only by "genus" column
        grouped_columns = [genus_column]

    # Group the DataFrame and count occurrences
    grouped_counts = df.groupby(grouped_columns).size().reset_index(name='count')

    # Print unique values and their counts grouped by specified column(s)
    print(f"Unique values and their counts grouped by {genus_column}{' and ' + species_column if species_column else ''}:")
    for index, row in grouped_counts.iterrows():
        key = f"{row[genus_column]}"
        if species_column:
            key += f" - {row[species_column]}"
        print(f"{key}: {row['count']}")

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python script.py <csv_file> <genus_column> [species_column]")
        sys.exit(1)

    # Get CSV file path and genus column name from command-line arguments
    csv_file = sys.argv[1]
    genus_column = sys.argv[2]
    species_column = sys.argv[3] if len(sys.argv) == 4 else None

    # Call the function to print unique values and their counts grouped by genus and optionally species
    print_unique_values_with_counts_grouped(csv_file, genus_column, species_column)
