import gensim
def build_embedding_model():
    print ('start')
    model = gensim.models.Word2Vec.load_word2vec_format("D:\APCS\_Research\data\GoogleNews-vectors-negative300.bin",
                                                        binary=True)  # C binary format
    return model

def embedding(word, model):
    if word in model.vocab:
        return model[word]
    else:
        return False