
REGULAR_PRICE = 185  
DISCOUNT_PERCENTAGE = 60  


num_fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
num_day_old_loaves = int(input("Enter the number of day-old loaves purchased: "))


regular_price = (num_fresh_loaves + num_day_old_loaves) * REGULAR_PRICE
amount_new_loaves = num_fresh_loaves * REGULAR_PRICE
amount_day_old_loaves = num_day_old_loaves * (REGULAR_PRICE * (1 - DISCOUNT_PERCENTAGE / 100))
total_amount = amount_new_loaves + amount_day_old_loaves


print(f"Regular Price:          Rs.{regular_price:.2f}")
print(f"Amount of new loaves:   Rs.{amount_new_loaves:.2f}")
print(f"Amount of day-old loaves: Rs.{amount_day_old_loaves:.2f}")
print(f"Total amount:           Rs.{total_amount:.2f}")
