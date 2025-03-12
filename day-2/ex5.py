import random
from random import randint

number = input("Enter a number: ")
def check_nubmer(number):
    num = randint(1, 100)
    if num == number:
        print("its the same number!")
    else:
        print("its the wrong number, that's your number"+number+"and that's my number",num)
check_nubmer(number)