"""Develop a large program to plan a tea party"""

__author__: str = "730823736"


def main_planner(guests: int) -> None:
    """the main function that orchestrates the program's execution."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """Compute the number of tea bags needed based on number of guests."""
    return 2 * people


def treats(people: int) -> int:
    """Compute the number of treats needed based on the number of teas guests are expecting to drink."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Compute the cost of the tea bags and the treats combined."""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
