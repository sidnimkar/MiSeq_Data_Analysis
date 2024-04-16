import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to the CSV file
csv_file_path = 'P50KNNS_enrichment.csv'  # Change to the path of your CSV file

# Read the data from the CSV file into a DataFrame
data_frame = pd.read_csv(csv_file_path)

# Extract the categories and values from the DataFrame
# Assuming the first column is categories and the third column is values
categories = data_frame.iloc[:, 0]
values = data_frame.iloc[:, 2]

# Create the bar graph
plt.bar(categories, values)  # Use categories for x-ticks directly

# Set the x-axis labels to the categories from the CSV file
plt.xticks(categories, ['K', 'R', 'E', 'D', 'N', 'Q', 'H', 'T', 'S', 'C', 'A', 'V', 'L', 'I', 'M', 'F', 'Y', 'W', 'G', 'P', '*'])

# Add labels and title
plt.xlabel('Amino Acid')
plt.ylabel('Enrichment Values')
plt.title('F91M')

# Fix the y-axis between -2 and 2
plt.ylim(-2, 2)

# Display the bar graph with grid
plt.grid(True)

# Show the plot
plt.show()