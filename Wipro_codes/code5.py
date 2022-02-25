def first_unique_product(products):
    unique = []
    for i in products:
        if products.count(i) == 1:
            unique.append(i)
            break
        else:
            pass
    if len(unique) > 0:
        return unique[0]
    else:
        return None

if __name__ =="__main__":
    print(first_unique_product(["Apple", "Computer", "Apple", "bag"]))
