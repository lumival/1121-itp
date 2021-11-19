# ITP Week 1 Day 2 (In-Class) Practice

# This is a number magic trick
# Pick a number from 1 - 9
# a = 5
# Multiple by 2
# a *= 2
# Add 10 to the total
# a += 10
# Divide by 2
# a /= 2
# Subtract by the original number
# a -= 5
# Final number is 5
# print(a)
# Take an user's input
step1 = input('Pick a number from 1-9: ')
# Assign a new variable for each step
step2 = int(step1) * 2
print(str(step1) + ' Multiplied by 2 is: ' + str(step2))
step3 = step2 + 10
print(str(step2) + ' Plus 10 is: ' + str(step3))
step4 = int(step3) / 2
print(str(step3) + ' Divided by 2 is: ' + str(step4))
step5 = int(step4) - int(step1)
if step5 == 5:
    print(str(step4) + " Minus the first number is: " + str(step5))
else:
    print('Does not = 5')

# at the end, use an if statement to see if the final is always 5!