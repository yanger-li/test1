def main():
    limitspeed, clockedspeed, overmiles, drivingspeed, fine= 0, 0, 0, 0, 0
    over90 = "No"
    overlimit, overunit, overmph, overpenalty= 65, 5, 90, 220

    print("Enter the speed limit and the clocked speed: ", end="")
    limitspeed, clockedspeed = eval(input())


    if (limitspeed > clockedspeed):
        drivingspeed = "legal"
        fine = 0
    else:
        drivingspeed = "Illegal"
        overmiles = clockedspeed - limitspeed
        fine = overlimit + overmiles * overunit
    if (clockedspeed > overmph):
        over90 = "Yes"
        fine = fine + overpenalty
    else:fine = fine

    print("")
    print("\tThe clocked speed is:\t", drivingspeed)
    print("\tDriving over 90 mph:\t\t$", format(over90, "0.2f"))
    print("\tThe fine is:\t\t$", format(fine, "0.2f"))

main()
