start = 9
end = 101

print("For:")
for i in range(start, end + 1):
    if i % 2 == 1:
        print(i)


print("While:")
i = start
while i <= 101:
    if i % 2 == 1:
        print(i)
    i += 1
