# This function converts miles to kilometers (km).
# Complete the function to return the result of the conversion
# Call the function to convert the trip distance from miles to kilometers
# Fill in the blank to print the result of the conversion
# Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result


def convert_distance(miles):
    km = miles * 1.6
    return km


my_trip_miles = 55

my_trip_km = convert_distance(my_trip_miles)

print("The distance in kilometers is " + str(my_trip_km))

print("The round-trip in kilometers is", my_trip_km * 2)
