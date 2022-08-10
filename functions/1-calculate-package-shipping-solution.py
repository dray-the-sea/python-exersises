# write a function that calculates shiping cost given the weight of a package and the distance it's traveling
# shipping cost rules:
#  1. there's a starting cost of $5 per package, regardless of weight and distance
#  3. for packages is over 5lb, add $2 for every 1lb
#  3. for distance is over 12 miles, add $.25 for every 1 mile 



def calculate_shipping(weight, distance):
    starting_cost = 5

    free_weight = 5
    lb_surcharge = 2

    free_distance = 12
    distance_surcharge = .25
 
    cost = starting_cost

    if weight > free_weight:
        cost += lb_surcharge * (weight - free_weight)
    
    if distance > free_distance:
        cost += distance_surcharge * (distance - free_distance)

    return cost


# test the fuction with the following shipping options: 
#  1. letter that weighs .3lb and is traveling 5 miles
#  2. letter that weighs .3lb and is traveling 12 miles
#  3. letter that weighs .3lb and is traveling 52 miles
#  4. box that weighs 5lb and is traveling 8 miles
#  5. box that weighs 5lb and is traveling 12 miles
#  6. box that weighs 5lb and is traveling 800 miles
#  7. box that weighs 25lb and is traveling 1 miles
#  8. box that weighs 25lb and is traveling 12 miles
#  9. box that weighs 25lb and is traveling 800 miles

# under the weight limit
print( calculate_shipping(.3, 5) ) # expect 5 ($5 base, no extra for weight, distance < limit) 
print( calculate_shipping(.3, 12) ) # expect 5 ($5 base, no extra for weight, distance == limit)
print( calculate_shipping(.3, 52) ) # expect 15 ($5 base + .25 * 40 extra miles)

# at weight limit
print( calculate_shipping(5, 8) ) # expect 5 ($5 base, weight == limit, distance < limit)
print( calculate_shipping(5, 12) ) # expect 5 ($5 base, weight == limit, distance == limit) 
print( calculate_shipping(5, 800) ) # expect 202 ($5, weight == limit, .25 * 788 extra miles)

# over weithg limit
print( calculate_shipping(25, 1) ) # expect 45 ($5 base, 2* 20 extra lb, distance < limit) 
print( calculate_shipping(25, 12) ) # expect 45 ($5 base, 2* 20 extra lb, distance == limit)
print( calculate_shipping(25, 800) ) # expect 242 ($5 base, 2* 20 extra lb, .25 * 788 extra miles)
