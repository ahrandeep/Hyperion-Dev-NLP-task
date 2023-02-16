'''
HYPERION DEV BOOTCAMP TASK

Requires spacy and english language model installed via 2 commands:
pip3 install spacy
python -m spacy download en_core_web_md
'''
import spacy

# english language model
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("purr")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word1.similarity(word4))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


'''
'cat' and 'monkey' are most similiar as they are both animals
'banana' and 'monkey' are more similar than 'banana' and 'cat' likely because monkeys are known to eat bananas
It is interesting that the model matches well known associations rather than just via categories

I added in a 4th word 'purr' to check with 'cat' and it had a similarity of 0.77 which illustrates how well the model is able to associate words together
'''

'''
Must use 'en_core_web_md' over 'en_core_web_sm' as _sm has no word vectors loaded
It therefore gives inaccurate results which differ greatly from _md
'''