# 自作関数pyファイルを呼び出し
import Calculation

# Calculation.pyのtasu関数とhiku関数を実行
tasu = Calculation.tasu(3, 1)
hiku = Calculation.hiku(3, 1)

print('足し算の結果は{}です。'.format(tasu))
print('引き算の結果は{}です。'.format(hiku))
