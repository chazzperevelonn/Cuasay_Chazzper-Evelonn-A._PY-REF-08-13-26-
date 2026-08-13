import math

print("--- Task 1: Angle Explorer ---")
angle_degrees = 60

# TODO: convert angle_degrees to radians using the math module
angle_radians = math.radians(angle_degrees)

# TODO: print the radians value, rounded to 4 decimal places,
#       labeled exactly:  "Angle in radians:"
print(f"Angle in radians: {angle_radians:.4f}")

# TODO: print the sine of angle_radians, rounded to 4 decimals,
#       labeled exactly:  "sin ->"
print(f"sin -> {math.sin(angle_radians):.4f}")

# TODO: print the cosine of angle_radians, rounded to 4 decimals,
#       labeled exactly:  "cos ->"
print(f"cos -> {math.cos(angle_radians):.4f}")

# TODO: print the tangent of angle_radians, rounded to 4 decimals,
#       labeled exactly:  "tan ->"
print(f"tan -> {math.tan(angle_radians):.4f}")

print()
