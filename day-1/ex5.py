#Exercice5
my_numbers = {9, 17, 21}
my_numbers.add(22)
my_numbers.add(89)

my_numbers.remove(89)

friend_fav_numbers = {10, 20, 30}
our_numbers = my_numbers.union(friend_fav_numbers)

print(our_numbers)