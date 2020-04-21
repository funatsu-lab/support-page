#!/usr/bin/env python
# coding: utf-8

# # BRICS Demo
from rdkit import Chem
from rdkit.Chem import BRICS
from rdkit.Chem import Draw
import pandas as pd
import numpy as np
from time import time
from multiprocessing import Pool


def stopwatch(t):
    """経過時間を測る関数"""
    return (time() - t)/60

def sample_molecule(mol):
    """
    multiprocessing.Pool.imapに渡す関数。
    Molオブジェクトの更新をしたあとでSMILESに変換。
    """
    mol.UpdatePropertyCache(strict=True)
    return Chem.MolToSmiles(mol)


if __name__=='__main__':
    df=pd.read_csv('./data/delaney-solubility/delaney-processed.csv',
                  index_col=0)
    TARGET=['measured log solubility in mols per litre']
    df['mol'] = df['smiles'].apply(Chem.MolFromSmiles)

    fragments = set()
    for ix, mol in df[['mol']].iterrows():
        f = BRICS.BRICSDecompose(mol[0], returnMols=True)
        fragments.update(list(f))
    else:
        print(len(fragments))

    NUM_ITER=100000
    from random import seed
    #--- starts parallel BRICS
    start = time()
    seed(20200315)
    builder = BRICS.BRICSBuild(fragments)
    with open('./results/mol_single.smi', 'w') as f:
        for i in range(NUM_ITER):
            m = next(builder)
            m.UpdatePropertyCache(strict=True)
            smi = Chem.MolToSmiles(m)
            f.write(smi+'\n')
    print('Elapsed time', stopwatch(start), '[mins]')

    #--- starts parallel BRICS
    start2 = time()
    c = 0
    seed(20200315)
    builder = BRICS.BRICSBuild(fragments)
    with Pool(4) as p:
        f = open('./results/mol_quad.smi', 'w')
        for smi in p.imap(func=sample_molecule, iterable=builder, chunksize=100):
            f.write(smi+'\n')
            c+=1
            if c == NUM_ITER:
                print(c)
                break
        f.close()
    print('Elapsed time', stopwatch(start2), '[mins]')
