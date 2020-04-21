import numpy as np
from scipy.sparse import lil_matrix
from sklearn.base import TransformerMixin, BaseEstimator
from rdkit.Chem import Descriptors, RDKFingerprint
from rdkit.Chem.AllChem import GetHashedMorganFingerprint, GetMorganFingerprintAsBitVect
__all__ = ['RDKitDescriptor', 'HashedMorgan', 'BinaryHashedMorgan', 'RDKitFingerprint']


class RDKitDescriptor(TransformerMixin, BaseEstimator):
    """
    RDKit記述子を計算するクラス
    """
    def __init__(self):
        pass
    def fit(self, x, y=None):
        return self
    def transform(self, data):
        """SMILESの配列`data`をRDKit記述子にする"""
        return np.matrix(list(map(lambda m:
                                  list(map(
                                      lambda f:f(m), dict(Descriptors.descList).values()
                                  ))
                                 , data)))


class HashedMorgan(TransformerMixin, BaseEstimator):
    """
    Morganフィンガープリント（頻度）を取り出すクラス
    """
    def __init__(self, n_bits=512, radius=3):
        self.n_bits = n_bits
        self.radius = radius
    def fit(self, x, y=None):
        return self
    def transform(self, data):
        """SMILESの配列`data`をHashed Morganフィンガープリントにする"""
        n_samples = len(data)
        D = lil_matrix((n_samples, self.n_bits))
        for ix, mol in enumerate(data):
            morgan = GetHashedMorganFingerprint(mol=mol,
                                             radius=int(self.radius),
                                             nBits=int(self.n_bits)).GetNonzeroElements()
            for key, val in morgan.items():
                D[ix, key]=val
        return D.toarray()


class BinaryHashedMorgan(TransformerMixin, BaseEstimator):
    """
    Morganフィンガープリント（有無）を取り出すクラス
    """
    def __init__(self, n_bits=512, radius=3):
        self.n_bits = n_bits
        self.radius = radius
    def fit(self, x, y=None):
        return self
    def transform(self, data):
        """SMILESの配列`data`をHashed Morganフィンガープリントにする"""
        n_samples = len(data)
        D = lil_matrix((n_samples, self.n_bits))
        for ix, mol in enumerate(data):
            D[ix, :] = GetMorganFingerprintAsBitVect(mol=mol,
                                             radius=int(self.radius),
                                             nBits=int(self.n_bits))
        return D.toarray()


class RDKitFingerprint(TransformerMixin, BaseEstimator):
    """
    RDKitフィンガープリント（有無）を取り出すクラス
    doc: http://rdkit.org/docs/source/rdkit.Chem.Fingerprints.FingerprintMols.html
    """
    def __init__(self, n_bits=256, fraglen=7):
        self.n_bits = n_bits
        self.fraglen = fraglen
    def fit(self, x, y=None):
        return self
    def transform(self, data):
        """SMILESの配列`data`をHashed Morganフィンガープリントにする"""
        n_samples = len(data)
        D = lil_matrix((n_samples, self.n_bits))
        for ix, mol in enumerate(data):
            D[ix, :] = RDKFingerprint(mol=mol, # radius=int(self.radius),
                                      fpSize=int(self.n_bits),
                                      minPath=1, maxPath=int(self.fraglen))
        return D.toarray()
