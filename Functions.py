
numbers = [13, 5102, 45, 2301.40, 203, 1502, 3]

# Starter code - finished in the lists mini-project
numbers_sum = sum(numbers)

if len(numbers) >= 1:
    print(numbers_sum/len(numbers))
else:
    print(0)
    
# Complete the mean function 
def mean(arg_numbers):
    numbs_sum = sum(arg_numbers)
    
    if len(arg_numbers)>=1:
        return numbs_sum/len(arg_numbers)
    else:
        return 0
    

# Test code - Do not change anything below this line
print(mean(numbers))
