num = int(input())
print(f"+ {'- ' * (num - 2)}+")
for a in range(num - 2):
    print(f"| {'- ' * (num - 2)}|")
print(f"+ {'- ' * (num - 2)}+")
