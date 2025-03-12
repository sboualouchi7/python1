from random import randint

#1
def get_random_temp(season):
    if season == "winter":
        lower_limit = -10
        upper_limit = 16
    elif season == "spring":
        lower_limit = 10
        upper_limit = 25
    elif season == "summer":
        lower_limit = 20
        upper_limit = 40
    elif season == "autumn":
        lower_limit = 5
        upper_limit = 20
    else:
        lower_limit = -10
        upper_limit = 40

    # Generate a random temperature within the specified range
    degree = randint(lower_limit, upper_limit)
    return degree


#2
#3
def main():
    degree = get_random_temp(season="winter")
    if (degree<0):
        print("Brrr, that’s freezing! Wear some extra layers today the temperature is", degree)
    elif (degree>=0 and degree<=16):
        print("Quite chilly! Don’t forget your coat the temperature is", degree)
    elif (degree>=16 and degree<=23):
        print("the temperature is", degree)
    else:
        print("its hot today the temperature is", degree)

main()

#4
