import re
import json

def remove_punctuation(text):
    cleaned = re.sub('[?|!|"|#|:|=|+|_|{|}|[|]|-|$|%|^|&|]','', text)
    cleaned = re.sub(r'[.|,|)|(|\|/|-|~|`|>|<|*|$|@|;|→]',r'',cleaned)
    return cleaned

def remove_urls(text):
    reg = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+';
    text = re.sub(reg, '', text)
    return text

def remove_words():
    stop_words = []
    with open('search/words/stop_words.json', 'r', encoding="utf8") as f:
        data = json.load(f)
        for i in data:
            stop_words.append(i)
    
    return stop_words

def to_lowercase(text):
    return text.lower()

# Remove numbers 
def remove_numbers(text): 
    result = re.sub(r'\d+', '', text) 
    return result 
  

def digit_to_word(num):
    units = ("", "bir ", "ikki ", "uch ", "to'rt ","besh ", "olti ", "yetti ","sakkiz ", "to'qqiz ", "o'n", "o'n bir", "o'n ikki", "o'n uch ", "o'n to'rt ", "o'n besh ","o'n olti ", "o'n yetti ", "o'n sakkiz ", "o'n to'qqiz ")
    tens =("", "", "yigirma ", "o'ttiz ", "qirq ", "ellik ","oltmish ","yetmish ","sakson ","to'qson ")
    num = int(num)
    if num < 0:
        return "minus "+digit_to_word(-num)

    if num<20:
        return  units[num] 

    if num<100:
        return  tens[num // 10]  +units[int(num % 10)] 

    if num<1000:
        return units[num // 100]  +"yuz " +digit_to_word(int(num % 100))

    if num<1000000: 
        return  digit_to_word(num // 1000) + "ming " + digit_to_word(int(num % 1000))

    if num < 1000000000:    
        return digit_to_word(num // 1000000) + "million " + digit_to_word(int(num % 1000000))

    return digit_to_word(num // 1000000000)+ "milliard "+ digit_to_word(int(num % 1000000000))

