#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self):
            self._grow_counter = 0
            self._age_counter = 0
            self._show_counter = 0
            self._shade_counter = 0

        def grow_counter(self) -> None:
            self._grow_counter += 1

        def age_counter(self) -> None:
            self._age_counter += 1

        def show_counter(self) -> None:
            self._show_counter += 1

        def show_statistics(self) -> None:
            print(f"Stats: {self._grow_counter} grow, "
                  f"{self._age_counter} age, {self._show_counter} show")

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
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)
        self._stats.grow_counter()

    def age(self) -> None:
        self._plant_age += 1
        self._stats.age_counter()

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._plant_age} days old")
        self._stats.show_counter()

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


def display_stats(plant: Plant) -> None:
    print(f"[statistics from {plant.name}]")
    plant._stats.show_statistics()


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, color: str) -> None:
        super().__init__(name, height, plant_age)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def grow(self) -> None:
        self._height = round(self._height + 8.0, 1)
        self._stats.grow_counter()

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_counter = 0

        def shade_counter(self) -> None:
            self._shade_counter += 1

        def show_statistics(self) -> None:
            super().show_statistics()
            print(f" {self._shade_counter} shade")

    def __init__(self, name: str, height: float,
                 plant_age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, plant_age)
        self._trunk_diameter = round(trunk_diameter, 1)
        self._stats: Tree.TreeStats = self.TreeStats()

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self._height:.1f}"
              f"cm long and {self._trunk_diameter:.1f}cm wide.")
        self._stats.shade_counter()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, plant_age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, plant_age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional Value: {self._nutritional_value}")

    def grow(self) -> None:
        self._height = round(self._height + 2.1, 1)

    def age(self) -> None:
        self._plant_age += 1
        self._nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("")
    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    display_stats(flower)
    print("[asking the rose to bloom]")
    flower.grow()
    flower.bloom()
    flower.show()
    display_stats(flower)
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print("")
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
    print("")
    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
