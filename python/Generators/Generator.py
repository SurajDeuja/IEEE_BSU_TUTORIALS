def first(num):
    n = 0
    while n < num:
        yield n
        n += 1

gen = first(20)

print sum(x for x in range(1, 101)) == sum(first(101))

