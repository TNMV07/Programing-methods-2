#excercise1
print("Exercise 1- Min, Max, Average")
import math
readings=[23.1,26.4,21.8,29.3,25.0]
print("The max value is: ",max(readings))
print("The min value is: ",min(readings))
print("The average value is: ", round(sum(readings)/5,2))
#excercise 2
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
if __name__ == "__main__":
    print("Exercise 2- Search for a Robot ID")
    robot_ids = [42, 17, 83, 5, 61, 29, 74, 11, 55, 38]
    target = 61
    idx_linear = linear_search(robot_ids, target)
    print(f"[Linear] target={target}, index={idx_linear}")
    sorted_ids = sorted(robot_ids)
    idx_binary = binary_search(sorted_ids, target)
    print(f"[Binary] target={target}, index={idx_binary} (list đã sort: {sorted_ids})")
