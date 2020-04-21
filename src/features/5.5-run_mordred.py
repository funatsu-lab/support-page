#!/usr/bin/python
"""
Mordredを用いて計算するスクリプト
"""
from pandas import read_csv
import numpy as np
from rdkit.Chem import MolFromSmiles
from mordred import Calculator as mord_calc, descriptors
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib as mpl

def main():
    mpl.rcParams['figure.figsize']=[12, 8]
    mpl.rcParams['font.size']=25.
    plt.rcParams['font.family'] = 'MS Gothic'

    df = read_csv('../data/delaney-solubility/delaney-processed.csv')
    df['Mol'] = df.smiles.apply(MolFromSmiles)
    calc2d = mord_calc(descriptors, ignore_3D=False)
    descs2d = df.Mol.apply(calc2d)
    dfX = calc2d.pandas(df.Mol)
    print('data shape', dfX.shape)


    sc = StandardScaler()
    Xsc = sc.fit_transform(dfX)
    is_nonnan = np.sum(np.isnan(Xsc), axis=0)==0
    pca = make_pipeline(StandardScaler(),  PCA())
    T = pca.fit_transform(dfX.iloc[:, np.where(is_nonnan)[0]])
    contrib_=pca.steps[-1][-1].explained_variance_ratio_
    plt.plot(np.cumsum(contrib_)*100, 'o-')
    plt.xlabel('成分数')
    plt.ylabel('累積寄与率 [%]')
    plt.savefig('../results/mordred_contrib_cumsum.jpg')
    plt.show()

    plt.plot(*T[:,:2].T, 'o')
    plt.xlabel('第1主成分 {:.2f}%'.format(100*contrib_[0]))
    plt.ylabel('第2主成分 {:.2f}%'.format(100*contrib_[1]))
    plt.savefig('../results/mordred_score2d.jpg')
    plt.show()

if __name__=='__main__':
    main()
