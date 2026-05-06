# Remember the format() function we used in the last video?? Now pass 145 and
# ‘o’ in the function and see what it returns. Try to find out which representation it is.
# There is a circular pond in a village. This pond has a radius of 84 meters.
# Can you find the area of the pond? (Bonus: If there is exactly 1.4 liter of water in a square meter,
# what is the total amount of water in the pond?)

print(format(145,'o'))

# The  above will print 221
# | Division step | Quotient | Remainder |
# | ------------- | -------- | --------- |
# | 145 ÷ 8       | 18       | **1**     |
# | 18 ÷ 8        | 2        | **2**     |
# | 2 ÷ 8         | 0        | **2**     |
# 145₁₀ = 221₈
# 221 to base 8 = (2×82)+(2×81)+(1×80)
#              = (2×64)+(2×8)+(1×1)
#              = 128+16+1=145


# Find area of Circle.
pond_radius = 84
pi_val = 22/7
area_of_pond = pi_val * pond_radius * pond_radius
print(str(area_of_pond) + " Meters")

# 3. If you cross a 490-meter-long street in 7 minutes, then what is your speed in meters per second?
# Print your answer without any decimal point in it.
distance = 490
time = 7
speed = distance / time
print(str(speed) + " m/min")
