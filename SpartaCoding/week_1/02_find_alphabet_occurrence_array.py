def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for str_data in string:
        str_inx = 0
        if str_data.isalpha():
            str_inx = ord(str_data)
            str_inx = str_inx - ord('a')
            alphabet_occurrence_array[str_inx] += 1
    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
