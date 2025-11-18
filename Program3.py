
def main():

    try:   
        a_input = input("Enter a number (a): ")
        a = int(a_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return 

    terms = a - 1 if (a % 2 == 0) else a   
    output = ""
    
    for i in range(1, terms + 1):
      
        oddNumber = 2 * i - 1     
        if i < terms:         
            output += str(oddNumber) + ", "
        else:        
            output += str(oddNumber) 
  
    print(output)
 
if __name__ == "__main__":
    main()