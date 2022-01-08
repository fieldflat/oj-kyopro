import os
import sys
import subprocess

### 引数取得 ###
args = sys.argv
postfix = args[1]

### 有効ディレクトリに存在しているかチェック ###
current_path = os.getcwd()
base_dir="" # fill here!!
if not (base_dir in current_path):
    print("[ERROR] Please check current path")
    sys.exit(1)

contest_name = current_path.split("/")[-1]
qname = contest_name + "_" + postfix
os.chdir(qname)

### test ###
try:
    res = subprocess.run(["oj", "t", "-c", "python {0}.py".format(qname)])
except:
    print("[END] cannot execute command (for test)")

### 全て test OK ならば、そのまま submit ###
if res.returncode == 0:
    try:
        url = "https://atcoder.jp/contests/{0}/tasks/{1}".format(contest_name, qname)
        res = subprocess.run(["oj", "submit", url, "{0}.py".format(qname)])
    except:
        print("[END] cannot execute command (for submission)")
