n = int(input('Enter number for range: '))
s = 0
i = 1
while i <= n:
    s = i + s
    i += 1
print(f'Sum 1 to {n}: ', s)
