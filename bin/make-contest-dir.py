import sys
import os
import subprocess

args = sys.argv
contest_name = args[1]
base_url = "https://atcoder.jp/contests/{0}/tasks/{1}".format(contest_name, contest_name)
base_dir = "/Users/hiratatomonori/kyopro"
postfixes_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

### コンテストディレクトリを作成 ###
contest_dir_name = contest_name
os.makedirs("{0}/{1}".format(base_dir, contest_dir_name))

for postfix in postfixes_list:
    ### 問題ディレクトリを作成 ###
    qdir = "{0}/{1}/{2}_{3}".format(base_dir, contest_dir_name, contest_name, postfix)
    url = "{0}_{1}".format(base_url, postfix)
    os.makedirs(qdir)

    ### 各問題ディレクトリにテストデータを設置 ###
    os.chdir(qdir)
    try:
        print(url)
        res = subprocess.check_call(["oj", "download", url])
    except:
        print("Error")
        continue
    
    ### テキストファイルの生成 ###
    f = open("{0}_{1}.py".format(contest_name, postfix), "w")
    f.write("### {0}_{1}.py ###".format(contest_name, postfix))
    f.close()
print("Don\'t forget to login: \"oj login https://atcoder.jp/\"")
print("[DONE]")
