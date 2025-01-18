column1 = input('Enter the title for column 1 (20 characters max): ')[:20]

column2 = input('Enter the title for column 2 (20 characters max): ')[:20]

column3 = input('Enter the title for column 3 (20 characters max): ')[:20]

print("\nNow, enter the data for the table rows:")

row1_column1 = input(f"Enter the value for {column1}: ")[:20]

row1_column2 = input(f"Enter the value for {column2}: ")[:20]

row1_column3 = input(f"Enter the value for {column3}: ")[:20]

row2_column1 = input(f"Enter another value for {column1}: ")[:20]

row2_column2 = input(f"Enter another value for {column2}: ")[:20]

row2_column3 = input(f"Enter another value for {column3}: ")[:20]

print("\nFormatted Table:")
print("-" * 64)
print(f"{column1:<20} | {column2:<20} | {column3:<20}")
print("-" * 64)
print(f"{row1_column1:<20} | {row1_column2:<20} | {row1_column3:<20}")
print(f"{row2_column1:<20} | {row2_column2:<20} | {row2_column3:<20}")
print("-" * 64)
