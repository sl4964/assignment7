from interval import Interval
import sys

ReadMe = "Please read me"
print(ReadMe)


while True:
    while True:
        answer = input('Continue? (y/n): ')
        if answer in ('y', 'n', 'yes', 'no', 'Y', 'Yes', 'N', 'No'):
            break
        print('Invalid input.')
        
    if answer in ('y', "yes", 'Y', 'Yes'):
        break
    else:
        print('Sorry to see you go.')
        sys.exit()

while True:
    userInput = input("List of intervals?  ")
    try:
    	intList = Interval.mergeOverlapping(userInput)
    	print(intList)
    	break
    except:
    	print("Invalid list")


while True:
	addOn = input("interval?  ")
	if addOn == "quit":
		print('Sorry to see you go.')
		sys.exit()

	try:
		test = Interval(addOn)
	except:
		print("Invalid Input")
		continue

	ans = Interval.insert(userInput, addOn)
	userInput = userInput + ',  ' + addOn
	print(ans)
	# except:
	# 	print("Invalid Input")


# while True:
#     try:
#         addOn = input("interval?  ")
#         if addOn == "quit":
#         	print('Sorry to see you go.')
#         	sys.exit()
        
#         try:

#        	ans = Interval.insert(userInput, addOn)
#         userInput = userInput + ',  ' + addOn
#         print(ans)

#     except:
#     	pass

#     print('\nIncorrect input, try again')




if __name__ == '__main__':
    pass