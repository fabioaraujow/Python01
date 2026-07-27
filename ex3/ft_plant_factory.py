#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    print("Created: ", end="")
    rose.show()
    oak = Plant("Oak", 200, 365)
    print("Created: ", end="")
    oak.show()
    cactus = Plant("Cactus", 5, 90)
    print("Created: ", end="")
    cactus.show()
    sunflower = Plant("Sunflower", 80, 45)
    print("Created: ", end="")
    sunflower.show()
    fern = Plant("Fern", 15, 120)
    print("Created: ", end="")
    fern.show()
