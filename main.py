import functions

def display_menu():
    print("\nMenu:")
    print("1 - URL Categorize")
    print("2 - Check Palindrome")
    print("3 - Count Digits in String")
    print("4 - Disemvowel a String")
    print("5 - Calculate Expression")
    print("6 - Exit Program")

def main():
    option = 0  # Initialize the option
    while option != 6:
        display_menu()  # Display menu each time
        
        try:
            option = int(input("Enter your option: "))  # Prompt for input inside the loop
            if option == 1:
                url = input("Enter URL: ")
                print("Category:", functions.url_categorize(url))
                pass
            elif option == 2: 
                # is_palindrome(s)
                pass
            elif option == 3: 
                # digit_count(s)
                pass
            elif option == 4: 
                # dsmvwl(string)
                pass
            elif option == 5: 
                # calculate(expr)
                pass
            elif option == 6: 
                print("Exiting the program!")
                break  # Properly exit the loop
            else: 
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


main()