ar = {
    3: "ground",
    4: "four",
    6: "turkey",
    0: "0"
}


def print_stuff(start, end, rules):
    for i in range(start, end + 1):
        if i in rules:
            print(rules[i])
        elif i % 2 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print_stuff(0, 12, ar)


