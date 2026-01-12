import argparse
import rust_sort

parser = argparse.ArgumentParser(description="A script that processes user values.")
parser.add_argument("technique", type=str, help="The name of the user (a required string)")
# Parse the arguments from the command line
techniqueparsed = parser.parse_args()

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 1. Divide: Find the midpoint
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 2. Conquer: Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Picking the middle element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def quicksort_inplace(arr, low, high):
    if low < high:
        # p is the partitioning index
        p = partition(arr, low, high)
        
        # Separately sort elements before and after partition
        quicksort_inplace(arr, low, p)
        quicksort_inplace(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]
        
def get_dataset_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the entire content
            content = file.read()
            
            # Split by any whitespace and convert to integers
            dataset = [int(x) for x in content.split()]
            
        return dataset
    except FileNotFoundError:
        return "Error: The file was not found."
    except ValueError:
        return "Error: The file contains non-numeric data."     
        





def main():        
    # 1. Load the data
    my_data = get_dataset_from_file('dataset.txt')

    match (techniqueparsed.technique):
        case ("merge"):
            sorted_data = merge_sort(my_data)
            # print(sorted_data)
        case ("quick"):
            sorted_data = quicksort(my_data)
            # print(sorted_data)
        case ("rmerge"):
            sorted_data = rust_sort.merge_sort(my_data)
            # print(sorted_data)

        case ("tim"):
            sorted_data = sorted(my_data)
            # print(sorted_data)

        case (_):
            sorted_data = quicksort(my_data)
            # print(sorted_data)
            print("Defaulted to quicksort")


















if __name__ == "__main__":
    main()