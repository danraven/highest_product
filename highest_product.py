import math
import argparse
from typing import List

def smallest_index(l: List[int]) -> int:
    i_min = 0
    for i, val in enumerate(l[1:]):
        if (val < l[i_min]):
            i_min = i + 1
    return i_min

def highest_product(nums: List[int], size: int=3) -> int:
    # Sanity checks: numbers to check cannot be lower than 2, and the list cannot be smaller than the numbers required
    if size < 2:
        raise ValueError("Size must be at least 2")
    if len(nums) < size:
        raise ValueError("List of numbers must be at least the given size (%d)" % size)
    # If the list is exactly the size, its elements yield the highest product by default
    if len(nums) == size:
        return math.prod(nums)
    largest = nums[:size]
    min_index = smallest_index(largest)
    for n in nums[size:]:
        if n <= largest[min_index]:
            continue
        largest[min_index] = n
        min_index = smallest_index(largest)
    return math.prod(largest)

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs="+", help="List of numbers", type=int)
    parser.add_argument("-s", "--size", help="Number of highest numbers to multiply", type=int, default=3)
    args = parser.parse_args()
    print(highest_product(args.numbers, args.size))

if __name__ == "__main__":
    run()