# Go through a pile of boxes of tomatoes 
# Print what box it's in and whether it's rotten or not. 

boxes_of_tomatoes = [
                    ["rotten", "not rotten", "not rotten", "not rotten", "rotten"],
                    ["not rotten", "rotten", "rotten", "rotten", "not rotten"],
                    ["rotten", "rotten", "rotten", "not rotten", "not rotten", "not rotten"]
                    ]

for box, tomatoes in enumerate(boxes_of_tomatoes):
    if 'rotten' in tomatoes:
        print(f"box number {box} contains {tomatoes.count('rotten')} rotten tomatoes and {tomatoes.count('rotten')} fresh tomatoes ")