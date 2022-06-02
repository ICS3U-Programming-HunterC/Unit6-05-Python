#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 31, 2022
#  This program asks the user repeatedly for a mark between 0 and 100%
# The program uses a loop to enter each mark into a list of integers.
# When the user enters -1, the loop stops. It will then calculate the
# average and display the average


def calc_average(list_of_int):

    # calculate the sum
    if len(list_of_int) == 0:
        return -1
    else:
        sum = 0
        for a_num in list_of_int:
            sum += a_num

    # calculate the avearge
    avg = sum / len(list_of_int)

    # return the average
    return avg


def main():

    # declare the list
    list_of_num = []

    # greet the user
    print(
        "This program calculates the average of all your marks!! Enter -1 to end the program!"
    )

    while True:
        # get the mark as a string
        mark_string = input("Enter a mark(%) or -1 to stop: ")
        try:
            # convert the string to an int
            mark_int = int(mark_string)

            # if the user enters -1 the program will stop asking for input
            # and it will then calculate the average, by calling the function
            if mark_int == -1:
                avg = calc_average(list_of_num)
                break

            # append the mark to the list
            list_of_num.append(mark_int)
        except:
            # catch the invalid input and then get the user to go again
            print("{} is not a valid input".format(mark_string))
            continue

    # display the average
    print("")
    print("The average is: {:.0f}%".format(avg))


if __name__ == "__main__":
    main()
