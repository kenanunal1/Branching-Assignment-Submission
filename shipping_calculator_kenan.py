# Package Express Shipping Cost Calculator
# Developer: Lisa Thompson
# Version: 2.1.0

# Show program introduction
print("Welcome to Package Express. Please follow the instructions below.")

# Collect package weight
weight_value = float(input("Please enter the package weight:\n"))

# Weight validation
if weight_value > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Get package dimensions
dimension_w = float(input("Please enter the package width:\n"))
dimension_h = float(input("Please enter the package height:\n"))
dimension_l = float(input("Please enter the package length:\n"))

# Sum of all dimensions
total_size = dimension_w + dimension_h + dimension_l

# Size validation
if total_size > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping cost
# Cost formula: (width * height * length * weight) / 100
final_cost = (dimension_w * dimension_h * dimension_l * weight_value) / 100

# Display shipping cost
print(f"Your estimated total for shipping this package is: ${final_cost:.2f}")
print("Thank you!") 