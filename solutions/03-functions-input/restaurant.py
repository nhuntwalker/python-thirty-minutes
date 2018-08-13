"""Command line program modeling the point of sale in a Caribbean restaurant."""


if __name__ == "__main__":
    greeting = """Welcome to Caribbean Hot Pot!
--------------------
> If you'd like to see our menu, enter "MENU"
> If you'd like to get right to ordering, enter "ORDER"
"""
    action = input(greeting)
    
    while True: