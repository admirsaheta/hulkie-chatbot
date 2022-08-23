## Copyright Admir Saheta | 2022
## Hulkie Bot - Alpha

import random
import json
import pickle
import numpy as np
## Neural Language ToolKit imports
import nltk 
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD 


lemetizer = WordNetLemmatizer
intents = json.loads(open('intents.json').read())
## Models
words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ","]

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.tokenize(pattern)
        words.append(word_list)
        documents.append((word_list), intent['tag'])
        if intent['tag'] not in classes: 
            classes.append(intent['tag'])
            
print(documents)