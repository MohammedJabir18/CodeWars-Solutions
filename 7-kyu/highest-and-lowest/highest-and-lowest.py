def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split()]
    
    numbers = f"{max(numbers)} {min(numbers)}"
    
    return numbers