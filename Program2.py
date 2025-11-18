def main():  
    try:
        
        x_input = input("Enter a number (x): ")
        x = int(x_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return 

    output = ""
    for i in range(1, x + 1):
        oddNumber = 2 * i - 1  
        if i < x:
            output += str(oddNumber) + ", "
        else:   
            output += str(oddNumber) 

    print(output)
    
if __name__ == "__main__":
    main()
