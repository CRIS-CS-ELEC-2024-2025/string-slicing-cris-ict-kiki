'''
<Kiki>, <Grade 10> <Intro to Computer Science>
Assignment: String Slicing
This assignment will demonstrate how to manipulate and print strings.
'''

# DO NOT EDIT THIS LINE
country = "the united states of america"

# 1. print the country in *lower case*
print("the united states of america".lower())

# 2. print country in *title case*
print(country.title())

# 3. print country in *upper case*
print(country.upper())

# 4. print the length of the country string as:
#    string length of country: <length>
print(f"string length of country: {(len(country))}")

# 5. slice the string "america" from country, upper case the 'a',
#    and store it in a variable named `short_name` with a value "America"
short_name = country[21:28].title()
print(short_name)

# 6. concantentate a string value with `short_name` to
#    produce the name of the continent where the country resides
#    and print the result:
#    <title case country> is located within <title case continent>
continent = "north america"
print(f"{short_name} is located within {continent.title()}")

# 7. print a statement how we refer to people from the country:
#    People from <title case country> are called <title case of people in plural>
print(f"People from {country.title()} are called {short_name.title()}" + "ns")
