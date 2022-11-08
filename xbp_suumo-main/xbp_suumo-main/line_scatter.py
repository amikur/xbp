import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

"""
名称、カテゴリー、アドレス、アクセス
路線、駅、バス停、
乗換時間、バス、徒歩、車、合計時間（分）
築年数、構造、階数、
家賃、管理費、敷金、礼金（万円）
間取り、面積、URL
"""
########################
factor_1 = "面積"
factor_2 = "家賃"
########################

# 日本語の設定
font_manager.fontManager.addfont("./fonts/ipaexg.ttf")
matplotlib.rc("font", family="IPAexGothic")

# データの読み込み
df = pd.read_csv("./data/yokohama_kawasaki.csv", encoding="utf-8")

# 指定された列における駅ごとの各項目の平均値の取得
df_group = df.groupby(["路線"]).mean()
X = df_group.loc[:, factor_1]
Y = df_group.loc[:, factor_2]
T = df_group.index

# グラフのサイズなどの指定
fig, ax = plt.subplots(figsize=(6.4, 4.8), nrows=1, ncols=1)

# 散布図の表示
ax.scatter(X, Y)

# グラフの調整
ax.set_xlabel(factor_1)
ax.set_ylabel(factor_2)
for x, y, t in zip(X, Y, T):
    ax.annotate(t, xy=(x, y), size=10)
plt.title(f"{factor_1}と{factor_2}")
fig.subplots_adjust(wspace=0.1, top=0.96)
# fig.patch.set_alpha(0)  # 余白を透明にする場合
# ax.patch.set_alpha(0)  # プロット部分を透明にする場合

# グラフの保存
plt.savefig(
    "./graph/{}.png".format(f"{factor_1}と{factor_2}"),
    bbox_inches="tight",
    pad_inches=0.1,
    dpi=200,
)
