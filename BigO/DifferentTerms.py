def print_items(a,b): # O(a + b)
    for i in range(a): # for loop runs a times
        print(i) # printing takes O(1) time

    for j in range(b):  # for loop runs b times
        print(j)

print_items(1, 10)
