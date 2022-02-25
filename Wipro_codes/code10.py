
def find_unique_numbers(numbers):
    return [i for i in numbers if numbers.count(i) == 1]

if __name__ =="__main__":
    print(find_unique_numbers([1,2,1,3]))
