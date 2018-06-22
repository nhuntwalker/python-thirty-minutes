"""Read in a data file of people's information, restructure it into a list of dictionaries, and print the result."""
from pprint import pprint 
# pprint = pretty print;
# for making a list of dictionaries look like more than a blob of text


def process_line(line: str) -> dict:
    """Assign values from lines of a data file to keys in a dictionary."""
    name, age, state = line.strip().split(",")
    result = {"name": name, "age": int(age), "state": state}
    return result


file_path = "data/people.csv"
in_file = open(file_path)
file_data = in_file.readlines()
in_file.close()

people = []
for line in file_data:
    people.append(process_line(line))

pprint(people)
