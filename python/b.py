import random
from re import I
from tkinter import Y
counter=0 #最初の数字は0
print("99を超えないように限界まで挑戦してください。")
print("現在の数字は0です。")
while counter<=99: #上限の99を超えるまで同じ流れが繰り返される
    a = random.randint(1,30) #ランダムで足される数字の幅が1~30
    question=input("まだ足しますか。")
    
    if question=="yes":
        counter=counter+a #ランダムに数字が足される
        print("現在の合計は",counter,"です。") #合計が表示される
    
    elif counter==99: #合計が99ぴったりだと以下の文が表示され、繰り返しから抜ける
        print("おめでとうございます。99ぴったりです。")
        break
    
    elif question=="no": #noと入力されるとハイスコアが表示され、繰り返しから抜ける
        print("ハイスコアは",counter,"です。")
        break
    
else: #合計が99を超えると以下の文が表示される
    print("99を超えました。失敗です。")