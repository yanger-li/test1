def main():
    print("")
    copies, total = 0, 0
    COST1, COST2, FIXEDCOPY = 6.25, 5, 20

    print("Enter the number of copies: ", end="")
    copies = eval(input())

    if (copies < FIXEDCOPY):
        cost = COST1
        total = copies * cost
    else:
        cost = COST2
        total = (copies - FIXEDCOPY) * cost + FIXEDCOPY * COST1

    print("")
    print("\tYou made", copies, "copies.")
    if (copies < FIXEDCOPY):
        print("\tTotal = ", copies, "x $", format(cost, "0.2f"), "= $", format(total, "0.2f"))
    else:
        print("\tTotal = ", "(", FIXEDCOPY, "x $", COST1, ") + (", copies - FIXEDCOPY, "x $", format(cost, "0.2f"), ") = $", format(total, "0.2f"))
main()
