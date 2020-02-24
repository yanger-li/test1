Input = 0
Output = 0
Result = 0
one, two = 0, 0

print("Enter an integer between 1 and 99 :", end="")
Input = eval(input())

one = Input % 10
two = Input // 10
Output = one*10+two
Result = 2*Output
print ("You entered", Input, ".", "The swapped integer is", Output, ".")
print ("The double of the swapped integer is: 2 x ", Output, "=", Result)
