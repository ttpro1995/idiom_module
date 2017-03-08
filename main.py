from idiom_dict import IdiomDict
import gensim
from LSTM import LSTM
import numpy as np

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

def debug_lstm():
    sentence_vec = np.load('sentvec.npy')
    meaning = [2]
    print (sentence_vec.shape)
    lstm = LSTM(n_classes=3, hidden_dim=300)
    lstm.sgd_step(sentence_vec, meaning,learning_rate=0.01)


def main():
    # load embedding
    embedding_model = build_embedding_model()

    idiom_dict = IdiomDict()
    a = "Let's do half"
    # look up idiom
    meaning = idiom_dict.lookup(a)

    # embedding
    sentence_vec = []
    for word in meaning[0].split():
        vec = embedding(word, embedding_model)  # some word will be ignore because no embedding
        if (not isinstance(vec, bool)): # only add word embedding vector if can get the embedding
            sentence_vec.append(vec)

    sentence_vec = np.asarray(sentence_vec)

    np.save('sentvec.npy', sentence_vec)
    lstm = LSTM(n_classes=3, hidden_dim=300)
    lstm.sgd_step(sentence_vec, [meaning[1]],learning_rate=0.01)



    print (sentence_vec)

if __name__ == "__main__":
    main()

