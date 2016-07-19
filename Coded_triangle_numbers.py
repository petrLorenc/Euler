
alfa = "abcdefghijklmnopqrstuvwxyz"

def char_position(letter):
    return alfa.index(letter.lower()) + 1

def pos_to_char(pos):
    return alfa[pos]


def get_triangle_num(th) :
    return 0.5 * ( th * ( th+1 ) )


list = [ 1 ]

def get_dict_of_triagle_number(limit):
    if limit > max(list):
        for x in range(max(list), limit + 1 , 1):
            list.append(get_triangle_num(x))
    return (limit in list)

def get_list_of_words():
    a_file = open("p042_words.txt", encoding="utf-8")
    a_line = a_file.read()

    list_of_word = [elem.replace("\"","") for elem in a_line.split("\",\"")]
    # print(list_of_word)
    return  list_of_word


if __name__ == "__main__":
    triangle_number = 0
    list_of_words = get_list_of_words();
    for word in list_of_words:
        value_of_word = 0
        for letter in word:
            value_of_word += char_position(letter)
        if get_dict_of_triagle_number(value_of_word):
            triangle_number += 1

    print(triangle_number)

    # value_of_word = 0
    # for letter in "SKY":
    #     print(char_position(letter))
    #     value_of_word += char_position(letter)
    #
    # print(value_of_word)
    # print(get_dict_of_triagle_number(value_of_word))












