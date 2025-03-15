class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal, count=1):
        # Add animals to  farm
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"

        info += "\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()

        animals_list = []
        for animal in animal_types[:-1]:  # All but the last animal
            if self.animals[animal] > 1:
                animals_list.append(f"{animal}s")
            else:
                animals_list.append(animal)

                animals_str = ', '.join(animals_list)

                last_animal = animal_types[-1]
                if self.animals[last_animal] > 1:
                    animals_str += f" and {last_animal}s"
                else:
                    animals_str += f" and {last_animal}"

                return f"{self.name}'s farm has {animals_str}."

macdonald = Farm("McDonald")

macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')  # Default count is 1
macdonald.add_animal('sheep')  # Add another sheep
macdonald.add_animal('goat', 12)

print(macdonald.get_info())

print("\nTypes of animals on the farm:")
print(macdonald.get_animal_types())

print("\nShort summary:")
print(macdonald.get_short_info())