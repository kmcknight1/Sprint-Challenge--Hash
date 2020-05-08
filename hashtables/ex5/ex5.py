def finder(files, queries):

    ht = {files.index(v):v for v in files}

    print(ht)

    result = []
    for i in range(len(queries)):
        if queries[i] in ht[i].split("/"):
            print(f'i:{i} queries[i]:{queries[i]} ht[i]:{ht[i]}')
            result.append(ht[i])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
