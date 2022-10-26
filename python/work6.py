# 冒頭
from ast import pattern
from html.entities import name2codepoint
import numbers
from random import choices
from secrets import choice
from this import d
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("ようこそ、ブラックジャックへ。")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
people=int(input("プレイ人数は？（1～4名・数字のみ入力）"))

if 1<people<5:
  # プレイ人数が2名の場合
  if 1<people<3:
    name1=input("プレイヤー1さん、名前を入力してください:")
    name2=input("プレイヤー2さん、名前を入力してください:")
    print(name1,"さん",name2,"さんですね。それではゲームをはじめるとしましょう。") 
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    # ルール説明
    print("はじめに、ルール説明です。")
    print("ブラックジャックは、ディーラーとプレイヤー、配られたカードの数字の合計が「２１」により近い人が勝ち、というゲームです。")
    print("最初に、ディーラーがプレイヤー側・ディーラー側にそれぞれカードを2枚ずつ配ります。この時、ディーラー側のカードは1枚が伏せられた状態になります。")
    print("プレイヤーの皆様は、合計数が21になるまで何回でもカードを引くことができますが、21をオーバーした瞬間負けになってしまいます。また、合計数が同じだった場合は引き分けとなります。")
    print("プレイヤーの皆様がカードを引くフェーズが終了したら、ディーラーは自分のカードの合計数が「１７」を超えるまで引き続けます。")
    print("ディーラーよりプレイヤーの方が合計数が高い、もしくは、ディーラーが21をオーバーしたら、プレイヤーの皆様の勝ちです")
    print("カードの数字が、「２～１０」までは、数字のままカウントします。")
    print("カードの数字が、「J・Q・K」の場合、すべて「10」としてカウントします。")
    print("カードの数字が、「A」の場合、「1」としてカウントします。")
    print("カードの絵柄はそれぞれ、「♥ハート」「♣クローバー」「♤スペード」「♢ダイヤ」です。")
    print("大まかな流れは以上になります。")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    # カード配る
    import random
    num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    patt=("♥","♣,","♤","♢")
    print("ディーラー:はじめに、私のカードを2枚引き、そのうち１枚をお見せします。")
    deapat=random.sample(patt, k=1)
    dea=random.sample(num, k=1)
    print(deapat)
    print(dea)

# ---プレーヤー1セットここから---
    print("ディーラー：",name1,"さん、カードを2枚お配りします。",name2,"さんは、画面を見ないでください")
    choices=input("　　　　　　準備はよろしいですか？ yes/no:")
    if choices in ['y', 'ye', 'yes']:
      print(random.choices(patt, k=1))
      a=random.sample(num, k=1)
      print(a)
      print("と、")
      print(random.choices(patt, k=1))
      b=random.sample(num, k=1)
      print(b)
      print("です。")
      print("合計は、")
      total1=(sum(a+b))
      print(total1,"点です。")
      choices=input("ディーラー：カードを追加しますか？ yes/no:")
      # カードを追加する
      if choices in ['y', 'ye', 'yes']:
        print(random.choices(patt, k=1))
        c=random.sample(num, k=1) 
        print(c)
        total1=(sum(a+b+c))
        print("合計は、")
        print(total1,"点です。")


        if total1>21:    
          print("ディーラー：21を超えてしまいました。残念ながら負けです。")
          zzz=(input("次へ進みます。yを押してください"))

        elif total1<22:
          choices=input("ディーラー：カードを追加しますか？ yes/no:")
          # カードを追加する
          if choices in ['y', 'ye', 'yes']:
            print(random.choices(patt, k=1))
            d=random.sample(num, k=1) 
            print(d)
            total1=(sum(a+b+c+d))
            print("合計は、")
            print(total1,"点です。")


          if total1>21:    
            print("ディーラー：21を超えてしまいました。残念ながら負けです。")
            zzz=(input("次へ進みます。yを押してください"))

            choices=input("ディーラー：カードを追加しますか？ yes/no:")
            # カードを追加する
            if choices in ['y', 'ye', 'yes']:
              print(random.choices(patt, k=1))
              e=random.sample(num, k=1) 
              print(e)
              total1=(sum(a+b+c+d+e))
              print("合計は、")
              print(total1,"点です。")


              if total1>21:    
                print("ディーラー：21を超えてしまいました。残念ながら負けです。")
                zzz=(input("次へ進みます。yを押してください"))

              elif total1<22:
                choices=input("ディーラー：カードを追加しますか？ yes/no:")
          # カードを追加する
              if choices in ['y', 'ye', 'yes']:
                print(random.choices(patt, k=1))
                c=random.sample(num, k=1) 
                print(c)
                total1=(sum(a+b+c))
                print("合計は、")
                print(total1,"点です。")
                zzz=(input("次へ進みます。yを押してください"))
                # ---ここまで---


          

            

