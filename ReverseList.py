def reverse_list(input_list):
    reversed_list = []
    # Iterate over input_list in reverse order
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list

# Example usage:
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(f"Original List: {original_list}")
print(f"Reversed List: {reversed_list}")
