def hotel_cost(nights):
    return 140*nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 1000000
        
        
def rental_car_cost(days):
    cost = days * 40
    if 3 < days >= 7:
        cost -= 50
    elif 7 > days >= 3:
        cost -= 20
    return cost
    
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)+spending_money
