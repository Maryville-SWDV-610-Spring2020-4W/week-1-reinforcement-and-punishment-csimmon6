def main():
    print("This program will write the phrase \"I will never spam my friends again.\" 100 times.")
    input("Press enter to start the program.")
    #process a prnt statement 100x
    for index in range(100):
        print("I will never spam my friends again.")
    #ask the user if they would like to run the program again
    again = input("If you would like to run the program again, enter \"yes\", otherwise the program will close: ")
    if again == "yes":
        main()
        
main()