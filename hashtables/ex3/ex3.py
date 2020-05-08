def intersection(arrays):

    #return numbers that appear in all lists 
    #if number is same as number of lists, true

    length = len(arrays)

    ht = {k:1 for k in arrays[0]}


    arrays = [x for x in arrays if arrays.index(x) != 0]


    for i in arrays:
        for j in ht:
            if j in i:
                ht[j] += 1

    print(ht)
    print(length)
    print([x for x in ht if ht[x] == length])
    return [x for x in ht if ht[x] == length]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
