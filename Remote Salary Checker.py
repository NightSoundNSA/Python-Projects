import math

# This code calculates salary conversions and tax deductions for remote work scenarios.
# Users can choose a currency and either use a predefined exchange rate or enter their own.

# Currency options and predefined exchange rates
exchange_rates = {
    "USD": 4.81,  # US Dollar to RON
    "EUR": 4.97,  # Euro to RON
    "HUF": 0.013,  # Hungarian Forint to RON
}

# Let the user choose a currency
print("Choose a currency: USD, EUR, or HUF")
currency = input("Enter currency (USD/EUR/HUF): ").upper()

# Check if the chosen currency is available
if currency in exchange_rates:
    use_custom_rate = input("Use the default exchange rate? (yes/no): ").lower()
    
    if use_custom_rate == "no":
        exchange_rate = float(input(f"Enter your own exchange rate for {currency} to RON: "))
    else:
        exchange_rate = exchange_rates[currency]
else:
    print("Invalid currency selected. Using USD as default.")
    currency = "USD"
    exchange_rate = exchange_rates["USD"]

# User input for yearly salary
salary = float(input(f"Enter your yearly salary in {currency}: "))

# Tax rate (adjust as needed)
tax_rate = 0.45

# Convert salary to RON
converted_salary = round(salary * exchange_rate, 2)

# Monthly salary before tax
monthly_salary = round(converted_salary / 12, 2)

# Monthly salary after tax
taxed_salary = round(monthly_salary * (1 - tax_rate), 2)

# Display results
print("\n=== Salary Calculation ===")
print(f"Converted Salary: {converted_salary} RON (from {salary} {currency})")
print(f"Monthly Salary (before tax): {monthly_salary} RON")
print(f"Monthly Salary (after tax): {taxed_salary} RON\n")

# Hourly Rate Calculation
hourly_rate = float(input(f"Enter your hourly rate in {currency}: "))
hours_per_day = 8  # Standard workday
work_days_per_month = 22  # Average working days per month

# Calculate earnings based on hours worked
daily_earnings = hourly_rate * hours_per_day
monthly_earnings = daily_earnings * work_days_per_month

print("\n=== Part-Time Salary Calculation ===")
print(f"Daily Earnings: {daily_earnings} {currency}")
print(f"Monthly Earnings (based on {work_days_per_month} workdays): {monthly_earnings} {currency}")
