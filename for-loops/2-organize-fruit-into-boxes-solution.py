
#Sort fruit into 4 boxes:
#  one for good apples,
#  one for good tomatoes,
#  one for good peaches, and
#  one for rotten fruit.

#Print out what ends up in each box and the number of items in each box.


pile_of_fruit = [
    {"type": "apple", "rotten": 1},
    {"type": "peach", "rotten": 0},
    {"type": "tomato", "rotten": 1},
    {"type": "peach", "rotten": 1},
    {"type": "peach", "rotten": 0},
    {"type": "apple", "rotten": 0},
    {"type": "apple", "rotten": 0},
    {"type": "apple", "rotten": 1},
    {"type": "tomato", "rotten": 1},
    {"type": "tomato", "rotten": 0},
    {"type": "pineapple", "rotten": 0},
    {"type": "apple", "rotten": 1},
]

good_apples = []
good_peaches = []
good_tomatoes = []
rotten_stuff = []


for fruit in pile_of_fruit:
    if fruit["rotten"]:
        rotten_stuff.append(fruit)
    else:
        if fruit["type"] == "apple":
            good_apples.append(fruit)
        elif fruit["type"] == "peach":
            good_peaches.append(fruit)
        elif fruit["type"] == "tomato":
            good_tomatoes.append(fruit)
        else:
            print(f"unexpected fruit! it's a {fruit['type']}")

print(len(good_apples), " good apples:", good_apples)
print(len(good_peaches), " good peaches:", good_peaches)
print(len(good_tomatoes), " good tomatoes:", good_tomatoes)
print(len(rotten_stuff), " rotten things:", rotten_stuff)
