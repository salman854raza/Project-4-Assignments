# Solution
def get_last_element(lst):
    """Prints the last element of the provided list."""
    # Using negative indexing to get the last element
    print(lst[-1])

def get_lst():
    """Prompts the user to enter one element of the list at a time and returns the resulting list."""
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    if lst:  # Ensure the list is not empty
        get_last_element(lst)
    else:
        print("The list is empty. Please enter at least one element.")

if __name__ == '__main__':
    main()