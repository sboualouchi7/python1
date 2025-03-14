from ex2 import Dog
import random

# petdog inherits from Dog
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # Get the names of all dogs playing together
        dog_names = ', '.join([dog.name for dog in args])
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        # List of possible tricks
        tricks = [
            f"{self.name} does a barrel roll",
            f"{self.name} stands on his back legs",
            f"{self.name} shakes your hand",
            f"{self.name} plays dead"
        ]
        # Check if the dog is trained
        if self.trained:
            # Print a random trick
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")


if __name__ == "__main__":
    # Create some PetDog instances
    pet_dog1 = PetDog("Rex", 3, 30)
    pet_dog2 = PetDog("Buddy", 2, 25)
    pet_dog3 = PetDog("Max", 4, 40)

    # Train one of the dogs
    pet_dog1.train()


    pet_dog1.play(pet_dog2, pet_dog3)


    pet_dog1.do_a_trick()
    pet_dog2.do_a_trick()  # This dog is not trained yet