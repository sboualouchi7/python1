class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# 1.
cat1 = Cat("Luna", 3)
cat2 = Cat("rex", 5)
cat3 = Cat("mopoo", 2)

# 2
def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

# 3
cats = [cat1, cat2, cat3]
old = find_oldest_cat(cats)
print(f"The oldest cat is {old.name}, and is {old.age} years old.")