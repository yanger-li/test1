weight, height, BMI = 0, 0, 0

print("Enter the weight: ")
weight = eval(input())

print("Enter the height: ")
height = eval(input())

# print("Enter the weight in pounds and then the height in inches, ")
# print("seperate the two inputs using a comma: ", weight, ",", height)

converting = 703
BMI = (weight * converting)/(height * height)

print('The BMI is', BMI)



for x in range(0,10):
	print('testing', x)


