#! python3

# Multiplication quiz
import random
import sys

#This function prints the current results
def results():
    print('You have gotten ' + str(correct) + ' correct and ' + str(incorrect) + ' incorrect.')
    print('You have gotten ' + str(correct/total*100) + '% of ' + str(total) + ' right so far!')
    print('')
    
# Provide instructions
print('This program will provide multiplication problems.')
print('The values will be between 0 and 12.')
print('Please answer the problems provided.')
print('To begin, enter: \"begin\".')
print('When you are done, enter: \"done\".')

response = input()
correct = 0
incorrect = 0
total = 0

# Generate random multiplication problems and provide instant feedback
while response != 'done':
    first = random.randint(0, 12)
    second = random.randint(0, 12)
    print('What is ' + str(first) + ' * ' + str(second) + '?')
    response = input()
    try:
        if int(response) == first * second:
            total += 1
            correct += 1
            print('That is correct!')
            results()
            
        else:
            total += 1
            incorrect += 1
            print('Sorry, that is incorrect.')
            results()
    except ValueError:
        print('Thank you for playing!')
        print('Your final score is ' + str(correct/total*100) + '%!')
        sys.exit()