# pythonブチギレver.
    elif choices in ['n', 'no', ]:
      print("python:はよ準備せんかい")
      cho=input("　　　準備ええか？ yes/no:")
      if cho in ['y', 'ye', 'yes']:
        print(random.choices(patt, k=1))
        a=random.sample(num, k=1)
        print(a)
        print("と、")
        print(random.choices(patt, k=1))
        b=random.sample(num, k=1)
        print(b)
        print("だ。")
        print("合計は、")
        total=(sum(a+b))
        print(total,"点だよ。はぁ、、")
        choices=input("python：カード引く？どっちにすんの？ yes/no:")
        # カードを追加する
        if choices in ['y', 'ye', 'yes']:
          print(random.choices(patt, k=1))
          c=random.sample(num, k=1) 
          print(c)
          total=(sum(a+b+c))
          print("合計は、")
          print(total,"点だ。")


          if total>21:    
            print("python：あっ、、21超えたよww残念だったねｗ")
            zzz=(input("次行こう！！！！早くy押して"))

          choices=input("python：カード引く？どっちにすんの？ yes/no:")
            # カードを追加する
          if choices in ['y', 'ye', 'yes']:
            print(random.choices(patt, k=1))
            d=random.sample(num, k=1) 
            print(d)
            total=(sum(a+b+c+d))
            print("合計は、")
            print(total,"点だ。")


            if total>21:    
              print("python：あっ、、21超えたよww残念だったねｗ")
              zzz=(input("次へ進みます。yを押してください"))

            elif total<22:
              choices=input("python：カード引く？どっちにすんの？ yes/no:")
          # カードを追加する
              if choices in ['y', 'ye', 'yes']:
                print(random.choices(patt, k=1))
                e=random.sample(num, k=1) 
                print(c)
                otal=(sum(a+b+c+d+e))
                print("合計は、")
                print(total,"点です。")


              if total>21:    
                print("python：あっ、、21超えたよww残念だったねｗ")
                zzz=(input("次へ進みます。yを押してください"))
      else:
        sys.exit("python:お前となんかやってられっか！！！！強制終了します。")
          






    
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("ディーラー：",name2,"さん、カードを2枚お配りします。",name1,"さんは、画面を見ないでください")
    choices=input("　　　　　　準備はよろしいですか？ yes/no:")
    if choices in ['y', 'ye', 'yes']:
      print(random.choices(patt, k=1))
      a=random.sample(num, k=1)
      print(a)
      print("と、")
      print(random.choices(patt, k=1))
      b=random.sample(num, k=1)
      print(b)
      print("です。")
      print("合計は、")
      total2=(sum(a+b))
      print(total2)
      print("です。")
      choices=input("ディーラー：カードを追加しますか？ yes/no:")
      # カードを追加する
      if choices in ['y', 'ye', 'yes']:
        print(random.choices(patt, k=1))
        c=random.sample(num, k=1) 
        print(c)
        total2=(sum(a+b+c))
        print("合計は、")
        print(total2,"点です。")


        if total2>21:    
          print("ディーラー：21を超えてしまいました。残念ながら負けです。")
          zzz=(input("次へ進みます。yを押してください"))

        else:
          choices=input("ディーラー：カードを追加しますか？ yes/no:")
          # カードを追加する
          if choices in ['y', 'ye', 'yes']:
            print(random.choices(patt, k=1))
            d=random.sample(num, k=1) 
            print(c)
            total2=(sum(a+b+c+d))
            print("合計は、")
            print(total2,"点です。")


          if total2>21:    
            print("ディーラー：21を超えてしまいました。残念ながら負けです。")
            zzz=(input("次へ進みます。yを押してください"))

          
    
      
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print(".")
      print("ディーラー：",name1,"さん、",name2,"さん、勝負の時間です。")
      zzz=(input("準備はよろしいですか？yを押してください"))
      dea2=random.sample(num, k=1)
      deapat2=random.sample(patt, k=1)

      print("ディーラー：私が最初に引いたカードは、",deapat,"の",dea,"です。そして、もう１枚のカードは",deapat2,"の",dea2,"です。")
      totaldea=(sum(dea+dea2))
      print("ディーラー：現在の私の合計は、",totaldea,"です。")
      if totaldea<17:
        dea3=random.sample(num, k=1)
        deapat3=random.sample(patt, k=1)
        print("ディーラー：合計が17点に達していない為新しくカードを引きます。",deapat3,"の",dea3,"です。")
        totaldea2=(sum(dea+dea2+dea3))
        if totaldea2>21:
          print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
          

        if 16<totaldea2<22:
          print("ディーラー：準備は整いました。勝負です。")
          if total1>21 and total2>21:
            print("ディーラー：",name1,"さん、",name2,"さん、21をオーバーしている様ですね。今回のゲームは私の勝ちです。")


        




    

        
        
            
   
            
    


  # プレイ人数が3名の場合
  if 2<people<4:
    name3=input("プレイヤー1さん、名前を入力してください")
    name4=input("プレイヤー2さん、名前を入力してください")
    name5=input("プレイヤー3さん、名前を入力してください")
    print(name3,"さん",name4,"さん",name5,"さんですね。それではゲームをはじめるとしましょう。") 


# プレイ人数が4名の場合
  if 3<people<5:
    name6=input("プレイヤー1さん、名前を入力してください")
    name7=input("プレイヤー2さん、名前を入力してください")
    name8=input("プレイヤー3さん、名前を入力してください")
    name9=input("プレイヤー4さん、名前を入力してください")
    print(name6,"さん",name7,"さん",name8,"さん",name9,"さんですね。それではゲームをはじめるとしましょう。") 









# プレイ人数が1名の場合
else:
  name=input("名前を入力してください")
  print(name,"さんですね。それではゲームをはじめるとしましょう。") 