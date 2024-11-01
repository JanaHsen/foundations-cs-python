#Exercise 1:

def find_factorial (): #Define the function

    n=int(input('Please enter a number   ')) # The user will input a number

    x = range(1,n+1) #the number will be set in the range 

    n_factorial = 1 #this variable will be used in the eq

    if n > 0: 
        for i in x: #taking all the numbers between 1 and the entered number (included)
            n_factorial = n_factorial * i #this eq helps multiply all the numbers present in the range
        print ( 'The factorial number is', n_factorial )

    else: #if n<0
        print ( 'Invalid Input')
        

find_factorial ()

#Exercise 2

def find_divisors ():

    n=int(input('please enter a number    ')) #the user will input a number

    div = []  # define an empty list to add upon

    for i in range (1 , n+1): # this will allow to access all the numbers in this range

        if n % i == 0:  # remainder 0 means n is divisible by i

            div.append(i)  # we add the divisible numbers to the empty list 

    print ('The divisors are' , div , end= " ")


find_divisors ()

#Exercise 3:

def reverseString():
    
    user_input = input("Enter a phrase: ")
    
    reversed_input = "" #empty string to be used later
    
    for i in range(len(user_input) - 1, -1, -1): # go backwards while reading the string
        reversed_input += user_input[i]  # Append each character to the reversed string
    
    return reversed_input  


result = reverseString()
print(result)

    
#Exercise 4:

def even_list ():


    n = int(input('Please enter a number: ')) # user inputs a number 

    user_list = [n] #this number is added to a list

    new_list = [] #an emty list will be used further down

    while n>0 : # loop allowing us to insert several inputs

        n = int(input('Please enter a number: '))

        user_list.append(n) #the list now has all values of n

        if n < 0 : # to stop the loop we use the negative integer condition
             break
        
    for i in user_list: #we check the elements in this list

        if i<0: #This is to remove any negative numbers in the list
            user_list.remove(i)

            new_list = user_list # assign the new list as new variable

            for i in new_list: # access the odd elements to remove them and keep the even numbers
                if i % 2 == 1:
                    new_list.remove(i)
 
    print (new_list)

    
even_list()

# Exercise 5

def password_weak_or_strong ():

    password = (input('Please create a password :'))


    symbols = ['!', '$' , '?' ,'#'] # A list of symbols

    upper_case= lower_case = yes_digit = yes_symbol= False #flag method

    if len(password) >= 8 : #first check the number of characters
        for i in password : #loop to check each character with specific conditions
            if i.isupper():
                upper_case = True #changing the initial assumption to true if the condition is met
                
            if i.islower():
                lower_case = True
                
            
            if i.isdigit():
                 yes_digit = True 
                           
                    
            if i in symbols : 
                yes_symbol = True
                
        if upper_case== lower_case == yes_digit == yes_symbol== True : # if ALL conditions are met 
            print (' Strong Password')

        else:
             print ('Weak Password')
             
    else:
            print ('Weak Password')

password_weak_or_strong ()

# Exercise 6:

def IPv4_address():

    n = (input (' enter IPv4 address  '))

    octet = n.split ('.') #split the string to check each octet

    if len(octet) != 4: #ensure there are 4 numbers to be checked

        print ('Invalid IPv4 address')

    for i in octet:
        if not i.isdigit(): #string to int
            print ('Invalid IPv4 address')
            return

        if not 0 <= int(i) <256 : # specify the range of acceptable values
            print ('Invalid IPv4 address')
            return

        if len(i) > 1 and i.startswith('0'): # checks if the number starts with 0
            print ('Invalid IPv4 address')
            return    
    else: 
        print ( 'VALID IP address')

IPv4_address()




    


    



