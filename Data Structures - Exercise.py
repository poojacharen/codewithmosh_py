# Exercise : This is a common interview question
# So let's say we have some text, write a program to find the most repeated characters in the text. And also make the code readable. So we need to import pprint function

from pprint import pprint
sentence = "This is a common interview question"

dict_frequency = {}

for dict in sentence:
    if dict in dict_frequency:
        dict_frequency[dict] += 1
    else:
        dict_frequency[dict] = 1

dict_frequency_sorted = sorted(dict_frequency.items(), key=lambda kv: kv[1], reverse=True)
print(dict_frequency_sorted[0]) # output : ('i', 5)
# pprint(dict_frequency, width=1)  # instead of print we have use pprint
