print("To calculate your plates, please enter a number that's (1) at least 45(lbs) and (2) is divisible by 5!")
weightToCalculate = 0
while True:
    try:
        weightToCalculate = float(input("Enter your desired weight to lift: "))
    except ValueError:
        print("Invalid input. Please try again!")
        continue
    else:

        if weightToCalculate == 45:
            print("Just lift the bar! It should weigh 45 lbs.")
            break

        elif weightToCalculate > 45 and weightToCalculate % 5 == 0:

            weightLeft = weightToCalculate - 45
            countBar = 1
            count45s = 0
            count35s = 0
            count25s = 0
            count10s = 0
            count5s = 0
            count2AndAHalfs = 0

            while weightLeft > 0:
                if weightLeft >= 90:
                    count45s += 1
                    weightLeft -= 90
                elif weightLeft >= 70:
                    count35s += 1
                    weightLeft -= 70
                elif weightLeft >= 50:
                    count25s += 1
                    weightLeft -= 50
                elif weightLeft >= 20:
                    count10s += 1
                    weightLeft -= 20
                elif weightLeft >= 10:
                    count5s += 1
                    weightLeft -= 10
                elif weightLeft >= 5:
                    count2AndAHalfs += 1
                    weightLeft -= 5
                else:
                    print("Why isn't this loop working????")

            print("First, you need ONE 45-lb bar")
            print("Then, put the following weights on each side of the bar: ")
            if count45s > 0:
                print(str(count45s) + " 45-lb plate(s)")
            if count35s > 0:
                print(str(count35s) + " 35-lb plates(s)")
            if count25s > 0:
                print(str(count25s) + " 25-lb plates(s)")
            if count10s > 0:
                print(str(count10s) + " 10-lb plates(s)")
            if count5s > 0:
                print(str(count5s) + " 5-lb plates(s)")
            if count2AndAHalfs > 0:
                print(str(count2AndAHalfs) + " 2.5-lb plates(s)")
            break

        else:
            print("Invalid input! Please try again with a number that's "
                  "(1) greater than 45 and (2) evenly divisible by 5!")

# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
