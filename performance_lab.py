# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None
    
    counts = {}

    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    return max(counts, key=counts.get)

print("Test 1:")
print("")
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Expected: 3
print(most_frequent([]))                     # Expected: None
print(most_frequent([1, 2, 3, 4]))           # Expected: 1 (or any number in the list)
print(most_frequent([2, 2, 3, 3]))           # Expected: 2 or 3
print(most_frequent([7]))                    # Expected: 7
print("")
print("")



"""
Time and Space Analysis for problem 1:
- Best-case: O(1)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)

- Why this approach? 
Using a dictionary allows each number to be counted in one pass through the list, making it efficient and easy to understand. 
The lookups and updates take constant time on average, so the overall performance grows linearly with the size of the input, 
which matches the description of an effective O(n) solution.

- Could it be optimized? 
No because this solution already has linear time O(n), 
which is the most efficient possible because every element must be checked at least once. 
The algorithm’s growth is directly proportional to input size, and that’s expected for this type of problem.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    unique_list = []
    seen = set()

    for num in nums:
        if num not in seen:
            unique_list.append(num)
            seen.add(num)
    
    return unique_list

print("Test 2:")
print("")
print(remove_duplicates([4, 5, 4, 6, 5, 7]))   # Expected: [4, 5, 6, 7]   
print(remove_duplicates([]))                   # Expected: []
print(remove_duplicates([1, 2, 3, 4]))         # Expected: [1, 2, 3, 4]
print(remove_duplicates([9, 9, 9, 9]))         # Expected: [9]
print("")
print("")


"""
Time and Space Analysis for problem 2:
Best-case: O(n)
Worst-case: O(n)
Average-case: O(n)
Space complexity: O(k) distinct elements, up to O(n)

Why this approach? 
A set gives constant-time membership on average, so one pass preserves first-seen order with simple appends.

Could it be optimized? 
Not asymptotically. Any order-preserving method must scan the list. Sorting would change order and cost O(n log n).
Using a list instead of a set for membership would degrade to O(n^2).
"""




# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    pairs = []
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

print("Test 3:")
print("")
print(find_pairs([1, 2, 3, 4], 5))                  # Expected: [(1, 4), (2, 3)]
print(find_pairs([], 5))                            # Expected: []
print(find_pairs([7], 7))                           # Expected: []
print(find_pairs([-2, 0, 2, 4], 2))                 # Expected: [(-2, 4), (0, 2)]
print(find_pairs([4, 5, 6], 10))                    # Expected: [(4, 6)]
print("")
print("")



"""
Time and Space Analysis for problem 3:
Best case: O(n)
Worst case: O(n)
Average case: O(n)
Space complexity: O(n)

Why this approach?
A single pass with a set gives linear time and preserves uniqueness by only pairing with previously seen values

Could it be optimized?
Not asymptotically for unsorted input; if the list were already sorted a two-pointer scan would be O(n) time with O(1) extra space, but sorting first would raise time to O(n log n)
"""



# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    arr = []

    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            print(f"Copying {size} items to new list...")

            capacity *= 2
    
        arr.append(i)
        size += 1

print("Test 4:")
print("")
add_n_items(1)              # (No resizing messages, since capacity starts at 1)
print("")
add_n_items(2)              # Resizing from 1 to 2, Copying 1 items to new list...
print("")
add_n_items(6)              # Resizing from 1 to 2, Copying 1 items to new list..., Resizing from 2 to 4, Copying 2 items to new list..., Resizing from 4 to 8, Copying 4 items to new list...
print("")
add_n_items(10)             # Expected Output: ,Should print resizing messages for 1→2, 2→4, 4→8
print("")
add_n_items(0)              # Expected Output: ,(No output at all)
print("")
print("")
print("")



"""
Time and Space Analysis for problem 4:
- When do resizes happen? 
When size equals capacity; capacity then doubles

- What is the worst-case for a single append? 
O(n) when an append triggers a resize and all current elements are copied.

- What is the amortized time per append overall?
O(1) amortized, since total copies over n appends form a geometric series bounded by ~2n.

- Space complexity:
O(n) for stored items; during a resize there is a brief peak near 2n, which is still linear.

- Why does doubling reduce the cost overall?
Because each element is copied only a logarithmic number of times across the whole growth sequence; 
summing the work over n appends stays linear, making the average cost per append constant.

"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    totals = []
    current_sum = 0

    for num in nums:
        current_sum += num
        totals.append(current_sum)
    return totals

print("Test 5:")
print("")
print(running_total([1, 2, 3, 4]))        # Expected: [1, 3, 6, 10]
print(running_total([]))                  # Expected: []
print(running_total([7]))                 # Expected: [7]
print(running_total([-1, 2, -3, 4]))      # Expected: [-1, 1, -2, 2]
print(running_total([0, 0, 0]))           # Expected: [0, 0, 0]
print(running_total([5, -2, 3, -1, 4]))   # Expected: [5, 3, 6, 5, 9]
print(running_total(list(range(1, 11))))  # Expected: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
print("")
print("")

"""
Time and Space Analysis for problem 5:
Best-case: O(n)
Worst-case: O(n)
Average-case: O(n)
Space complexity: O(n)

Why this approach?
It efficiently computes running sums in one pass with constant-time updates per element, making it simple, predictable, and scalable for larger inputs

Could it be optimized?
Only by modifying the input list in place to reuse memory, but the time complexity would remain O(n)
"""

