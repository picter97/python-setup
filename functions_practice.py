def hello():
    print ("")
hello()


def pack(a, b, c):
    allpack = a + b + c
    print(allpack)

pack(2, 4, 5)


def eat_lunch(food_list):
    if len(food_list) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)

eat_lunch("")

eat_lunch(["salad", "piza", "cake"])