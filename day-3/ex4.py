class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"Animal '{new_animal}' has been added to the zoo.")
        else:
            print(f"Animal '{new_animal}' is already in the zoo.")

    def get_animals(self):
        # Print all the animals in the zoo
        if self.animals:  # Check if the list is not empty
            print(f"Animals in {self.name}:")
            for animal in self.animals:
                print(f"- {animal}")
        else:
            print(f"There are no animals in {self.name}.")
    def sell_animal(self,animal):
        if animal  in self.animals:
            self.animals.remove(animal)
            print(f"Animal '{animal}' has been removed from the zoo.")
        else:
            print(f"Animal '{animal}' is not in the zoo.")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)

        # Return the grouped dictionary
        return grouped_animals

my_zoo = Zoo("My Awesome Zoo")
my_zoo.add_animal("cat")
my_zoo.add_animal("shark")
my_zoo.add_animal("enez")
my_zoo.add_animal("tiple")
my_zoo.add_animal("dav")
my_zoo.add_animal("dog")
my_zoo.add_animal("cat")

my_zoo.get_animals()

my_zoo.sell_animal("lion")

my_zoo.sort_animals()

