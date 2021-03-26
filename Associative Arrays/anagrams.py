def anagrams(words):
    anagrams = {}
    for i in words:
        if str(sorted(i)) in anagrams:
            anagrams[str(sorted(i))].append(i)
        else:
            anagrams[str(sorted(i))] = [i]
    anagrams_list = list(anagrams.values())
    return [x for x in anagrams_list if len(x) >1] #remove lists with one item

print(anagrams(["cab", "bac", "abc", "bad", "dab", "fab"]))
# [["cab", "bac", "abc"], ["bad", "dab"]]