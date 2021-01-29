import datetime
account = [['Date', 'Credit', 'Debit', 'Balance']]

def transaction():
    now = datetime.datetime.now()
    dayMonthYear= str(now.day)+'/'+str(now.month)+'/'+str(now.year)
    validInput = False
    while validInput == False:
        creditQ = input('Do you want to credit your account in this transaction? Y/N: ').lower()
        if (creditQ == 'y'):
            validInput = True
            credit = float(input('How much do you want to credit your account? '))
            if len(account) > 1:
                lastRow = account[len(account)-1]
                newRow = [dayMonthYear,credit,0,credit + lastRow[3]]
                account.append(newRow)
                print('Added ', credit, 'to your account.')
                print('Your new balance is: ', account[len(account)-1][3])
            else:
                newRow = [dayMonthYear,credit,0,credit]
                account.append(newRow)
                print('Added ', credit, 'to your account.')
                print('Your new balance is: ', account[len(account)-1][3])
        elif(creditQ == 'n'):
            validInput = True
        else:
            print('Please enter a valid input.')

    validInput = False
    while validInput == False:
        debitQ = input('Do you want to debit your account in this transaction? Y/N: ').lower()
        if (debitQ == 'y'):
            validInput = True
            debit = float(input('How much do you want to debit your account? '))
            if len(account) > 1:
                lastRow = account[len(account)-1]
                newRow = [dayMonthYear,debit,0,debit + lastRow[3]]
                account.append(newRow)
                print('Added ', debit, 'to your account.')
                print('Your new balance is: ', account[len(account)-1][3])
            else:
                newRow = [dayMonthYear,credit,0,debit]
                account.append(newRow)
                print('Added ', debit, 'to your account.')
                print('Your new balance is: ', account[len(account)-1][3])
        elif(debitQ == 'n'):
            validInput = True
        else:
            print('Please enter a valid input.')

userQuestion = input('Do you still want to run the program? Y/N: ').lower()
while (userQuestion == 'y'):
    transaction()
    print('Your new account looks like this: ')
    for i in account: 
        print (i)
    userQuestion = input('Do you still want to run the program? Y/N: ').lower()

def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)): #run N times, where N is number of elements in a list
        # Last i elements are already in place
        # It starts at 1 so we can access the previous element
        for j in range(1,len(list_of_numbers)-i): # N-i elements
            if list_of_numbers[j-1] > list_of_numbers[j]: #check if previous element is bigger than the current element
                #Swap code from the instructors notes:
                temp = list_of_numbers[j-1]
                list_of_numbers[j-1] = list_of_numbers[j]
                list_of_numbers[j] = temp

    return list_of_numbers

test0 = [3, 22, 14, 434, 501, 11, 9, 1230, 304, 123, 5412, 381923, 302, -3, 1]
test1 = [43, 12, 7, 9, 22, 1, 104]
test2 = [100, 0, 0, -20, 30, -5]
test3  = [28, 4, 17, 666, 1001, 52, 61, 30]
print(bubble_sort(test0))
print(bubble_sort(test1))
print(bubble_sort(test2))
print(bubble_sort(test3))

def search(numbers, query_number):
    found_number = False
    
    for number in numbers:
        if number == query_number:
            found_number = True
            break
            
    return found_number


# Don't change code below this line
#query_number = 3
#numbers = [40, 512, 31, 3, 50, 610, 2]
#print(search(numbers, query_number))

test0 = [-3, 1, 3, 9, 11, 14, 22, 123, 302, 304, 434, 501, 1230, 5412, 381923]
searchItem0 = 13
print(search(test0, searchItem0))

test1 = [1, 7, 9, 12, 22, 43, 104]
searchItem1 = 9
print(search(test1, searchItem1))
 
test2 = [-20, -5, 0, 0, 30, 100]
searchItem2 = 31
print(search(test2, searchItem2))
 
test3 = [4, 17, 28, 30, 52, 61, 666, 1001]
searchItem3 = 666
print(search(test3, searchItem3))
