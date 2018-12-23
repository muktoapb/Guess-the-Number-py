import random

#Generate random number 1-100
number = random.randint(1,100)
count = 0

while True:
    guess_number = int(input('Give a number between 1-100 : '))
    if guess_number>100:
        continue
    #if user put more than 100 loop will not exicute belew code
    count += 1
    if guess_number > number :
        print('Put lower number then {}'.format(guess_number))
    elif guess_number < number :
        print('Put higher number then {}'.format(guess_number))
    elif guess_number == number:
        break
print("congratuations you tried {} times".format(count))
