import random as r
words = [i for i in open("python/wordle/dictionary.csv", "r").read().split("\n")]

def find_word(word, word_list):
    answer = input(f"enter {word.lower()} (grey(1)/yellow(2)/green(3)): ")
    c_0 = (int(answer[0]), 0)
    c_1 = (int(answer[1]), 1)
    c_2 = (int(answer[2]), 2)
    c_3 = (int(answer[3]), 3)
    c_4 = (int(answer[4]), 4)

    returned_list = letter_finding(word, c_0, word_list)
    returned_list = letter_finding(word, c_1, returned_list)
    returned_list = letter_finding(word, c_2, returned_list)
    returned_list = letter_finding(word, c_3, returned_list)
    returned_list = letter_finding(word, c_4, returned_list)

    return returned_list

        # 120 possibilitys with one word

def letter_finding(word, character, word_list):
    returning_list = []

    if len([i for i in word if i == word[character[1]]]) < 2:
        for i in word_list:
            if character[0] == 1:
                if word[character[1]] not in i:
                    returning_list.append(i)

            if character[0] == 2:
                if word[character[1]] in i:
                    if character[1] != i.index(word[character[1]]):
                        returning_list.append(i)
            
            if character[0] == 3:
                if word[character[1]] in i:
                    if character[1] == i.index(word[character[1]]):
                        returning_list.append(i)

    return returning_list

find_word("meets", words)

# # adieu
# # strow
# word_list = find_word("adieu", words)
# word_list = find_word("stroy", word_list)
# counter = 0

# while len(word_list) > 1 or counter > 3:
#     print(word_list)
#     word_list = find_word(word_list[r.randint(0, len(word_list))], word_list)
#     counter += 1

# print(f"The word is {word_list[0]}")