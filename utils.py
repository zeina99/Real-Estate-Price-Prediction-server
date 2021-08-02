from scipy.sparse import csr_matrix
# converts data to sparse format


def to_sparse(data):
    return csr_matrix(data)


def to_dense(data):
    return csr_matrix.todense(data)
