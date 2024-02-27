#!/usr/bin/env python3
"""
split the sentences from a directory
"""
import os
import sys

import spacy
nlp = spacy.load("en_core_web_sm")

directory = "data"

if len(sys.argv) > 1:
    directory = sys.argv[1]

#print(directory)

# Construction via add_pipe
sentencizer = nlp.add_pipe("sentencizer")

# Construction from class
#from spacy.pipeline import Sentencizer
#sentencizer = Sentencizer()

for fname in os.listdir(directory):
    with open(os.path.join(directory, fname)) as f:
        for line in f:
            #print(line.strip())
            doc = nlp(line)
            for sent in doc.sents:
                print(fname, sep="\t")
                print(sent)
            
