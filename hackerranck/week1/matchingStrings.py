def matchingStrings(strings, queries):
    # Write your code here
    result = [0 for x in queries]
    for string in strings:
        for i, query in enumerate(queries):
            if (string == query):
                result[i] += 1
                continue
    return result

strings = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb', 'ab']
res = matchingStrings(strings, queries)
print(res)