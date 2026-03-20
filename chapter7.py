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
#excercise: The swarm collision crisis
print("Excercise: The swarm collision crisis")
class Robot: 
    def __init__(self, x, y): 
        self.x, self.y = x, y 
def check_proximity(robots, limit=0.5): 
    pairs = []
    n = len(robots) 
    for i in range(n): 
        for j in range(i + 1, n): 
            dx =robots[i].x - robots[j].x
            dy =robots[i].y - robots[j].y
            dist = (dx**2 + dy**2)**0.5 
            if dist < limit: 
                pairs.append((i, j))  # store pair 
    return pairs
robots = [
    Robot(0, 0),
    Robot(0.3, 0.3),
    Robot(2, 2)
    ]
print(check_proximity(robots, limit=0.5))
#excercise: Binary search in robotics
print("Excercise: Binary search in robotics")
def binary_search(distances,target):
    left=0
    right= len(distances)-1
    while left<=right:
        mid=(left+right)//2
        if distances[mid]==target:
            return mid
        elif distances[mid]<target:
            left= mid +1
        else:
            right= mid-1
    return-1
distances= [0.5, 1.0, 1.5, 2.0, 2.5]
forces= [10, 20, 30, 40, 50]
idx= binary_search(distances=distances,target=2.0)
if idx !=-1:
    print("Forces: ",forces[idx])
#excercise: The "Max Alert" system
print("Exercise: The 'Max Alert' system")
def max_alert(temps,limit=80.0):
    if not temps:
        print("No data")
        return None
    max_temp=temps[0]
    fault=temps[0]>limit
    for t in temps[1:]:
        if t>max_temp:
            max_temp=t
        if t>limit:
            fault=True
    if fault:
        print("Cooling system fault")
    else:
        print("Cooling system OK")
    return max_temp
temps=[50.1, 60.0, 90.5, 64.8, 85.2]
m=max_alert(temps,limit=80.0)
print("Max_temp: ",m)
#excercise: selection sort
print("Excercise: selection sort")
def selection_sort(data):
    result=data.copy()
    n=len(result)
    for i in range(n):
        min_idx=1
        for j in range(i+1,n):
            if result[j]<result[min_idx]:
                min_idx=j
        result[i],result[min_idx]=result[min_idx],result[i]
    return result
list=[3.5,1.2,4.8,0.9,2.1]
sorted_list=selection_sort(list)
print("Original list: ",list)
print("Sorted list: ",sorted_list)