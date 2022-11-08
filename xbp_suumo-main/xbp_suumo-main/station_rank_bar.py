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
targets = ["京急本線", "京急逗子線"]
factor_1 = "駅"
factor_2 = "家賃"
########################

# 日本語の設定
font_manager.fontManager.addfont("./fonts/ipaexg.ttf")
matplotlib.rc("font", family="IPAexGothic")

# データの読み込み
df = pd.read_csv("./data/yokohama_kawasaki.csv", encoding="utf-8")

# ある路線の指定された列における各項目の平均値の取得
df = df[df["路線"].isin(targets)]
df_group = df.groupby([factor_1]).mean().sort_values(factor_2, ascending=False)

# グラフのサイズなどの指定
fig, ax = plt.subplots(figsize=(12, 3), nrows=1, ncols=1)

# 棒グラフの表示
ax.bar(df_group.index, df_group[factor_2])

# グラフの調整
xlabels = plt.xticks(rotation=-90)
title = plt.title("と".join(targets) + f"の{factor_1}別の平均{factor_2}")
fig.subplots_adjust(wspace=0.1, top=0.96)
# fig.patch.set_alpha(0)  # 余白を透明にする場合
# ax.patch.set_alpha(0)  # プロット部分を透明にする場合

# グラフの保存
plt.savefig(
    "./graph/{}.png".format("と".join(targets) + f"の{factor_1}別の平均{factor_2}"),
    bbox_inches="tight",
    pad_inches=0.1,
    dpi=200,
)
