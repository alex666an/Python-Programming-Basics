import math
paint_boxes = int(input())
wallpaper_rolls = int(input())
gloves_price = float(input())
brush_price = float(input())

gloves = math.ceil(0.35 * wallpaper_rolls)
brushes = math.floor(0.48 * paint_boxes)

paint_cost = paint_boxes * 21.50
wallpaper_cost = wallpaper_rolls * 5.20
gloves_cost = gloves * gloves_price
brushes_cost = brushes * brush_price

total_cost = paint_cost + wallpaper_cost + gloves_cost + brushes_cost
delivery_cost = total_cost / 15

print(f"This delivery will cost {delivery_cost:.2f} lv.")

