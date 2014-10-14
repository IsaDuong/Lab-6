print "How many numbers do you want to add together?"
total = 0
userInput = int(raw_input())
for item in range(userInput):
    userInput = int(raw_input())
    total = total + userInput
print total

totalList = []
userInput = int(raw_input())
totalList.append(userInput)
for item in range(userInput):
    print sum(totalList)
    
total = 1
firstNumber = int(raw_input())
print "What number do you want to take the factorial of?"
for item in range(firstNumber):
    total = total * item
print total