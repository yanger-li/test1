
import sys
def main():
	bags_ordered, box_used_large, box_used_medium, box_used_small, remainder = 0, 0, 0, 0, 0
	discount_rate, coffee_cost, box_cost, total_cost = 0.0, 0.0, 0.0, 0.0

	RATE1, RATE2, RATE3, TATE4, RATE5, RATE6, RATE7 = 0.0, 0.05, 0.08, 0.10, 0.12, 0.15, 0.20
	BAG1, BAG2, BAG3, BAG4, BAG5, BAG6, BAG7 = 0, 25, 50, 100, 150, 200, 300
	BOX1, BOX2, BOX3 = 2.00, 1.50, 0.80
	PRICE = 8.50

	print("Enter the number of bags ordered: ", end="")
	bags_ordered = eval(input())

	if (bags_ordered <= 0):
		print("Invalid Input! The number of bags must be greater than 0")
		sys.exit()

# calculate coffee cost (not include bags)
	if (bags_ordered >= BAG7):
		discount_rate = RATE7
	elif (bags_ordered >= BAG6):
		discount_rate = RATE6
	elif (bags_ordered >= BAG5):
		discount_rate = RATE5
	elif (bags_ordered >= BAG4):
		discount_rate = RATE4
	elif (bags_ordered >= BAG3):
		discount_rate = RATE3
	elif (bags_ordered >= BAG2):
		discount_rate = RATE2
	else:
		discount_rate = RATE1

	coffee_cost = bags_ordered * PRICE
	coffee_discount = coffee_cost * discount_rate


# calculate number of different boxes and box cost
	if (bags_ordered >= 20):
		box_used_large = bags_ordered // 20
		remainder = bags_ordered % 20
	if (remainder >= 10):
		box_used_medium = remainder // 10
		remainder = remainder % 10

	if (bags_ordered < 10):
		remainder = bags_ordered
	if (remainder > 5):
		box_used_small = 2
	elif (remainder > 0):
		box_used_small = 1
	else:
		box_used_small = 0

	box_cost = BOX1 * box_used_large + BOX2 * box_used_medium + BOX3 * box_used_small


# calculate total cost
	total_cost = coffee_cost - coffee_discount + box_cost

# print results
	print("\nOrder Summary: ")
	print("\tBags ordered:\t", bags_ordered)
	print("\tFull Price:\t", bags_ordered, "x $", format(PRICE, "0.2f"), "= $", format(coffee_cost, "0.2f"))
	print("\tDiscount:\t $", coffee_discount, "(", format(discount_rate * 100, "0.2f"), "%off)\n" )

	print("\tBox(es) Used: ")
	if (box_used_large > 0):
		print("\t\t\t", box_used_large, "Large - $", format(box_used_large * BOX1, "0.2f"))
	if (box_used_medium > 0):
		print("\t\t\t", box_used_medium, "Medium - $", format(box_used_medium * BOX2, "0.2f"))
	if (box_used_small > 0):
		print("\t\t\t", box_used_small, "Small - $", format(box_used_small * BOX3, "0.2f"))

	print("\nTotal = $", format(coffee_cost, "0.2f"), "- $", format(coffee_discount, "0.2f"),
	"+ $", format(box_cost, "0.2f"), "= $", format(total_cost, "0.2f"))


main()
