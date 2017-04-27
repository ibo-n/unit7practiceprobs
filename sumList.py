def sum_list(numbers):
	""" Takes a list of numbers and returns the sum of the list"""
	
	if len(numbers) == 0:
		return 0 

	sum = numbers[0] +sum_list(numbers[1:])
	return sum 
	
	
####### Main programm ###########

oneList = [1, 5, 6, 10]
sum = sum_list(oneList)
print("The sum of {} is {} ".format(oneList, sum_list(oneList)))  