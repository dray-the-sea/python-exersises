
# your friend has a small store and has asked you to analyze their sales for the week. They'll want to know:
#   1.  the total amount that they made for the whole week
#   2. what day they made the most money
#   3. how much money was made that day


weekly_sales = {
    "Monday": {"shoes": 5, "socks": 23, "toothbrushes": 2, "cookies": 75},
    "Tuesday": {"shoes": 2, "socks": 30, "toothbrushes": 4, "cookies": 42},
    "Wednesday": {"shoes": 6, "socks": 11, "toothbrushes": 3, "cookies": 8},
    "Thursday": {"shoes": 8, "socks": 9, "toothbrushes": 10, "cookies": 26},
    "Friday": {"shoes": 1, "socks": 14, "toothbrushes": 5, "cookies": 50}
}

prices =  {"shoes": 20, "socks": 2.50, "toothbrushes": 1.78, "cookies": .50}

best_day = ""
best_day_sales = 0
weekly_total = 0

# look at the sales for each day
for day, day_sales in weekly_sales.items():
    day_total = 0

    # add each sale total to the day's total
    for item, quantity in day_sales.items():
        sale = quantity*prices[item]
        day_total  = day_total + sale

    #track the total for the week
    weekly_total += day_total

    # track the best day's sales
    if day_total > best_day_sales:
        best_day = day
        best_day_sales = day_total


print(f"the weekly total was {weekly_total}")
print(f"the best day was {best_day} with a total sales of {best_day_sales}")
