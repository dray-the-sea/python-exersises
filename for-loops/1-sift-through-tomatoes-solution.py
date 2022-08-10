# Go through a pile of boxes of tomatoes 
# Print what box it's in and whether it's rotten or not. 

boxes_of_tomatoes = [
                    ["rotten", "not rotten", "not rotten", "not rotten", "rotten"],
                    ["not rotten", "rotten", "rotten", "rotten", "not rotten"],
                    ["rotten", "rotten", "rotten", "not rotten", "not rotten", "not rotten"]
                    ]

for box in boxes_of_tomatoes:
    for tomato in box:
        if tomato == "rotten":
            print(f"box {boxes_of_tomatoes.index(box)}: gross, throw it out!")
        else:
            print(f"box {boxes_of_tomatoes.index(box)}: keep it!")