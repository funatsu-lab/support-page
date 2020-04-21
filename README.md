# support-page
技術書のサポートページです

## プロジェクトの始め方

### このリポジトリをクローンする

Git BashやMac OS Xのターミナルを開いて，以下のコマンドを実行してください．
support-pageというフォルダが作成されます．

```bash
$ git clone https://github.com/funatsu-lab/support-page.git
```

### それぞれのライブラリをインストールする場合

```bash
$ conda create -n regz python==3.7 numpy scipy pandas scikit-learn
$ conda install -c rdkit rdkit
$ pip install jupyter
```

### Anacondaを使ってインストールする場合
```bash
$ conda env create -n [Python仮想環境名] -f environment.yml
```

## プロジェクトの構成
