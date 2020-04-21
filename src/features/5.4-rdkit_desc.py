#!/usr/bin/python
"""
RDKit記述子(200次元)を計算するスクリプト
"""
from rdkit.Chem import MolFromSmiles
from rdkit.Chem.Descriptors import descList
from pandas import read_csv
from numpy import array as np_array, matrix as np_matrix

list_functions = list(dict(descList).values())
def mol2rdkit_desc(mol):
    " RDKit descriptors "
    return list(map(lambda f: f(mol), list_functions))

def main(*argv):
    filename = argv[0]
    func = mol2rdkit_desc
    df = read_csv(filename)
    df['Mol'] = df.smiles.apply(MolFromSmiles)
    X = df.Mol.apply(func)
    return np_matrix(X.tolist())


if __name__=="__main__":
    from sys import argv
    from sklearn.pipeline import make_pipeline
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    mpl.rcParams['figure.figsize']=[12, 8]
    mpl.rcParams['font.size']=25.
    plt.rcParams['font.family'] = 'MS Gothic'

    X = main(*argv[1:])
    print(X.shape)
    pca = make_pipeline(StandardScaler(), PCA())
    T = pca.fit_transform(X)
    ratio_ = dict(pca.steps)['pca'].explained_variance_ratio_

    plt.plot(T[:,0], T[:,1], 'o')
    plt.xlabel('第1主成分 {:.2f}%'.format(ratio_[0]*100))
    plt.ylabel('第2主成分 {:.2f}%'.format(ratio_[1]*100))
    plt.axis('square')
    plt.savefig('../results/rdkit_pca_freqs.jpg')

    from numpy import cumsum, arange
    plt.figure()
    plt.plot(arange(1,1+len(ratio_)), 100*cumsum( ratio_ ),'o-')
    plt.xlabel('成分数')
    plt.ylabel('累積寄与率 [%]')
    plt.savefig('../results/rdkit_pca_cumsum_contribs.jpg')
