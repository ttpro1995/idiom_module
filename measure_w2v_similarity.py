# -*- coding: utf-8 -*-
import string
from util import *
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
def playing_with_fire():
    pass

if __name__ == "__main__":
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
