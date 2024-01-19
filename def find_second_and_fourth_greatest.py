def find_second_and_fourth_greatest(numbers):
    if len(numbers) < 4:
        return "Error: List should have at least 4 numbers."

    sorted_numbers = sorted(numbers, reverse=True)
    second_greatest = sorted_numbers[1]
    fourth_greatest = sorted_numbers[3]

    return second_greatest, fourth_greatest

# Example usage:
number_list = [int(item) for item in input().split()]
result = find_second_and_fourth_greatest(number_list)
print(result)