# 1.
class Dog:
    # 2.
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # 3.
    def bark(self):
        print(f"{self.name} goes woof!")

    # 4.
    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")


# 5.
davids_dog = Dog("Rex", 50)

# 6.
print(f"David's dog: Name - {davids_dog.name}, Height - {davids_dog.height}cm")
davids_dog.bark()
davids_dog.jump()

# 7.
sarahs_dog = Dog("Teacup", 20)

# 8.
print(f"Sarah's dog: Name - {sarahs_dog.name}, Height - {sarahs_dog.height}cm")
sarahs_dog.bark()
sarahs_dog.jump()

# 9. Vérifier quel chien est le plus grand
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger")
else:
    print("Both dogs are the same height")