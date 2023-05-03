# your code goes here!
# possible_anagrams = ['enlists', 'google', 'inlets', 'banana']

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, options):
        word_list = [letter for letter in self.word]
        result_list = []
        for option in options:
            option_list = [letter for letter in option]
            if sorted(word_list) == sorted(option_list):
                result_list.append(option)
            else:
                pass

        return result_list

    
