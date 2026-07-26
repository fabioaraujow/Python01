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
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


if __name__ == "__main__":

    rose = Plant("Rose", 25, 30)
    start_size = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    final_size = round(rose.height - start_size, 1)
    print(f"Growth this week: {final_size}cm")
