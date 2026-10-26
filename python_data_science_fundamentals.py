"""
Python & Data Science Fundamentals
Internship Task - Beginner Practice File

How to run:
1. Install Python from https://www.python.org/downloads/ OR open Google Colab:
   https://colab.research.google.com/
2. To use Jupyter Notebook, install it with: python -m pip install notebook
   Then run: jupyter notebook
3. Save this file as python_data_science_fundamentals.py and run:
   python python_data_science_fundamentals.py

This beginner script demonstrates:
- Variables and basic data types
- Lists and dictionaries
- Loops and functions
- Writing and reading a text file
- A simple data-science calculation and real-world application
"""

# 1. VARIABLES AND BASIC DATA TYPES
print("\n=== 1. Variables and Data Types ===")
intern_name = "Intern"
course = "Python & Data Science"
days_completed = 5
completion_rate = 80.0
is_learning = True

print("Name:", intern_name)
print("Course:", course)
print("Days completed:", days_completed)
print("Completion rate:", completion_rate, "%")
print("Currently learning:", is_learning)


# 2. LISTS
print("\n=== 2. Lists ===")
daily_sales = [1200, 1500, 900, 1800, 1600]
print("Daily sales:", daily_sales)
print("First day's sales:", daily_sales[0])
print("Number of days:", len(daily_sales))


# 3. LOOPS
print("\n=== 3. Loops ===")
for day, sales in enumerate(daily_sales, start=1):
    print("Day", day, "- Sales: ₹", sales)

total_sales = 0
for sales in daily_sales:
    total_sales += sales
print("Total sales: ₹", total_sales)


# 4. FUNCTIONS
print("\n=== 4. Functions ===")
def calculate_average(numbers):
    """Return the average of a list of numbers."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

average_sales = calculate_average(daily_sales)
print("Average daily sales: ₹", round(average_sales, 2))


# 5. DICTIONARIES
print("\n=== 5. Dictionaries ===")
sales_summary = {
    "total_sales": total_sales,
    "average_sales": round(average_sales, 2),
    "best_day_sales": max(daily_sales),
    "days_recorded": len(daily_sales)
}
for key, value in sales_summary.items():
    print(key, ":", value)


# 6. FILE HANDLING
print("\n=== 6. File Handling ===")
file_name = "internship_sales_report.txt"

# Write the summary to a text file.
with open(file_name, "w", encoding="utf-8") as file:
    file.write("Python & Data Science Fundamentals - Sales Report\n")
    file.write("-----------------------------------------------\n")
    for key, value in sales_summary.items():
        file.write(f"{key}: {value}\n")

print("Report saved to:", file_name)

# Read the report back from the file.
with open(file_name, "r", encoding="utf-8") as file:
    print("\nReport contents:")
    print(file.read())


# 7. BASIC DATA SCIENCE CONCEPTS
print("\n=== 7. Basic Data Science ===")
print("Data Science uses data to find patterns and support decisions.")
print("Example application: A shop can study sales to identify its best-selling days.")
print("Dataset:", daily_sales)
print("Minimum sales: ₹", min(daily_sales))
print("Maximum sales: ₹", max(daily_sales))
print("Average sales: ₹", round(average_sales, 2))

print("\nPractice complete! Try changing the sales values and run the file again.")
