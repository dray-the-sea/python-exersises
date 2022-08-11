# your friend has a small store and has asked you to analyze their sales for the week. 
# They'll want to know:
#   1.  the total amount that they made for the whole week
#   2. what day they made the most money
#   3. how much money was made that day

# Use the data and 2 functions that are provided below to implement the accounting that they want



weekly_sales = {
    "Monday": {"shoes": 5, "socks": 23, "toothbrushes": 2, "cookies": 75},
    "Tuesday": {"shoes": 2, "socks": 30, "toothbrushes": 4, "cookies": 42},
    "Wednesday": {"shoes": 6, "socks": 11, "toothbrushes": 3, "cookies": 8},
    "Thursday": {"shoes": 8, "socks": 9, "toothbrushes": 10, "cookies": 26},
    "Friday": {"shoes": 1, "socks": 14, "toothbrushes": 5, "cookies": 50}
}

prices =  {"shoes": 20, "socks": 2.50, "toothbrushes": 1.78, "cookies": .50}

def calculate_sale_total(sales, prices):
    """
    calculates sales total for a list of sales, given the prices for items sold
    sales: dictionary of item names and sold count
    prices: dictionary of item names and unit prices
    """
    day_total = 0

    # add each sale total to the day's total
    for item, quantity in sales.items():
        sale = quantity*prices[item]
        day_total  = day_total + sale

    return day_total

def print_week_summary(week_total, best_day_name, best_day_total):
    """
    prints formatted strings with the weekly sales summary
    week_total (float): total $ sold for the week 
    best_day_name (string): name of the week day with the best sales, e.g. "Monday"
    best day total (float): total $ sold on the best day
    """

    print(f"the weekly total was ${week_total:.2f}")
    print(f"the best day was {best_day_name} with a total sales of ${best_day_total:.2f}")


best_day = ""
best_day_sales = 0
weekly_total = 0

# look at the sales for each day
for day, day_sales in weekly_sales.items():
    
    day_total = calculate_sale_total(day_sales, prices)

    #track the total for the week
    weekly_total += day_total

    # track the best day's sales
    if day_total > best_day_sales:
        best_day = day
        best_day_sales = day_total


print_week_summary(weekly_total, best_day, best_day_sales )


