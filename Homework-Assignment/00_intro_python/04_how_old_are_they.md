Problem Statement
Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen.

Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):


def main():
    anton : int = 21  # Anton's age is given as 21 years old
    beth : int = 6 + anton  # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    chen : int = 20 + beth  # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    drew  : int= chen + anton  # Drew is as old as Chen's age plus Anton's age, so add them together
    ethan : int = chen  # Ethan is the same age as Chen, so set Ethan's age equal to Chen's

   # Print out all of the ages!
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

def main():
    anton = 21  # Anton's age is given as 21 years old
    beth = 6 + anton  # Beth is 6 years older than Anton
    chen = 20 + beth  # Chen is 20 years older than Beth
    drew = chen + anton  # Drew is Chen's age plus Anton's age
    ethan = chen  # Ethan is the same age as Chen

    # Print out all of the ages with the exact required format
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))


if __name__ == '__main__':
    main()

    #The output is 
    Anton is 21
    Beth is 27
    Chen is 47
    Drew is 68
    Ethan is 47

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()