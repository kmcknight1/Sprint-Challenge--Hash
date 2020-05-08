def get_indices_of_item_weights(weights, length, limit):
    #make hash table with key(limit-weight):value(index)
    ht = {limit-k:weights.index(k) for k in weights} 
    result = []
    for i in weights:
        if i not in ht:
            continue
        else:
            result.append(ht[i])
    #if no result found, return None
    if len(result) == 0:
        return None
    #if 2 weights are the same, find the index of the last occurrance of that weight in the weights array
    if result[0] == result[1]:
        heavier_index = ''.join([str(w) for w in weights]).rindex(str(i))
        heavier_index = int(heavier_index)
        result[0] = heavier_index
    return result
