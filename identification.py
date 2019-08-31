import glob
import json
import os
import re
import sys



"""
print(sys.argv[0])
"""






"""
with open(path_turkish_extended) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line

content = [x.strip() for x in content]
"""



text = sys.argv[1]

def load_languages():
    #LOADING LANGUAGES WORDS
    languages_words = {}
    for path in glob.glob("/home/heyo/all_codes/UKPapplication/most-common-words-by-language/src/resources/*"):
        with open(path) as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        
        content = [x.strip() for x in content]
        print(os.path.basename(path))
        language_name = os.path.basename(path)[:-4]
        languages_words[language_name] = content[0:4000]
    return languages_words





#languages_words = load_languages()
#identify_language = "Hey, What do you want to say to me?"



#REGEX TOKENS WITHOUT NLTK
def tokenize(text):
    tokens_regex = re.findall(r"[\w']+", text)
    tokens_regex = [token.lower() for token in tokens_regex]
    return tokens_regex


#LANGUAGE IDENTIFICATION
def identify_language(text, languages_words):
    tokens_regex = tokenize(text)
    lang_occurence_list = []
    word_frequency_index_list = []
    for lang in languages_words.keys():
        language_list = list(languages_words.keys())
        print(lang)
        lang_occurence = 0
        word_list = languages_words[lang]
        word_frequency_index = []
        for elem in tokens_regex:
            #print(elem)
            if elem in word_list:
                lang_occurence = lang_occurence + 1
                word_frequency_index.append(word_list.index(elem))
        word_frequency_index_list.append(word_frequency_index)
        lang_occurence_list.append(lang_occurence)
    if lang_occurence_list.count(max(lang_occurence_list)) > 1:
        max_equal_occurences = [i for i, j in enumerate(lang_occurence_list) if j == max(lang_occurence_list)]
        total_minimum_word_index = min(word_frequency_index_list[max_equal_occurences[0]])
        total_minimum_lang_index = max_equal_occurences[0]
        for lang_index in max_equal_occurences[1:]:
            minimum_word_index = min(word_frequency_index_list[lang_index])
            if minimum_word_index < total_minimum_word_index:
                total_minimum_word_index = minimum_word_index
                total_minimum_lang_index = lang_index
        print(language_list)
        print(total_minimum_lang_index)
        print("The Language is " + language_list[total_minimum_lang_index])
    else:
        print(lang_occurence)
            
    
        max_equal_occurences = [i for i, j in enumerate(lang_occurence_list) if j == max(lang_occurence_list)]
        print("Occurence of the max" + str(lang_occurence_list.count(max(lang_occurence_list))))
        print(lang_occurence_list.index(max(lang_occurence_list)))
        most_occurred = lang_occurence_list.index(max(lang_occurence_list))
        print("The Language is " + language_list[most_occurred])


def main():
    languages_words = load_languages()
    identify_language(text, languages_words)


if __name__ == "__main__":
    text = sys.argv[1]
    print(sys.argv)
    languages_words = load_languages()
    identify_language(text, languages_words)
    #IF MULTIPLE GET OCCURENCES OF LIST 
#indices = [i for i, x in enumerate(my_list) if x == "whatever"]





