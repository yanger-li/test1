OVERLIMIT, OVERUNIT, OVERMPH, OVERPENALTY = 65, 5, 90, 220

def main():
    print("Enter the speed limit and the clocked speed: ")
    speed_limt, clocked_speed = input().split(",")
    speed_limt = eval(speed_limt)
    clocked_speed = eval(clocked_speed)

    # print(type(speed_limt))
    # print(type(clocked_speed))

    speed_fine = 0.0

    if clocked_speed < speed_limt:
        print("\t The clocked speed is: \t Legal")
        print("\t Driving over 90 mph: \t No")
        print("\t The fine is: \t $" + str(speed_fine))
    else:
        if clocked_speed > OVERMPH:
            speed_fine = speed_fine + OVERLIMIT + (clocked_speed - speed_limt)*OVERUNIT + OVERPENALTY
            print("\t The clocked speed is: \t Illegal")
            print("\t Driving over 90 mph: \t Yes")
            print("\t The fine is: \t\t $" + str(speed_fine))
        else:
            speed_fine = speed_fine + OVERLIMIT + (clocked_speed - speed_limt)*OVERUNIT
            print("\t The clocked speed is: \t Illegal")
            print("\t Driving over 90 mph: \t No")
            print("\t The fine is: \t\t $" + str(speed_fine))

main()
