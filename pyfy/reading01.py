#!/usr/bin/env python3

"""Automation Course - working with files"""

def main():
    """ Main function """

    """ opening the vendor file """
    myfile = open("vendor.txt", "r")


    with open("vendor-ips.txt", "w") as myotherfile:
        for line in myfile.readlines():
            splitline = line.split(" ")
            myotherfile.write(splitline[-1] + "\n")


    myfile.close()


if __name__ == "__main__":
    main()

