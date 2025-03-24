def high_and_low(numbers):
    # numbers = [int(x) for x in number.split()]

    # numbers = f"{min(numbers)} {max(numbers)}"
    
    return f"{max([int(x) for x in numbers.split()])} {min([int(x) for x in numbers.split()])}"