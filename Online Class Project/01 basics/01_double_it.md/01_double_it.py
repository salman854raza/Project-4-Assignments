def main():
    # Get initial number from user
    curr_value = float(input("Enter a number: "))
    
    # Double the number until it's 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2
        print(int(curr_value) if curr_value.is_integer() else curr_value, end=' ')

    print()  # Add a newline at the end


if __name__ == '__main__':
    main()