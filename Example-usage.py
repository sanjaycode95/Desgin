import tableframe as ta

# Initialize table with row and column labels
table =ta.creatTable("Marks", ["Math", "Science"], ["Alice", "Bob"])

# Insert single data point
table.insert_data("Math", "Alice", 85)

# Insert full row of values
table.insert_datalist("Bob", [90, 75])

# Display data for one label
table.show_datalist("Math")

# Print full table
print(table)

# Get sum or average for a label
print("Sum of Alice:", table.sum("Alice"))
print("Average of Math:", table.average("Math"))
