import argparse

# 最初にパーサーとしてArgumentParserオブジェクトを作成する
psr  = argparse.ArgumentParser(
    prog='プログラムの名前',
    usage='プログラムの使い方',
    description='プログラムの説明'
    )

# add_argumentメソッドを使って、コマンドラインから引数を受け取る処理を作成する
psr.add_argument('-f', '--first', required=True, help='一つ目の引数')
psr.add_argument('-s', '--second', required=True, help='二つ目の引数')
psr.add_argument('-t', '--third', help='三つ目の引数(必須ではない)')

# 受け取った引数を解析する
args = psr.parse_args()

# 解析した引数を表示する
print('引数1:' + args.first)
print('引数2:' + args.second)
print('引数3:' + args.third)