import math
class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2  # Convert diameter to radius
        else:
            raise ValueError("You must provide either radius or diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}, area: {self.area:.2f}"

    def __repr__(self):
        # This helps with debugging
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        # Make sure we're adding another circle
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        else:
            raise TypeError("Can only add another Circle object")

    def __gt__(self, other):
        # Greater than comparison
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        # Equality check
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius


if __name__ == "__main__":
    # Create some test circles
    c1 = Circle(radius=3)
    c2 = Circle(diameter=8)  # radius should be 4
    c3 = Circle(radius=5)

    print("Circle 1:", c1)
    print("Circle 2:", c2)
    print("Circle 3:", c3)

    c4 = c1 + c3
    print("\nAfter adding Circle 1 and Circle 3:")
    print("New circle:", c4)

    print("\nComparisons:")
    print("Is Circle 1 bigger than Circle 2?", c1 > c2)
    print("Is Circle 3 bigger than Circle 1?", c3 > c1)
    print("Are Circle 1 and Circle 3 equal?", c1 == c3)

    # list of circles
    circle_list = [
        Circle(radius=10),
        Circle(radius=2.5),
        Circle(diameter=12),
        Circle(radius=4)
    ]

    print("\nUnsorted circles:")
    for c in circle_list:
        print(f"- {c}")

    sorted_circles = sorted(circle_list)

    print("\nSorted circles (smallest to largest):")
    for c in sorted_circles:
        print(f"- {c}")