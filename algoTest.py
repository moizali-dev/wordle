from tqdm import tqdm

f = open('wordlist.txt', "r")

word_lst = []
for i in f.readlines():
    word_lst.append(i.strip().lower())

len(word_lst)

# Get a list of words that are 5 letters
five_letter_word_lst = []

for i in word_lst:
    if len(i) == 5:
        five_letter_word_lst.append(i.lower())

len(five_letter_word_lst)

# Find list of words that have the max vowels in there

vowels = ['a','e','i','o','u']

dic_vowel = {}

for i in five_letter_word_lst:
    count = 0
    for v in vowels:
        if v in i:
            count += 1

    dic_vowel[i] = count

dic_vowel_sorted = {k: v for k, v in sorted(dic_vowel.items(), key=lambda item: item[1], reverse=True)}
dict_vowel_items = dic_vowel_sorted.items()
vowtoplst = list(dict_vowel_items)[:20]
print(vowtoplst)

# If you start with one word then how many points does that word get

lst = five_letter_word_lst

dic = {}

for i in tqdm(lst):
    count = 0
    for j in lst:
        if i != j:
            for idx, l in enumerate(i):
                if i[idx] == j[idx]:
                    count += 3
                elif l in j:
                    count += 1

    dic[i] = count

dic_sorted = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=False)}

#Print top N k,v pairs

dict_items = dic_sorted.items()
toplst = list(dict_items)[:50]
print(toplst)

