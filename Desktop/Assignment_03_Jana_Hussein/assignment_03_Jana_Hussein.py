line = '_________________'
print(line)
Menu = ['1. Count Digits', '2. Find Max', '3. Count Tags', '4. Exit']
for choice in Menu:
    print(choice)
line = '_________________'
print(line)

inp = int(input('Please select a choice: '))

if inp == 4:
    print('You exited the program.')

elif inp == 1:
    def count_digit():
        integ = int(input('Enter any number: '))
        def split_num(integ, count=1):
            if integ < 10:  # the integer is made up of 1 digit (Base Case)
                return count  # which is equal to 1
            else:
                # Recursive Case
                return split_num(integ // 10, count + 1)  # Increase counter
        print('The number of digits in this number is', split_num(integ))

    count_digit()

elif inp == 2:
    def Max():
        InputList = []
        while True:
            Input = int(input('Enter a list of integers: '))
            InputList.append(Input)
            if len(InputList) >= 8:
                break
        print("Input list:", InputList)

        
        def FindMax(InputList, index):
            if index == len(InputList) - 1:#Base case reaching the last value of the list
                return InputList[index]
            compare_digits = FindMax(InputList, index + 1) #check each element on dif indexes
            if compare_digits > InputList[index]:#check values each returned value and compare with the one before
                return compare_digits
            else:
                return InputList[index]

        
        print("The maximum value is:", FindMax(InputList, 0))

    Max()

