def count_anagram_words(query,dictionary):
    query_count = []
    for i_1,s1 in enumerate(query,start=0):
        counter = 0
        for i_2,s2 in enumerate(dictionary,start=0):
            if sorted(s1) == sorted(s2):
                counter = counter + 1
        query_count.append(counter)
    print(query_count)
