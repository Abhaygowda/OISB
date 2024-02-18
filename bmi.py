w=float(input("Enter your Weight in kg: "))
h= float(input("Enter Your Height in meters: "))

BMI = w/(h*h)

print(BMI)
if (BMI<25):
    print("Normal weight")
elif (25<BMI<30):
    print("Overweight")
else:
    print("Obesity")