#printing numbers as words
dictionary = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "null"
}
var = input("enter your phone number (or any number): ")
for item in var:
    print(dictionary[int(item)], end=" ")