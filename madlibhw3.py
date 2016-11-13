# Ethan Jannott
# ejannott
# 22235024

# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

import nltk
from nltk.book import *
import math
import random

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

print("START*******")
print('- - - - - - - - - - - - - ORIGINAL TEXT - - - - - - - - - - - - -')
first150words = text2[11:161]
# Mend the words together into a 'paragraph' format
originalText = ' '.join(first150words)
print (originalText)

# Turn original text into tokens
tokens = nltk.word_tokenize(originalText) # makes a string a list of substrings - breaks sentences up
tagged_tokens = nltk.pos_tag(tokens) # Tagged list of tokens

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","AV":"an adverb","JJ":"an adjective"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"AV":.1,"JJ":.1}

final_words = []
for (word, tag) in tagged_tokens:
 	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
 		final_words.append(spaced(word))
 	else:
 		new_word = input("Please enter %s:\n" % (tagmap[tag]))
 		final_words.append(spaced(new_word))

print('\n- - - - - - - - - - - - - - NEW TEXT - - - - - - - - - - - - - -')
print ("".join(final_words))

print("\n\nEND*******")
