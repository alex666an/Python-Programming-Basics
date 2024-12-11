pens_price_per_piece = 5.8
markers_price_per_piece = 7.2
cleaning_liquid_price_per_litre = 1.2
pen_count = int(input())
marker_count = int(input())
litres_cleaning_liquid = int(input())
discount_percentage = int(input())
pens_price = pens_price_per_piece * pen_count
markers_price = markers_price_per_piece * marker_count
cleaning_liquid_price = cleaning_liquid_price_per_litre * litres_cleaning_liquid
supplies_price = pens_price + markers_price + cleaning_liquid_price
discount_size = supplies_price * discount_percentage / 100
money_needed = pens_price + markers_price + cleaning_liquid_price \
               - discount_size
print(money_needed)




