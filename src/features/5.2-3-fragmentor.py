#!/usr/bin/python
"""
部分構造の出現回数を数え上げるスクリプト
"""
from rdkit.Chem import MolFromSmarts, MolFromSmiles
from rdkit.Chem.Descriptors import descList
from pandas import read_csv

def count_rings(mol):
    match = MolFromSmarts('c1ccccc1')
    ret = mol.GetSubstructMatches(match)
    n_rings = len(ret)
    return n_rings

listFreq = [key for key in dict(descList).keys() if key.startswith('fr_')]
list_functions = [dict(descList)[k] for k in listFreq]
def mol2freqs(mol):
    " 85 部分構造の出現回数 "
    return list(map(lambda f: f(mol), list_functions))

def main(*argv):
    filename = argv[0]
    func = mol2freqs # 85 部分構造の出現回数
    # func = count_rings # ベンゼンの数え上げ
    df = read_csv(filename)
    df['Mol'] = df.smiles.apply(MolFromSmiles)
    X = df.Mol.apply(func)
    return X


if __name__=="__main__":
    """
    スクリプト実行した際に実行される箇所．
    """
    from sys import argv
    count = main(*argv[1:])
    import matplotlib.pyplot as plt
    plt.hist(count)
    plt.savefig('ring_count_hist.jpg')
