# While Loop
i = 1
while i <= 5:
    print(i)
    i += 1   # increase value of i

# Example 
password = ""
while password != "python123":
    password = input("Enter your password: ")

print("Access Granted!")  # it's not a part of loop

# # Infinite loop
# i = 1
# while i <= 5:
#     print(i)
#     # forgot to increase i → this becomes infinite loop