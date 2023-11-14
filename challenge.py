#!/usr/bin/python3
"""Challenge"""

wordbank= ["indentation", "spaces"]

tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "Louis", "Mabel", "Paul", "Zach"]


def main():
    """runtime code"""

    wordbank.append(4)
    print("\n" + str(wordbank) + "\n")
    
    num = input("Please enter a number between 1 and 17: ")
    print(num)
    
    print("")

    student_name = tlgstudents[int(num) - 1]
    print(student_name)
    print("")
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

if __name__ == "__main__":
    main()
