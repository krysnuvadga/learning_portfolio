import re
import sys
from collections import Counter

'''
My approach:

1. Make a list of words from both f1.txt and f2.txt.
2. Remove unwanted characters from the text input.
3. Compare the two list and remove common words from the list generated from f2.txt
4. sorting words in the list generated from f2.txt by frequency

'''

if len(sys.argv) != 3:
    print('python uncommonwords.py common.txt alice.txt')
    sys.exit(1)

with open(sys.argv[1]) as f1,open(sys.argv[2]) as f2:
    passage = f2.read()
    common = f1.read()

words = re.findall(r'\w+', passage)
common_words = re.findall(r'\w+', common)
passage_text = [words.lower() for words in words]

final_set = set(passage_text) - set(common_words) # Comparing the lists using sets
word_count = Counter([w for w in passage_text if w in final_set])

for word, count in sorted(word_count.items(), key=lambda k: -k[1]):
    print(word, " : ", count)
