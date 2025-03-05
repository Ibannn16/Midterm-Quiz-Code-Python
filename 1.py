import time
def generate_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)
        time.sleep(0.5)

user_input = input("Do you want to generate a right-angled triangle? (yes/no): ").lower()

if user_input == 'yes' or user_input == 'y':
    generate_triangle(10)
else:
    print("Triangle generation skipped.")
