def PrefixFrequency(string):
        LIMIT = string.split()[0]
        return list(reversed([string.count(string[: i + 1]) for i in range(len(LIMIT))]))
  
def LongestCommonPrefix(string):
    max_frq =  max(PrefixFrequency(string))
    return string[: len(string.split()[0]) - PrefixFrequency(string).index(max_frq) ]
  
print(LongestCommonPrefix("apple ape april" ))