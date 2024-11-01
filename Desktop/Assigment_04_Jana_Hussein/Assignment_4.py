#Exercise 1:

def display_menu():
    print("Please choose one of the following options:")
    print("1. Sum Tuples")
    print("2. Export JSON")
    print("3. Import JSON")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter a number from (1-4): ")

        if choice == '1':
            print("You selected 'Sum Tuples'")
            def add_tuples ():
                tup1 = tuple(input('please enter a tuple '))
                tup2 = tuple(input('please enter another tuple '))
                if len(tup1)!= len(tup2): #ensure tuples are of same length
                    print ('the tuples must be of same length.')
                else:
                    list_1 = list(tup1) #convert tuple to a list to be mutable
                    list_2 = list(tup2)
                    list1 = [] 
                    list2 = []
                for i in list_1:
                    if i.isdigit():
                        i = int(i) #convert the string to int and add them to the empty list
                        list1.append(int(i))
                for j in list_2:
                    if j.isdigit():
                        j =int(j)
                        list2.append(j)
                def add_values (index):
                    if index == len(list1):#base case
                        return [] #mesh 0 or btenzed empty list kaen 0
                    else:
                        return [list1[index] + list2[index]] + add_values(index + 1)#recursive case
                result = add_values (0)
                sum_of_tuples = tuple(result)
                print ('sum of tuples is' , result)
            add_tuples()
                
        elif choice == '2':
            print("You selected 'Export JSON'")   
        elif choice == '3':
            print("You selected 'Import JSON'")
        elif choice == '4':
            print("You exited the program.")
            break
        else:
            print("Invalid choice")


main()
