#
# Given array of bag weights, janitor can carry bags as long as combined weight is less than 3.00
# Find # of trips that need to be completed.
# E.g. [1.01, 1.99, 2.5, 1.5, 1.1] will take 3 trips


arr = [1.01, 1.99, 2.50, 1.50, 1.10, 0.29, 0.10]
trips = 1
bal = 3.00

for x in arr:
    if bal < x:
        trips = trips + 1
        bal = 3.00 - x

    else:
        bal = bal - x


print("Trips ", trips)
