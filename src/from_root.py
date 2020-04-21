"""
Pythonパスシステムの理解。
このファイルが存在するフォルダ src/ で
実行すると実行できて、プロジェクトルートへ移動すると実行できない。

```bash
$ pwd
./support-page
$ python src/from_root.py
t2_score
$ cd src
$ python from_root.py
Traceback (most recent call last):
  File "from_root.py", line 16, in <module>
    from cheminfo.metrics import t2_score
ModuleNotFoundError: No module named 'cheminfo'
```
"""
import sys
sys.path.append('./')
from cheminfo.metrics import t2_score

if __name__=='__main__':
    print(t2_score.__name__)
