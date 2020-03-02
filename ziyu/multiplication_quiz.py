import random
def main():
    x1 = random.randint(0, 9)
    x2 = random.randint(0, 9)

    print("How much is", x1, "x", x2, "= ? ", end="")
    answer = eval(input())

    if (answer == (x1 * x2)):
        correct = random.randint(1,4)
        if (correct == 1):
            print("\nVery good!")
        elif (correct == 2):
            print("\nExcellent!")
        elif (correct == 3):
             print("\nNice work!")
        else:
            print("\nKeep up the good work!")
    if (answer != (x1 * x2)):
        wrong = random.randint(1,4)
        if (wrong == 1):
            print("\nNo, but thanks for trying.")
        elif (wrong == 2):
            print("\nClose, but not quite right.")
        elif (wrong == 3):
            print("\nWrong answer.")
        else:
            print("\nNo, but it's okay to be wrong.")

    print(x1, "x", x2, "=", x1 * x2, "\n")

main()
