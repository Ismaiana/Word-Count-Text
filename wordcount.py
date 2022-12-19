"""Count words in file."""
import sys
# filename = test.txt
# fp = open(test.txt)

data = open("test.txt")




dict_count = {}

def word_count(data):

    
   for line in data:

        words = line.split()

        for words in data:
        
            if words not in dict_count:
            
                dict_count[words] = 1

            else:

                dict_count[words] += 1
            
            
        return dict_count

print(word_count(data))






# for loop to go over the lines 
# we want the if stat to take each word and assign it as a key with val 1
# we want anything else to check if there's a key and assign value 