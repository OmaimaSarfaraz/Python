# Number Pairs
for i in range(1, 4):          # outer loop
    for j in range(1, 4):      # inner loop
        print(i, j)




# Multiplication Table (1–3)
for i in range(1, 4):        # outer loop (row)
    for j in range(1, 11):   # inner loop (col)
        print(i, "x", j, "=", i*j)
    print("------")   # separator after each table