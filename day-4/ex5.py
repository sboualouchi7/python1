from ex4 import Family

class TheIncredibles(Family):
    def use_power(self, name):
        # Check if the member is over 18 before allowing them to use their power
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name} uses their power: {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old and cannot use their power!")
                return
        print(f"{name} is not a member of the family.")

    def incredible_presentation(self):
        print("***** Here is our powerful family *****")
        super().family_presentation()
        print("\nIncredible details:")
        for member in self.members:
            print(f"Incredible name: {member['incredible_name']}, Power: {member['power']}")

incredibles = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])

incredibles.incredible_presentation()

incredibles.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')

print("\nAfter Baby Jack is born:")
incredibles.incredible_presentation()

print("\nDemonstrating powers:")
try:
    incredibles.use_power('Michael')  # This should work
    incredibles.use_power('Sarah')    # This should work
    incredibles.use_power('Jack')     # This should raise an exception
except Exception as e:
    print(f"Error: {e}")