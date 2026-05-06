#
# 1. Write a program that can tell you your BMI Category.
#   Ask user to enter height in Meter
#   Ask user to enter weight in KG
#   Calculate the BMI(Body Mass Index) = weight /(height)**2 and store it in a variable
#
#   If the BMI is 30 or greater, print “Obesity”
#
#   If the BMI is in between 25 and 29, print “Overweight”
#
#   If the BMI is in between 18.5 and 25, print “Normal”
#
#   If the BMI is less than 18.5, print “Underweight”
#
# 2. Using the following list of cities per country,
#
#   India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
#   USA = ["New York","Chicago","Las Vegas", "San Francisco"]
#   UK = ["London", "Manchester", "Liverpool", "Nottingham"]
#   Write a program that asks the user to enter a city name, and it should tell which country the city belongs to
#
#   Write a program that asks users to enter two cities, and it tells you if they both are in the same country or nor />
#   For example:
#   If I enter Mumbai and Chennai, it will print "Both cities are in India" but if I enter Mumbai and New York it should print "They don't belong to the same country"
#

height = input(" Enter Height in meters:")
weight = input(" Enter weight in Kgs:")

#Calculate the BMI(Body Mass Index) = weight /(height)**2 and store it in a variable
BMI = float(weight) / float(height) ** 2
print(BMI)
if BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You are normal")
elif BMI < 30:
    print("You are Overweight")
elif BMI >= 30:
    print("You are obese")


India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

def get_country(city):
    if city in India:
        return "India"
    elif city in USA:
        return "USA"
    elif city in UK:
        return "UK"
    else:
        return None
# Task 1: Single city lookup
city = input("Enter a city name: ").strip().title()
country = get_country(city)

if country:
    print(f"{city} is in {country}")
else:
    print(f"I don't know which country {city} belongs to.")

# Task 2: Two city comparison
city1 = input("\nEnter the first city: ").strip().title()
city2 = input("Enter the second city: ").strip().title()

country1 = get_country(city1)
country2 = get_country(city2)

if country1 and country2 and country1 == country2:
    print(f"Both cities are in {country1}")
elif country1 and country2:
    print("They don't belong to the same country")
else:
    print("One or both cities are not in my database.")

