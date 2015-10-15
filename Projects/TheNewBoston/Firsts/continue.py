numbersTaken = [2, 5, 12, 7, 9, 1]

print("Here are the numbers that ar still avaliable: ")

for n in range(1, 20):
    if n in numbersTaken:
        continue
    print(n)