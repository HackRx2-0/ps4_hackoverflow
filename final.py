import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords, wordnet
from nltk.stem.porter import PorterStemmer

def empty_set(some_set):
    return some_set == set()

tokenizer = RegexpTokenizer(r'\w+')
p_stemmer = PorterStemmer()

df = pd.read_csv ('internal.csv')
ls = df['Word'].tolist()

words = []

# ENTER QUERY HERE
subs = 'buy phone'
#res1 = list(i for i in ls if subs in i)
FINAL = []
FINAL.append([i for i in ls if subs in i])
print(FINAL)
#if empty_set(res1) == False: print (str(res1))

raw = subs.lower()
tokens = tokenizer.tokenize(raw)
stop_words = set(stopwords.words('english'))
stopped_tokens = [subs for subs in tokens if not subs in stop_words]

words.append(stopped_tokens)

#words = subs.split()
for each in words:
    for subs in each:
        #res = set(i for i in ls if subs in i)
        #if empty_set(res) == False: 
        FINAL.append([i for i in ls if subs in i])
            #print (str(res), end=',')
        i=1
        if i==0:
            synonyms = []
            for syn in wordnet.synsets(subs):
                #print(syn)
                for l in syn.lemmas():
                    synonyms.append(l.name())
            
            final = list(dict.fromkeys(synonyms))
            for new in final:
                #res = set(i for i in ls if subs in i)
                FINAL.append([i for i in ls if subs in i])
            #print(final)

print(FINAL)