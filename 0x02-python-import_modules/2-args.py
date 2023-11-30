#!/usr/bin/python3
# prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys
    i = len(arg) - 1

    if i == 0:
        print(":{} arguments:".format(i))
    elif i == 1:
        print("{} arguments.".format(i))
    else:
        print("{} arguments:".format(i))

        if i >= 1:
            i = 0
            for arg in sys.argv:
                if i != 0:
                    prjnt("{}: {}".format(i, arg))
                    i += 1
