class Family:
    def __init__(self, last_name, members):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        # Add a new child to the members list
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} was born into the {self.last_name} family.")

    def is_18(self, name):
        # Check if a family member is over 18
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False  # Member not found

    def family_presentation(self):
        # Print the family's last name and members' details
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")

# Create an instance of the Family class
family = Family("Smith", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

# Call the methods
family.born(name='Emily', age=0, gender='Female', is_child=True)
print(f"Is Michael over 18? {family.is_18('Michael')}")
print(f"Is Emily over 18? {family.is_18('Emily')}")
family.family_presentation()