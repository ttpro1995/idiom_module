# -*- coding: utf-8 -*-
import string
from util import *
from _collections import defaultdict
def measure_similarity(embedding_model, sentence):
    done = set()
    sentence = sentence.translate(None, string.punctuation)
    for word1 in sentence.split():
        if (word1 in embedding_model.vocab):
            for word2 in sentence.split():
                if (word1 != word2):
                    if (word2 in embedding_model.vocab):
                        if (word1, word2) not in done:
                            similarity = embedding_model.similarity(word1, word2)
                            print ('%s - %s ==> %f'%(word1, word2, similarity))
                            done.add((word1, word2))
                            done.add((word2, word1))

# test the case playing with fire
def measure_similarity_with_idiom(embedding_model, sentence, idiom):
    done = set()
    w = defaultdict()
    sentence = sentence.translate(None, string.punctuation)
    idiom = idiom.translate(None, string.punctuation)
    for word1 in sentence.split():
        if (word1 in embedding_model.vocab):
            for word2 in sentence.split():
                if (word1 != word2):
                    if (word2 in embedding_model.vocab):
                        if (word1, word2) not in done:
                            similarity = embedding_model.similarity(word1, word2)
                            w[word1+word2] = similarity
                            print ('%s - %s ==> %f' % (word1, word2, similarity))
                            done.add((word1, word2))
                            done.add((word2, word1))
    average_with_idiom = sum(w.values())/len(w.values())

    # remove idiom
    for word in idiom.split():
        for word2 in sentence.split():
            ww1 = word+word2
            ww2 = word2+word
            if (ww1 in w.keys()):
                ww = ww1
            elif (ww2 in w.keys()):
                ww = ww2
            else:
                continue
            w.pop(ww)
    average_without_idiom = sum(w.values()) / len(w.values())
    print (sentence)
    print ('idiom ',idiom)
    print ('average with idiom ', average_with_idiom)
    print ('average without idiom ', average_without_idiom)
    print ('after remove idiom ', average_without_idiom - average_with_idiom)
    print ('---------------------------------')

def main():
    embedding_model = build_embedding_model()
    sentences = ["Somehow I always end up spilling the beans all over the floor and looking foolish when the clerk comes to sweep them up"
        ,"Dad had to break the ice on the chicken troughs so that they could get water"
        ,"If you sometimes like to go to the movies to have fun , Wasabi is a good place to start"
        ,"It s  great deal of sizzle and very little steak"
        ,'Grilling outdoors is much more than just another dry-heat cooking method. It s the chance to play with fire, satisfying a primal urge to stir around in coals',
                 'And PLO chairman Yasser Arafat has accused Israel of playing with fire by supporting  in its infancy',
                 'People who buy products from  Company are playing with fire']
    for sen in sentences:
        measure_similarity(embedding_model, sen)
        print (sen)
        print ('---------------------------------')

if __name__ == "__main__":
    embedding_model = build_embedding_model()
    measure_similarity_with_idiom(embedding_model,
                                  "Grilling outdoors is much more than just another dry-heat cooking method. It s the chance to play with fire, satisfying a primal urge to stir around in coals",
                                  'play with fire')
    measure_similarity_with_idiom(embedding_model, 'People who buy products from  Company are playing with fire', 'playing with fire')
    measure_similarity_with_idiom(embedding_model, 'And PLO chairman Yasser Arafat has accused Israel of playing with fire by supporting in its infancy',
                                  'playing with fire')
    measure_similarity_with_idiom(embedding_model, 'Dad had to break the ice on the chicken troughs so that they could get water.', 'break the ice')
    measure_similarity_with_idiom(embedding_model,
                                  'Dad had to break the ice on the chicken troughs so that they could get water.',
                                  'get water')
