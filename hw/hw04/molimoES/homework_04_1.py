# Homework Lesson 04

# ///////////////////////////////////////////////////////////////////
# 1 - Temperature converter
print("Subtask 1")

temp_c = int(input("Enter the temperature in Celsius: "))

if temp_c < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    temp_f = (temp_c * 9 / 5) + 32
    print(f"{temp_c}°C is equivalent to {temp_f}°F")
