import time
def generate_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)
        time.sleep(0.5)
def nested_loops():
    numbers = []
    for i in range(8):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    for a in range(numbers[0]):
        for b in range(numbers[1]):
            for c in range(numbers[2]):
                for d in range(numbers[3]):
                    for e in range(numbers[4]):
                        for f in range(numbers[5]):
                            for g in range(numbers[6]):
                                for h in range(numbers[7]):
                                    print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={h}")

while True:
    username = input("Enter Sauce: ")
    password = input("Enter passCode: ")
    time.sleep(1)

    if username == "HotSauce" and password == "393878":
        print("\nLogin successful!\n")
        time.sleep(1)
        while True:
            choice = input("1 for Triangle Generator or 2 for Nested Loops: ")
            if choice == '1':
                height = int(input("Enter the height of the triangle: "))
                generate_triangle(height)
            elif choice == '2':
                nested_loops()
            else:
                retry = input("SHUCKS! Try again? (y/n): ").lower()
                if retry != 'y':
                    break

        # Restart
        restart = input("\nTry again? (yes/no): ").lower()
        if restart not in ('yes', 'y'):
            print("Sayonara! 👋")
            break
    else:
        retry_login = input("Account not found! Try again? (yes/no): ").lower()
        if retry_login not in ('yes', 'y'):
            print("GAY! 👋")
            break
