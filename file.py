import time

n = int(input('Enter number of last range: '))
s = 0
i = 1
while i <= n:
    s = i + s
    i += 1
print(f'Sum 1 to {n}: ', s)
time.sleep(3)

my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    print(f"Element {my_list[i]} got index {i}")

