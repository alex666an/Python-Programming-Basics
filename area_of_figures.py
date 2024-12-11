import math
figure = str(input())
if figure == 'square':
    side = float(input())
    square_area = side * side
    print(f'{square_area:.3f}')
elif figure == 'rectangle':
    side_one = float(input())
    side_two = float(input())
    rectangle_area = side_one * side_two
    print(f'{rectangle_area:.3f}')
elif figure == 'circle':
    radius = float(input())
    circle_area = math.pi * (radius ** 2)
    print(f'{circle_area:.3f}')
elif figure == 'triangle':
    side = float(input())
    height = float(input())
    triangle_area = (side * height) / 2
    print(f'{triangle_area:.3f}')