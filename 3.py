import time
user_input = input("Do you want to print a countdown? (yes/no): ").lower()

if user_input == "yes":
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
elif user_input == "no":
    print("Maybe next time!")
else:
    print("Invalid input!")
