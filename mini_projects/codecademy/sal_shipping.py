# 31/12/2024
# Shipping Cost Project from Codecademy Course
# intended only to practice if statement blocks

weight = 1.5
premium_flat_rate = 125
# Ground Shipping
if weight <= 2:
  print(weight*1.5 + 20)
elif weight <= 6:
  print(weight*3 + 20)
elif weight <= 10:ff
  print(weight*4 + 20)
else:
  print(weight*10 + 20)

print("Premium Flat Rate: " + str(premium_flat_rate))

# Drone Shipping
if weight <= 2:
  print(weight*4.5)
elif weight <= 6:
  print(weight*9)
elif weight <= 10:
  print(weight*12)
else:
  print(weight*14.25)


