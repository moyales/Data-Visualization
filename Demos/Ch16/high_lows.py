import csv
# The above module parses lines in a CSV file and allows for 
# us to extract the necessary values.
from matplotlib import pyplot as plt

# Get high temps from the file.
filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)

    # print(header_row)
    # Shows what kind of info is in each line (displayed as a list)

    #for index, column_header in enumerate(header_row):
        # print(index, column_header)
        # Show the index of file_header data

# --------------------------------------------------------------
# Run this as a script in IDLE or ipython, not from VS Code.
# --------------------------------------------------------------