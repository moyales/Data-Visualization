import csv
# The above module parses lines in a CSV file and allows for 
# us to extract the necessary values.
from datetime import datetime
# A module to help format dates and times as one pleases.

from matplotlib import pyplot as plt

# Get dates, high, and low temps from the file.
filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)

    # print(header_row)
    # Shows what kind of info is in each line (displayed as a list)

    #for index, column_header in enumerate(header_row):
        # print(index, column_header)
        # Show the index of file_header data

    # Plot data.
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    title = "Daily High & Low Temps. - 2014\nDeath Valley, CA"
    plt.title(title, fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temp. (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# --------------------------------------------------------------
# Run this as a script in IDLE or ipython, not from VS Code.
# --------------------------------------------------------------