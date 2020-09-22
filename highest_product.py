import math
import argparse
from typing import List

def highest_product(nums: List[int]) -> int:
    size = 3
    # Sanity check, can't have a list smaller than the desired size
    if len(nums) < size:
        raise ValueError("List of numbers must be at least the given size (%d)" % size)
    # If the list is exactly the size, its elements yield the highest product by default
    if len(nums) == size:
        return math.prod(nums)
    largest = nums[:size]
    smallest = nums[:size - 1]
    min_index = largest.index(min(largest))
    max_index = smallest.index(max(smallest))
    for n in nums[size:]:
        if n > largest[min_index]:
            largest[min_index] = n
            min_index = largest.index(min(largest))
        if n < smallest[max_index]:
            smallest[max_index] = n
            max_index = smallest.index(max(smallest))
    return max(math.prod(largest), math.prod(smallest + [max(largest)]))

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs="+", help="List of numbers", type=int)
    args = parser.parse_args()
    print(highest_product(args.numbers))

if __name__ == "__main__":
    run()
