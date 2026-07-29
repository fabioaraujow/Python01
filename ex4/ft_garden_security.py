#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        if height < 0.0:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if plant_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            self._plant_age = 0
        else:
            self._plant_age = plant_age

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._plant_age += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._plant_age} days old")

    def set_height(self, new_height: float) -> None:
        if new_height < 0.0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._plant_age = new_age
            print(f"Age updated: {self._plant_age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-1)
    rose.set_age(-1)
    print("")
    print("Current state: ", end="")
    rose.show()
