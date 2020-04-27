# サポートページ

技術書のサポートページです。

## プロジェクトの始め方

本リポジトリを使用する際には

1. このリポジトリをクローンする（手元へダウンロードする）
1. 必要なライブラリを揃える

という2つのステップを踏む必要があります。

### このリポジトリをクローンする

Git BashやMac OS Xのターミナルを開いて，以下のコマンドを実行してください．
support-pageというフォルダが作成されます．

```bash
$ git clone https://github.com/funatsu-lab/support-page.git
```

### 必要なライブラリを揃える

#### それぞれのライブラリをインストールする場合

```bash
$ conda create -n regz python==3.7 numpy scipy pandas scikit-learn
$ conda install -c rdkit rdkit
$ pip install jupyter
```

#### Anacondaを使ってインストールする場合

Anaconda (Miniconda)の`conda env create`コマンドを使って<br>
（Pythonの）仮想環境を構築します。本フォルダには既に<br>
`environment.yml`という必要なライブラリのリストが<br>
掲載されているテキストファイルがありますので利用してください。

```bash
$ conda env create -n [Python仮想環境名] -f environment.yml
```

## プロジェクトの構成

以下のフォルダ構成は[Cookie Cutter/Data Science](https://github.com/drivendata/cookiecutter-data-science)が<br>
テンプレートとして作成するフォルダ構成を参考に作っています。<br>
他の人も利用可能な状況にフォルダを維持しておくのは<br>
プログラミングの生産性の観点からも重要です。<br>
可能な限り以下のフォルダ構成を維持するようにしてください。<br>
もちろん、必要に応じてフォルダが増減しても構いません。

```
support-page
|-- README.md       # プロジェクト概要を示すテキストファイル
|-- environment.yml # Anacondaにインストールしたライブラリの情報を書き出す
|-- setup.py        # cheminfo ライブラリをコンパイルする場合は作成する
|-- bin             # シェルスクリプトを書いたら保存しておくフォルダ
|   `-- compile_package.sh
|-- cheminfo        # 自作ライブラリを保存するフォルダで、今回は`cheminfo`とした
|   |-- __init__.py # __init__.pyを必ず含む
|   |-- descriptors.py
|   `-- metrics.py
|-- data            # データを保存するフォルダ。データセットが多様ならデータソースごとに
|   |-- catalyst    # サブフォルダを作っておくと良い
|   |-- chembl
|   |-- delaney-solubility
|   `-- zinc
|-- models          # 作った機械学習モデルを保存するフォルダ
|   |-- 9.3_rdkit_pls.joblib
|   |-- morgan_svm.joblib
|   |-- rdfrags_svm.joblib
|   `-- rdkit_svm.joblib
|-- notebooks       # 探索的な解析，可視化をする場合はJupyter Notebookを用いた解析をする
|   |-- 1.2-eda-boston-data.ipynb
|   |-- 1.3-tsne-tanimoto-distance.ipynb
|   |-- 1.4-fragment-visualization.ipynb
|   |-- 4.2-doe_orthogonal.ipynb
|   |-- 4.4-deap_d_optimal_design.ipynb
|   |-- 8.1.2-structure-decomposition.ipynb
|   |-- 8.1.2-structure-generation-brics.ipynb
|   |-- 8.2-bayes-optimization.ipynb
|   |-- 9.2-catalyst-exhaustive.ipynb
|   |-- 9.3-decsriptors.ipynb
|   `-- 9.4-histamine-antagonist-screening.ipynb
|-- references      # 文献を保存しておくフォルダ
|-- results         # 解析結果の図を保存しておくフォルダ。必要に応じてサブフォルダを作る
`-- src             # Jupyter Notebookで実行すべきではない重い処理や
    |               #   何度も実行する処理をスクリプトにまとめて保存するフォルダ
    |-- from_root.py
    |-- from_src.py
    |-- parallel.py
    |-- parallel_wo_with.py
    |-- data
    |   `-- 9.3-brics.py
    |-- features
    |   |-- 5.2-3-fragmentor.py
    |   |-- 5.4-rdkit_desc.py
    |   `-- 5.5-run_mordred.py
    `-- models
        `-- 9.3-screening.py
```

## コンテンツ

0. Pythonの基礎（テキスト本編にはありません） [gist](https://nbviewer.jupyter.org/gist/sshojiro/e437645bb071bcb6c072f9cc6dbb11fa)
1. CoLabでの演習
    - 1.2 Bostonデータ可視化 [gist](https://nbviewer.jupyter.org/gist/sshojiro/d614503df0db630ac8194e381a7e5588)
    - 1.3 tSNEでのタニモト距離基準の可視化 [gist](https://nbviewer.jupyter.org/gist/sshojiro/01579415335916620109f5c45e69826e)
    - 1.4 フラグメント可視化 [gist](https://nbviewer.jupyter.org/gist/sshojiro/946737ed021eae99b08e6b2cd0b4cc12/1-4-fragment-visualization.ipynb)
2. （環境構築，テキスト参照のこと）
3. （マテリアルズインフォマティクス概論，テキスト参照のこと）
4. 実験計画法
    - 4.2 直交計画法 [gist](https://nbviewer.jupyter.org/gist/sshojiro/975bd4c31e32fde35ddae14987510fa5/4-2-doe_orthogonal.ipynb)
    - 4.4 D最適化計画 [gist](https://nbviewer.jupyter.org/gist/sshojiro/1806ea69ce0b190a38a516bc050d36a9)
5. 記述子計算（スクリプト実行）
    - 5.2 フラグメントカウントの実装
    - 5.3 RDKit組み込みのフラグメントカウント
    - 5.4 RDKit記述子
    - 5.5 Mordred
    - 5.6 Pymatgen （`notebooks/9.2-catalyst-exhaustive.ipynb`に記載）
6. （機械学習，テキスト参照のこと）
7. （機械学習モデルの解釈，テキスト参照のこと）
8. 追加検討
    - 8.1.1 自作構造生成
    - 8.1.2 ReCAP，BRICSによる構造生成
    - 8.2 ベイズ最適化（図が白黒対応していない）
9. 解析例
    - 9.2 触媒データを使った解析
    - 9.3 水溶解度データを使った構造生成、スクリーニング
    - 9.4 ChEMBLデータを用いた分類。カーネル法と分類問題
10. （Bashによるデータ加工，テキスト参照のこと）

## 誤字脱字等の報告

本書あるいは本リポジトリに誤りが見つかった場合は<br>
[Issueを立ててください](https://github.com/funatsu-lab/support-page/issues/new/choose)。
