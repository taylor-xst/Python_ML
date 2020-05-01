price = 24.95 * (1-0.4)

first_trans_fee = 3
other_trans_fee = 0.75
n = 60

sum = price + first_trans_fee + (n - 1) * (price + other_trans_fee)
print sum