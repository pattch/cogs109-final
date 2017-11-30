import re, sys
import spacy

pattern = re.compile('[\W_]+')
infile = 'smsspamcollection/SMSSpamCollection'
outfile = 'smsspamcollection/cleanedcollection'
nlp = spacy.load('en')

if len(sys.argv) > 1:
    infile = sys.argv[1]
    outfile = outfile[0] + 'cleaned'
print('Processing',infile)

def process_lyrics(l):
    c,words = l.strip().split('\t',1)
    spam = '0'
    if 'spam' == c.lower():
        spam = '1'
    lemmatized = [pattern.sub('',token.lemma_) for token in nlp(words) if not token.is_stop]
    lemmatized = ' '.join([word for word in lemmatized if word])
    return spam + ':' + lemmatized

with open(infile) as f:
    lyrics = [process_lyrics(l) for l in f]

print('Finished Processing. Writing to',outfile)
print(len(lyrics))
with open(outfile,'w') as f:
    for l in lyrics:
        # print(l)
        f.write(l + '\n')
