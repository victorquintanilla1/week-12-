# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temperature = int(input("Is it hot or cold outside"))
if temperature >= 100:
    print("Extreme temperature warning")

elif 85 <= temperature <= 90:
    print("It is hot outside")
elif 70 <= temperature <= 80:
    print("It is nice outside")
elif 60 <= temperature <= 70:
    print("It is chilly outside")
   
else:
    print("It is cold outside")
