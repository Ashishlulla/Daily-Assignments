def find_max_sum(numbers):
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1+max2

if __name__ == "__main__":
    print(find_max_sum([5,9,7,11]))
