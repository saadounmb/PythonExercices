def bubble_sort(arr):
    n = len(arr)
    steps = []
    
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                steps.append(list(arr))  # Record each step of the sort
        if not swapped:
            break
    
    return arr, steps

# Function to visualize sorting steps
def visualize_steps(steps):
    for i, step in enumerate(steps):
        print(f"Step {i+1}: {step}")

# Prompting the user to enter a list of numbers
input_str = input("Enter a list of numbers separated by spaces: ")
arr = list(map(int, input_str.split()))

# Prompting the user to choose a sorting algorithm
print("Choose a sorting algorithm:")
print("1. Bubble Sort")
# Add more sorting algorithms as needed

choice = int(input("Enter your choice (1 for Bubble Sort): "))

# Sorting the list using the chosen algorithm
if choice == 1:
    sorted_arr, steps = bubble_sort(arr)
    print("\nSorted list:", sorted_arr)
    visualize_steps(steps)
else:
    print("Invalid choice. Please enter a valid option.")
