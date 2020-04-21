from joblib import load as jl_load
import numpy as np
from rdkit.Chem import MolFromSmiles

from cheminfo.descriptors import RDKitDescriptor
from cheminfo.metrics import t2_score, q_value
from multiprocessing import Pool, cpu_count

def processor(argv):
    """予測値とSMILESを文字列で返す関数。multiprocessing.Pool.imap用。"""
    smiles, model = argv
    smi = smiles.strip()
    mol = MolFromSmiles(smi)
    mol.UpdatePropertyCache(strict=True)
    rdcalc = RDKitDescriptor()
    xnew = np.array(rdcalc.transform([mol]))
    # print(xnew,type(xnew))
    ypred = model.predict(xnew)
    t2 = t2_score(xnew, model)
    q = q_value(xnew, model)
    return '%s %.8f %.8f %.8f'%(smi, ypred, t2, q)


def count_lines(filename):
    """ファイルの行数を数える関数"""
    with open(filename, 'r')as f:
        c=0
        for _ in f:
            c+=1
    return c


def main(argv):
    """メイン関数。入力を受け取り、並列処理を実行。"""
    assert len(argv)>2, "SYNTAX: python src/10.3-screening.py MODEL_FILE.joblib SMILES.smi"
    modelfile, smilesfile = argv[1:]
    model = jl_load(modelfile)
    n_counts = count_lines(smilesfile)
    cs = 1000
    model_sampler = (model for _ in range(n_counts))
    outfile = open(smilesfile.replace('.smi', '.out'), 'w')
    with open(smilesfile, 'r') as f:
        with Pool(cpu_count()) as pool:
            "並列処理"
            for ret in pool.imap(processor, zip(f, model_sampler), chunksize=cs):
                outfile.write(ret+'\n')
    outfile.close()# 開いたファイルオブジェクトは必ず閉じる。

if __name__ == '__main__':
    main(sys.argv)
