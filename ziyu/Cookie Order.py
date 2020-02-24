Cookies, Cost_of_cookies, Shipping_fee, Total = 0, 0, 0, 0,

cookies_cost = 5.5
unitprice = 0.85
fixedrate = 1.75

print("Enter the pounds of cookies you want to order: ", end="")
Cookies = eval(input())

Cost_of_cookies= cookies_cost*Cookies
Shipping_fee = unitprice*Cookies+fixedrate
Total = Cost_of_cookies+Shipping_fee

print ("payment information: ")
print("         \tCost of cookies:\t$", format(Cost_of_cookies, "0.2f"))
print("         \tShipping fee:\t$", format(Shipping_fee, "0.2f"))
print("         \tTotal due:\t$", format(Total, "0.2f"))
