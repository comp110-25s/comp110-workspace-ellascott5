"""Planning a tea party!"""

__author__: str = "730736431"


def main_planner(guests: int) -> None:
    """Main function for planning a tea party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed for each person."""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats need for each person."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost the tea party."""
    return float(tea_count * 0.50 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
