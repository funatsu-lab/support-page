"""
Pythonパスシステムの理解。
このファイルが存在するフォルダ src/ で
実行すると実行できて、プロジェクトルートへ移動すると実行できない。

```bash
$ pwd
./support-page/src
$ python from_src.py
t2_score
$ cd ../
$ python src/from_src.py
Traceback (most recent call last):
  File "src/from_src.py", line 13, in <module>
    from cheminfo.metrics import t2_score
ModuleNotFoundError: No module named 'cheminfo'
```
"""
import sys
sys.path.append('../')
from cheminfo.metrics import t2_score

if __name__=='__main__':
    print(t2_score.__name__)
