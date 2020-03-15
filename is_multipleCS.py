def is_multiple():    
    print("This function will test to see if a number \"n\" is a multiple of another number \"m\".")
    n = float(input("\nPlease enter your value for the variable \"n\": "))
    m = float(input("Next, your value for the variable \"m\": "))
    
    #use an equation to test if n devides cleanly into m
    test = n/m
    #use a float method to test if the number is whole
    if test.is_integer() == True:
        print("\n" + str(n) + " is a multiple of " + str(m) + ".")
        
    else:
        print("\n" + str(n) + " is not a multiple of " + str(m) + ".")
    
    #ask the user if they would like to run the function again
    again = input("If you would like to run the function again, enter \"yes\", otherwise the program will close: ").lower()
    if again == "yes":
        print("\n")
        is_multiple()

is_multiple()