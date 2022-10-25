name=input("名前を教えてください")
waist=input("腹囲は？")
age=input("おいくつですか？")

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=85 and age>=40:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")