#Program  for Cost & Selling price...
"""
Take 2 inputs CP & SP of a product from the user and return following:-
(i) Profit from this Sell
(ii) What should be the selling price if we want to increase profit by 5%.
"""
SP = float(input("Enter the Cost Price of the product :  "))
CP = float(input("Enter the Selling Price of the product: "))
profit = SP - CP
newSelling_price = 1.05 * profit + CP
print("Profit will be : ",profit)
print("New Selling Price after increasing profit by 5% : ",newSelling_price)