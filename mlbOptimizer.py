import csv

# Path to your CSV file
file_path = '/Users/philculver/CodeProjects/mlbOptimizer/fangraphs-leaderboards.csv'

# Open the file and read its content
with open(file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    # Optional: Capture the header row if you want to use it to reference columns by name
    headers = next(csv_reader)

    # Initialize an empty list to store your data (if needed)
    players_data = []

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # You can access each column by index. For example:
        # player_name = row[0] assuming the player's name is in the first column

        # Process your row here (e.g., filtering based on certain criteria, extracting specific fields)
        # Example: Add the row to your list if it meets certain conditions
        players_data.append(row)

        # If you want to print or process specific rows, insert your logic here

    # Do something with the processed data
    print(players_data[:5])  # Example: Print first 5 rows for checking
