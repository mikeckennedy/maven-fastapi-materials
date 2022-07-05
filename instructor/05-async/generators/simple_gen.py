def fib(n: int) -> list[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)

    return numbers


result = fib(5)

for n in result:
    print(n, end=', ')

print()
print("Done")
