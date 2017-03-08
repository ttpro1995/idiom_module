import numpy as np
import theano.tensor as T
import theano


def case1():
    # input a matrix, expect scan to work with each row of matrix
    my_matrix = np.asarray([[0,1,0,0],[0,0,1,0],[0,0,0,1]])

    x = T.imatrix()

    def encoding(x_t):
        x_t = x_t + 1
        return x_t

    m, update = theano.scan(fn=encoding,
                            sequences=x)

    f = theano.function([x], m)

    ##########3
    result = f(my_matrix)
    print (result)

def to_one_hot():
    # input a matrix, expect scan to work with each row of matrix
    my_matrix = np.asarray([[1,2,3],[1,3,2],[1,1,1]])

    x = T.imatrix()

    def encoding(idx):
        z = theano.tensor.zeros((idx.shape[0], 4))
        one_hot = theano.tensor.set_subtensor(z[theano.tensor.arange(idx.shape[0]), idx], 1)
        return one_hot

    m, update = theano.scan(fn=encoding,
                            sequences=x)


    f = theano.function([x], m)

    ##########3
    result = f(my_matrix)
    print (result)

to_one_hot()