def average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers) if len(numbers) else None

print(average([]))
