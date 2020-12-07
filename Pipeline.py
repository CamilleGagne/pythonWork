import nltk, os
from nltk import word_tokenize, sent_tokenize, ne_chunk, tag
from nltk.parse.stanford import StanfordParser
from nltk.corpus import movie_reviews

#Input
text = " "
#text = movie_reviews.raw(' / .txt')

#tokenizer
token = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
print("Sentence splitting: ", nltk.sent_tokenize(text))
print("Word tokenization: ", token)

#POS-tagger
tag = tag.pos_tag(token)
print("POS-Tagging:", tag)

#Parser
os.environ.get('CLASSPATH')
os.environ['CLASSPATH'] = "/Users/macbookaire/Desktop/Stanford/stanford-parser-full-2018-02-27"
parser=StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
sentences = (parser.raw_parse(text))
print(sentences)

#NER
print("NER:", ne_chunk(tag, binary=False))

#Parser's GUI
for line in sentences:
   for sentence in line:
       sentence.draw()


