# 1, 1, 2, 3, 5, 8, 13, 21, ...


def og_fib(n: int) -> list[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)

    return numbers


def fib():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


result = fib()

for num in result:
    print(num, end=', ')
    if num > 10_000:
        break

print()
print("Done")
