n = int(input('Enter number of last range: '))
s = 0
i = 1
while i <= n:
    s = i + s
    i += 1
print(f'Sum below numbers 1 to {n}: ', s)