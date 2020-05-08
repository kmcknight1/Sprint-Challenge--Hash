def has_negatives(a):

    #return empty list if no negatives found
    #if negatives found, return list with those numbers (no repeats)
    #only return positive numbers that have a corresponding negative

    #make hash table with k(number):v(0) if number > 0
    result = {k:0 for k in a if k > 0}
    for i in a:
        #if the number is negative, and there is an occurrance of the absolute value in our hashtable, make it True
        if i < 0 and result[abs(i)] == 0:
            result[abs(i)] = True
        
    #reutrn list of True values from the ht
    return [x[0] for x in result.items() if x[1]]


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
