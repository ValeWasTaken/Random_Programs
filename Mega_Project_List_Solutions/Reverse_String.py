def main():
    original_string = raw_input("Enter a string to be reversed: ")
    reversed_string = ''

    i = len(original_string) - 1
    while(i >= 0):
        reversed_string += original_string[i]
        i = i - 1

    print(reversed_string)
main()
