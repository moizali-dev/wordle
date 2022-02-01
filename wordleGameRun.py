# TODO: Fix logic bugs: lares (xxxyy) -> shine (ygxxg) -> these (ggxgg) -> those (ggggg)
# TODO: Run scoring function for each step to figure out top word
# TODO: Convert code to OOP vs Functional Programming
# TODO: Get information from website automatically
# TODO: Input information from website automatically
# TODO: Save results

#####################
#### Wordle Game ####
#####################

from english_words import english_words_set
word_lst = english_words_set

f = open('wordlist.txt', "r")

word_lst = []
for i in f.readlines():
    word_lst.append(i.strip().lower())

# Get a list of words that are 5 letters
five_letter_word_lst = []

for i in word_lst:
    if len(i) == 5:
        five_letter_word_lst.append(i.lower())


# Repeat game until condition met (game only allows 5 tries)
tries = 0
win = False
condition = True

updated_lst = five_letter_word_lst.copy()

while condition:

    val = input("Enter your guess: ")
    print(val)

    # g is green, y is yellow and x is grey

    result = input("Enter your 5 digit result (x, y, g, or ----): ")
    print(result)

    # update green, yellow and grey list

    green_idx = []
    yellow_letters = []
    yellow_idx = []
    grey_letters = []

    for i in range(len(result)):
        if result[i] == "g":
            green_idx.append(i)

        if result[i] == "y":
            yellow_letters.append(val[i])

        if result[i] == "y":
            yellow_idx.append(i)

        if result[i] == "x":
            grey_letters.append(val[i])

    # update list of words


    new_lst = []
    for i in updated_lst:

        lst = []
        for g in green_idx:
            if  i[g] == val[g]:
                lst.append(True)

        yellow_check = True
        for y in yellow_idx:
            if i[y] == val[y]:
                yellow_check = False

        if all([char in i for char in yellow_letters]) and not any([char in i for char in grey_letters]) and len(lst) == len(green_idx) and yellow_check:
            new_lst.append(i)

    updated_lst = new_lst

    if len(green_idx) == 5:
        win = True

    tries += 1

    if tries > 4 or win == True:
        condition = False

    print(new_lst)