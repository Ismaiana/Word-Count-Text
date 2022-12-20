"""Count words in file."""

data = open("test.txt")


dict_count = {}

def word_count(data):



    for line in data:

        words = line.split(" ")

        for word in words:


            dict_count[word] = dict_count.get(word, 0) + 1

    for word , value in dict_count.items():

        print(f"{word} {value}")     
    

word_count(data)




