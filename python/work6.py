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
people=int(input("プレイ人数は？（1～3名・数字のみ入力）"))

if 1<people<4:
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
    print("ディーラーよりプレイヤーの方が合計数が高い、もしくは、ディーラーが21をオーバーしたら、プレイヤーの皆様の勝ちです。")
    print("カードの数字が、「２～１０」までは、数字のままカウントします。")
    print("カードの数字が、「J・Q・K」の場合、すべて「10」としてカウントします。")
    print("カードの数字が、「A」の場合、「1」としてカウントします。")
    print("カードの絵柄はそれぞれ、「ハート」「クローバー」「スペード」「ダイヤ」です。")
    print("大まかな流れは以上になります。")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    # カード配る
    import random
    num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    patt=("ハート","クローバー","スペード","ダイヤ")
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
          zzz=(input("次へ進みます。aを押してください"))

        elif choices in ['y', 'ye', 'yes']:
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
                  zzz=(input("次へ進みます。aを押してください"))

            choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
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
                  zzz=(input("次へ進みます。aを押してください"))

                choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
          # カードを追加する
                if choices in ['y', 'ye', 'yes']:
                  print(random.choices(patt, k=1))
                  c=random.sample(num, k=1) 
                  print(c)
                  total1=(sum(a+b+c))
                  print("合計は、")
                  print(total1,"点です。")
                  zzz=(input("次へ進みます。aを押してください"))
                # ---ここまで---

                  if zzz in  ['a'] or choices in ['n','no']:
                    print(".")
                  

            

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
        total1=(sum(a+b))
        print(total1,"点だよ。はぁ、、")
        choices=input("python：カード引く？どっちにすんの？ yes/no:")
        # カードを追加する
        if choices in ['y', 'ye', 'yes']:
          print(random.choices(patt, k=1))
          c=random.sample(num, k=1) 
          print(c)
          total1=(sum(a+b+c))
          print("合計は、")
          print(total1,"点だ。")


          if total1>21:    
            print("python：あっ、、21超えたよww残念だったねｗ")
            zzz=(input("次行こう！！！！早くa押して"))

          choices=input("python：カード引く？どっちにすんの？あ、これコーディングしたやつバカだからオーバーしてもこの文出るときあんだ。そんときは[no]押せよ～ yes/no:")
            # カードを追加する
          if choices in ['y', 'ye', 'yes']:
            print(random.choices(patt, k=1))
            d=random.sample(num, k=1) 
            print(d)
            total1=(sum(a+b+c+d))
            print("合計は、")
            print(total1,"点だ。")


            if total1>21:    
              print("python：あっ、、21超えたよww残念だったねｗ")
              zzz=(input("次へ進みます。aを押してください"))

            elif total1<22:
              choices=input("python：カード引く？どっちにすんの？あ、これコーディングしたやつバカだからオーバーしてもこの文出るときあんだ。そんときは[no]押せよ～ yes/no:")
          # カードを追加する
              if choices in ['y', 'ye', 'yes']:
                print(random.choices(patt, k=1))
                e=random.sample(num, k=1) 
                print(c)
                otal=(sum(a+b+c+d+e))
                print("合計は、")
                print(total1,"点です。")
                zzz=(input("次へ進みます。aを押してください"))


              if total1>21:    
                print("python：あっ、、21超えたよww残念だったねｗ")
                zzz=(input("次へ進みます。aを押してください"))
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
      print(total2,"点です。")
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
          zz=(input("次へ進みます。aを押してください"))

        elif choices in ['y', 'ye', 'yes']:
          choices=input("ディーラー：カードを追加しますか？ yes/no:")
          # カードを追加する
          if choices in ['y', 'ye', 'yes']:
            print(random.choices(patt, k=1))
            d=random.sample(num, k=1) 
            print(d)
            total2=(sum(a+b+c+d))
            print("合計は、")
            print(total2,"点です。")


            if total2>21:    
                  print("ディーラー：21を超えてしまいました。残念ながら負けです。")
                  zz=(input("次へ進みます。aを押してください"))

            choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
            # カードを追加する
            if choices in ['y', 'ye', 'yes']:
                print(random.choices(patt, k=1))
                e=random.sample(num, k=1) 
                print(e)
                total2=(sum(a+b+c+d+e))
                print("合計は、")
                print(total2,"点です。")
                


                if total2>21:    
                  print("ディーラー：21を超えてしまいました。残念ながら負けです。")
                  zz=(input("次へ進みます。aを押してください"))

                choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
          # カードを追加する
                if choices in ['y', 'ye', 'yes']:
                  print(random.choices(patt, k=1))
                  c=random.sample(num, k=1) 
                  print(c)
                  total2=(sum(a+b+c))
                  print("合計は、")
                  print(total2,"点です。")
                  zz=(input("次へ進みます。aを押してください"))
                # ---ここまで---

          
                  if zz in  ['a'] or choices in ['n','no']:
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
      print("ディーラー：",name1,"さん、",name2,"さん、勝負の時間です。")
      zzz=(input("準備はよろしいですか？yを押してください"))
      dea2=random.sample(num, k=1)
      deapat2=random.sample(patt, k=1)

      print("ディーラー：私が最初に引いたカードは、",deapat,"の",dea,"です。そして、もう１枚のカードは",deapat2,"の",dea2,"です。")
      totaldea=(sum(dea+dea2))
      print("ディーラー：現在の私の合計は、",totaldea,"です。")
      # ディーラー17以上
      if 16<totaldea<22:
          print("ディーラー：準備は整いました。勝負です。")
          print("ディーラー：現在の私の合計は、",totaldea,"です。")
          if total1>21 and total2>21:
            # プレイヤー全員オーバー
            print("ディーラー：",name1,"さん、",name2,"さん、21をオーバーしている様ですね。今回のゲームは私の勝ちです。")

          elif 22>totaldea>total1 and 22>totaldea>total2:
            # ディーラープレイヤー全員に勝つ
            print("ディーラー：",name1,"さんの点数は",total1,"点、",name2,"さんの点数は",total2,"点、よって今回のゲームは私の勝ちです。")
          
          elif total1>21 and total2<22 and total2>totaldea:
            # プレイヤー１オーバー且つプレイヤー２ディーラーに勝つ
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name2,"さんの勝ちです。")
          
          elif total1<22 and total2>21 and total1>totaldea:
            # プレイヤー２オーバー且つプレイヤー１ディーラーに勝つ
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name1,"さんの合計は、",total1,"です。おめでとうございます。今回のゲームは",name1,"さんの勝ちです。")

          elif total1>21 and total2<22 and total2<totaldea:
            # プレイヤー１オーバー且つプレイヤー２ディーラーに負け
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さんの合計は、",total2,"です。今回のゲームは私の勝ちです。")
          
          elif total2>21 and total2<22 and total2<totaldea:
            # プレイヤー２オーバー且つプレイヤー１ディーラーに負け
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name1,"さんの合計は、",total1,"です。今回のゲームは私の勝ちです。")

          elif 22>total1==totaldea and 22>total2==totaldea:
            # 引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。今回のゲームは引き分けです。")

          elif total1<totaldea<22 and total2==totaldea:
            # プレーヤー１ディーラーより少ない且つプレイヤー２ディーラー引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name1,"さんは負け、",name2,"さんは引き分けです。")

          elif total2<totaldea<22 and total1==totaldea:
            # プレーヤー２ディーラーより少ない且つプレイヤー１ディーラー引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name2,"さんは負け、",name1,"さんは引き分けです。")

          elif total1<totaldea<22 and 22>total2>totaldea:
            # プレーヤー１ディーラーより少ない且つプレイヤー２勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name1,"さんは負け、おめでとうございます、",name2,"さんは勝ちです。")

          elif total2<totaldea<22 and 22>total1>totaldea:
            # プレーヤー２ディーラーより少ない且つプレイヤー１勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name1,"さんは負け、おめでとうございます、",name2,"さんは勝ちです。")

          elif 22>total2>totaldea and 22>total1>totaldea:
            # プレーヤー１勝ち且つプレイヤー２勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。おめでとうございます。",name1,"さん、",name2,"さんは勝ちです。")
          
      
      
      # ディーラー17に達していないため新しく引く
      if totaldea<17:
        dea3=random.sample(num, k=1)
        deapat3=random.sample(patt, k=1)
        print("ディーラー：合計が17点に達していない為新しくカードを引きます。",deapat3,"の",dea3,"です。")
        totaldea2=(sum(dea+dea2+dea3))
        print("ディーラー：現在の私の合計は、",totaldea2,"です。")
        # ディーラーオーバー
        if totaldea2>21:
          # プレイヤー１オーバー
          if total1>21 and total2<22 and total2>totaldea2:
            print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。",name1,"さんもオーバーしている為、今回のゲームは",name2,"さんの勝ちです。")
          elif total2>21 and total1<22 and total1>totaldea2:
            # プレイヤー２オーバー
            print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。",name2,"さんもオーバーしている為、今回のゲームは",name1,"さんの勝ちです。")
          elif total1>21 and total2>21:
            # ディーラー　プレイヤー１　プレイヤー２オーバー
            print("ディーラー：今回のゲームは全員21を超えてしまった為、引き分けです。")
          else:
            print("ディーラー：おっと、21を超えてしまいましたね。おめでとうございます。今回のゲームは、",name1,"さん、",name2,"さんの勝ちです。")
          

        if 16<totaldea2<22:
          # ディーラー17以上21以下
          print("ディーラー：準備は整いました。勝負です。")
          print("ディーラー：現在の私の合計は、",totaldea2,"です。")
          if total1>21 and total2>21:
            # プレイヤー全員オーバー
            print("ディーラー：",name1,"さん、",name2,"さん、21をオーバーしている様ですね。今回のゲームは私の勝ちです。")
          
          elif 22>totaldea2>total1 and 22>totaldea2>total2:
            # ディーラープレイヤー全員に勝つ
            print("ディーラー：",name1,"さんの点数は",total1,"点、",name2,"さんの点数は",total2,"点、よって今回のゲームは私の勝ちです。")
          
          elif total1>21 and total2<22 and total2>totaldea2:
            # プレイヤー１オーバー且つプレイヤー２ディーラーに勝つ
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name2,"さんの勝ちです。")
          
          elif total1<22 and total2>21 and total1>totaldea2:
            # プレイヤー２オーバー且つプレイヤー１ディーラーに勝つ
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name1,"さんの合計は、",total1,"です。おめでとうございます。今回のゲームは",name1,"さんの勝ちです。")

          elif total1>21 and total2<22 and total2<totaldea2:
            # プレイヤー１オーバー且つプレイヤー２ディーラーに負け
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さんの合計は、",total2,"です。今回のゲームは私の勝ちです。")
          
          elif total2>21 and total2<22 and total2<totaldea2:
            # プレイヤー２オーバー且つプレイヤー１ディーラーに負け
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name1,"さんの合計は、",total1,"です。今回のゲームは私の勝ちです。")

          elif 22>total1==totaldea2 and 22>total2==totaldea2:
            # 引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。今回のゲームは引き分けです。")

          elif total1<totaldea2<22 and total2==totaldea2:
            # プレーヤー１ディーラーより少ない且つプレイヤー２ディーラー引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name1,"さんは負け、",name2,"さんは引き分けです。")

          elif total2<totaldea2<22 and total1==totaldea2:
            # プレーヤー２ディーラーより少ない且つプレイヤー１ディーラー引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name2,"さんは負け、",name1,"さんは引き分けです。")

          elif total1<totaldea2<22 and 22>total2>totaldea2:
            # プレーヤー１ディーラーより少ない且つプレイヤー２勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name1,"さんは負け、おめでとうございます、",name2,"さんは勝ちです。")

          elif total2<totaldea2<22 and 22>total1>totaldea2:
            # プレーヤー２ディーラーより少ない且つプレイヤー１勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name1,"さんは負け、おめでとうございます、",name2,"さんは勝ちです。")

          elif 22>total2>totaldea2 and 22>total1>totaldea2:
            # プレーヤー１勝ち且つプレイヤー２勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。おめでとうございます。",name1,"さん、",name2,"さんは勝ちです。")

          elif total1==totaldea2 and 22>total2>totaldea2:
            # プレーヤー１引き分け且つプレイヤー２勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name1,"さんは引き分け、おめでとうございます、",name2,"さんは勝ちです。")

          elif total2==totaldea2 and 22>total1>totaldea2:
            # プレーヤー１勝ち且つプレイヤー２引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name2,"さんは引き分け、おめでとうございます、",name1,"さんは勝ちです。")


        num2 = ( 8, 9, 10, 10, 10)
        if totaldea2<17:
          dea4=random.sample(num2, k=1)
          deapat4=random.sample(patt, k=1)
          print("ディーラー：合計が17点に達していない為新しくカードを引きます。",deapat4,"の",dea4,"です。")
          totaldea3=(sum(dea+dea2+dea3+dea4))
          print("ディーラー：現在の私の合計は、",totaldea3,"です。")

          if totaldea3>21:
          # プレイヤー１オーバー
            if total1>21 and total2<22 and total2>totaldea2:
              print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。",name1,"さんもオーバーしている為、今回のゲームは",name2,"さんの勝ちです。")
            elif total2>21 and total1<22 and total1>totaldea2:
              # プレイヤー２オーバー
              print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。",name2,"さんもオーバーしている為、今回のゲームは",name1,"さんの勝ちです。")
            elif total1>21 and total2>21:
              # ディーラー　プレイヤー１　プレイヤー２オーバー
              print("ディーラー：今回のゲームは全員21を超えてしまった為、引き分けです。")
            else:
              print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。今回のゲームは、",name1,"さん、",name2,"さんの勝ちです。")

          if 16<totaldea3<22:
            print("ディーラー：準備は整いました。勝負です。")
            print("ディーラー：現在の私の合計は、",totaldea3,"です。")
            if total1>21 and total2>21:
              # プレイヤー全員オーバー
              print("ディーラー：",name1,"さん、",name2,"さん、21をオーバーしている様ですね。今回のゲームは私の勝ちです。")

            elif 22>totaldea3>total1 and 22>totaldea3>total2:
            # ディーラープレイヤー全員に勝つ
              print("ディーラー：",name1,"さんの点数は",total1,"点、",name2,"さんの点数は",total2,"点、よって今回のゲームは私の勝ちです。")
            
            elif total1>21 and total2<22 and total2>totaldea3:
              # プレイヤー１オーバー且つプレイヤー２ディーラーに勝つ
              print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
              print("ディーラー：",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name2,"さんの勝ちです。")
            
            elif total1<22 and total2>21 and total1>totaldea3:
              # プレイヤー２オーバー且つプレイヤー１ディーラーに勝つ
              print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
              print("ディーラー：",name1,"さんの合計は、",total1,"です。おめでとうございます。今回のゲームは",name1,"さんの勝ちです。")

            elif total1>21 and total2<22 and total2<totaldea3:
            # プレイヤー１オーバー且つプレイヤー２ディーラーに負け
              print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
              print("ディーラー：",name2,"さんの合計は、",total2,"です。今回のゲームは私の勝ちです。")
          
            elif total2>21 and total2<22 and total2<totaldea3:
            # プレイヤー２オーバー且つプレイヤー１ディーラーに負け
              print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
              print("ディーラー：",name1,"さんの合計は、",total1,"です。今回のゲームは私の勝ちです。")

            elif 22>total1==totaldea3 and 22>total2==totaldea3:
              # 引き分け
              print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。今回のゲームは引き分けです。")

            elif total1<totaldea3<22 and total2==totaldea3:
              # プレーヤー１ディーラーより少ない且つプレイヤー２ディーラー引き分け
              print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name1,"さんは負け、",name2,"さんは引き分けです。")

            elif total2<totaldea3<22 and total1==totaldea3:
              # プレーヤー２ディーラーより少ない且つプレイヤー１ディーラー引き分け
              print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name2,"さんは負け、",name1,"さんは引き分けです。")

            elif total1>21 and total2==totaldea3:
              # プレイヤー１オーバー且つプレイヤー２引き分け
              print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
              print("ディーラー：",name2,"さんの合計は、",total2,"です。",name1,"さんは負け、",name2,"さんは引き分けです。")

            elif total2>21 and total1==totaldea3:
              # プレイヤー２オーバー且つプレイヤー１引き分け
              print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
              print("ディーラー：",name1,"さんの合計は、",total1,"です。",name2,"さんは負け、",name1,"さんは引き分けです。")

            elif total1<totaldea3<22 and 22>total2>totaldea3:
              # プレーヤー１ディーラーより少ない且つプレイヤー２勝ち
              print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name1,"さんは負け、おめでとうございます、",name2,"さんは勝ちです。")

            elif total2<totaldea3<22 and 22>total1>totaldea3:
              # プレーヤー２ディーラーより少ない且つプレイヤー１勝ち
              print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name1,"さんは負け、おめでとうございます、",name2,"さんは勝ちです。")

            elif 22>total2>totaldea3 and 22>total1>totaldea3:
              # プレーヤー１勝ち且つプレイヤー２勝ち
              print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。おめでとうございます。",name1,"さん、",name2,"さんは勝ちです。")

            elif total1==totaldea3 and 22>total2>totaldea3:
            # プレーヤー１引き分け且つプレイヤー２勝ち
              print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name1,"さんは引き分け、おめでとうございます、",name2,"さんは勝ちです。")

            elif total2==totaldea3 and 22>total1>totaldea3:
              # プレーヤー１勝ち且つプレイヤー２引き分け
              print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"です。",name2,"さんは引き分け、おめでとうございます、",name1,"さんは勝ちです。")
  

  # プレイ人数が3名の場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
  if 2<people<4:
    name1=input("プレイヤー1さん、名前を入力してください")
    name2=input("プレイヤー2さん、名前を入力してください")
    name3=input("プレイヤー3さん、名前を入力してください")
    print(name1,"さん",name2,"さん",name3,"さんですね。申し訳ございません。現在３人では遊べません。")
    cancel
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    # ルール説明
    print("はじめに、ルール説明です。")
    print("ブラックジャックは、ディーラーとプレイヤー、配られたカードの数字の合計が「２１」により近い人が勝ち、というゲームです。")
    print("最初に、ディーラーがプレイヤー側・ディーラー側にそれぞれカードを2枚ずつ配ります。この時、ディーラー側のカードは1枚が伏せられた状態になります。")
    print("プレイヤーの皆様は、合計数が21になるまで何回でもカードを引くことができますが、21をオーバーした瞬間負けになってしまいます。また、合計数が同じだった場合は引き分けとなります。")
    print("プレイヤーの皆様がカードを引くフェーズが終了したら、ディーラーは自分のカードの合計数が「１７」を超えるまで引き続けます。")
    print("ディーラーよりプレイヤーの方が合計数が高い、もしくは、ディーラーが21をオーバーしたら、プレイヤーの皆様の勝ちです。")
    print("カードの数字が、「２～１０」までは、数字のままカウントします。")
    print("カードの数字が、「J・Q・K」の場合、すべて「10」としてカウントします。")
    print("カードの数字が、「A」の場合、「1」としてカウントします。")
    print("カードの絵柄はそれぞれ、「ハート」「クローバー」「スペード」「ダイヤ」です。")
    print("大まかな流れは以上になります。")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    # カード配る
    import random
    num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    patt=("ハート","クローバー","スペード","ダイヤ")
    print("ディーラー:はじめに、私のカードを2枚引き、そのうち１枚をお見せします。")
    deapat=random.sample(patt, k=1)
    dea=random.sample(num, k=1)
    print(deapat)
    print(dea)

# ---プレーヤー1セットここから---
    print("ディーラー：",name1,"さん、カードを2枚お配りします。",name2,"さん、",name3,"さんは、画面を見ないでください")
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
          zzz=(input("次へ進みます。aを押してください"))

        elif choices in ['y', 'ye', 'yes']:
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
                  zzz=(input("次へ進みます。aを押してください"))

            choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
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
                  zzz=(input("次へ進みます。aを押してください"))

                choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
          # カードを追加する
                if choices in ['y', 'ye', 'yes']:
                  print(random.choices(patt, k=1))
                  c=random.sample(num, k=1) 
                  print(c)
                  total1=(sum(a+b+c))
                  print("合計は、")
                  print(total1,"点です。")
                  zzz=(input("次へ進みます。aを押してください"))
                # ---ここまで---

                  if zzz in  ['a'] or choices in ['n','no']:
                    print(".")
                  

            

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
        total1=(sum(a+b))
        print(total1,"点だよ。はぁ、、")
        choices=input("python：カード引く？どっちにすんの？ yes/no:")
        # カードを追加する
        if choices in ['y', 'ye', 'yes']:
          print(random.choices(patt, k=1))
          c=random.sample(num, k=1) 
          print(c)
          total1=(sum(a+b+c))
          print("合計は、")
          print(total1,"点だ。")


          if total1>21:    
            print("python：あっ、、21超えたよww残念だったねｗ")
            zzz=(input("次行こう！！！！早くa押して"))

          choices=input("python：カード引く？どっちにすんの？あ、これコーディングしたやつバカだからオーバーしてもこの文出るときあんだ。そんときは[no]押せよ～ yes/no:")
            # カードを追加する
          if choices in ['y', 'ye', 'yes']:
            print(random.choices(patt, k=1))
            d=random.sample(num, k=1) 
            print(d)
            total1=(sum(a+b+c+d))
            print("合計は、")
            print(total1,"点だ。")


            if total1>21:    
              print("python：あっ、、21超えたよww残念だったねｗ")
              zzz=(input("次へ進みます。aを押してください"))

            elif total1<22:
              choices=input("python：カード引く？どっちにすんの？あ、これコーディングしたやつバカだからオーバーしてもこの文出るときあんだ。そんときは[no]押せよ～ yes/no:")
          # カードを追加する
              if choices in ['y', 'ye', 'yes']:
                print(random.choices(patt, k=1))
                e=random.sample(num, k=1) 
                print(c)
                otal=(sum(a+b+c+d+e))
                print("合計は、")
                print(total1,"点です。")
                zzz=(input("次へ進みます。aを押してください"))


              if total1>21:    
                print("python：あっ、、21超えたよww残念だったねｗ")
                zzz=(input("次へ進みます。aを押してください"))
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
    print("ディーラー：",name2,"さん、カードを2枚お配りします。",name1,"さん",name3,"さんは、画面を見ないでください")
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
      print(total2,"点です。")
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
          zz=(input("次へ進みます。aを押してください"))

        elif choices in ['y', 'ye', 'yes']:
          choices=input("ディーラー：カードを追加しますか？ yes/no:")
          # カードを追加する
          if choices in ['y', 'ye', 'yes']:
            print(random.choices(patt, k=1))
            d=random.sample(num, k=1) 
            print(d)
            total2=(sum(a+b+c+d))
            print("合計は、")
            print(total2,"点です。")


            if total2>21:    
                  print("ディーラー：21を超えてしまいました。残念ながら負けです。")
                  zz=(input("次へ進みます。aを押してください"))

            choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
            # カードを追加する
            if choices in ['y', 'ye', 'yes']:
                print(random.choices(patt, k=1))
                e=random.sample(num, k=1) 
                print(e)
                total2=(sum(a+b+c+d+e))
                print("合計は、")
                print(total2,"点です。")
                


                if total2>21:    
                  print("ディーラー：21を超えてしまいました。残念ながら負けです。")
                  zz=(input("次へ進みます。aを押してください"))

                choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
          # カードを追加する
                if choices in ['y', 'ye', 'yes']:
                  print(random.choices(patt, k=1))
                  c=random.sample(num, k=1) 
                  print(c)
                  total2=(sum(a+b+c))
                  print("合計は、")
                  print(total2,"点です。")
                  zz=(input("次へ進みます。aを押してください"))
                # ---ここまで---

          
                  if zz in  ['a'] or choices in ['n','no']:
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
      print("ディーラー：",name3,"さん、カードを2枚お配りします。",name1,"さん、",name2,"さんは、画面を見ないでください")
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
      total3=(sum(a+b))
      print(total3,"点です。")
      choices=input("ディーラー：カードを追加しますか？ yes/no:")
      # カードを追加する
      if choices in ['y', 'ye', 'yes']:
        print(random.choices(patt, k=1))
        c=random.sample(num, k=1) 
        print(c)
        total3=(sum(a+b+c))
        print("合計は、")
        print(total3,"点です。")


        if total3>21:    
          print("ディーラー：21を超えてしまいました。残念ながら負けです。")
          zzz=(input("次へ進みます。aを押してください"))

        elif choices in ['y', 'ye', 'yes']:
          choices=input("ディーラー：カードを追加しますか？ yes/no:")
          # カードを追加する
          if choices in ['y', 'ye', 'yes']:
            print(random.choices(patt, k=1))
            d=random.sample(num, k=1) 
            print(d)
            total3=(sum(a+b+c+d))
            print("合計は、")
            print(total3,"点です。")


            if total3>21:    
                  print("ディーラー：21を超えてしまいました。残念ながら負けです。")
                  zzz=(input("次へ進みます。aを押してください"))

            choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
            # カードを追加する
            if choices in ['y', 'ye', 'yes']:
                print(random.choices(patt, k=1))
                e=random.sample(num, k=1) 
                print(e)
                total3=(sum(a+b+c+d+e))
                print("合計は、")
                print(total3,"点です。")
                


                if total3>21:    
                  print("ディーラー：21を超えてしまいました。残念ながら負けです。")
                  zzz=(input("次へ進みます。aを押してください"))

                choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
          # カードを追加する
                if choices in ['y', 'ye', 'yes']:
                  print(random.choices(patt, k=1))
                  c=random.sample(num, k=1) 
                  print(c)
                  total3=(sum(a+b+c))
                  print("合計は、")
                  print(total3,"点です。")
                  zzz=(input("次へ進みます。aを押してください"))
                # ---ここまで---

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
    print("ディーラー：",name1,"さん、",name2,"さん、",name3,"さん、勝負の時間です。")
    zzz=(input("準備はよろしいですか？yを押してください"))
    dea2=random.sample(num, k=1)
    deapat2=random.sample(patt, k=1)

    print("ディーラー：私が最初に引いたカードは、",deapat,"の",dea,"です。そして、もう１枚のカードは",deapat2,"の",dea2,"です。")
    totaldea=(sum(dea+dea2))
    print("ディーラー：現在の私の合計は、",totaldea,"です。")
    # ディーラー17以上
    if 16<totaldea<22:
        print("ディーラー：準備は整いました。勝負です。")
        print("ディーラー：現在の私の合計は、",totaldea,"です。")
        if total1>21 and total2>21 and total3>21:
          # プレイヤー全員オーバー
          print("ディーラー：",name1,"さん、",name2,"さん、",name3,"さん、21をオーバーしている様ですね。今回のゲームは私の勝ちです。")

        elif 22>totaldea>total1 and 22>totaldea>total2 and 22>totaldea>total3:
          # ディーラープレイヤー全員に勝つ
          print("ディーラー：",name1,"さんの点数は",total1,"点、",name2,"さんの点数は",total2,"点、",name3,"さんの点数は",total3,"点、よって今回のゲームは私の勝ちです。")
        
        elif total1>21 and total2>21 and total3<22 and total3>totaldea:
          # プレイヤー１オーバー且つプレイヤー2オーバー且つプレイヤー3勝ち
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name3,"さんの勝ちです。")

        elif total1>21 and total3>21 and total2<22 and total2>totaldea:
          # プレイヤー１オーバー且つプレイヤー2勝ち且つプレイヤー3オーバー
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name2,"さんの勝ちです。")

        elif total2>21 and total3>21 and total1<22 and total1>totaldea:
          # プレイヤー１勝ち且つプレイヤー2オーバー且つプレイヤー3オーバー
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name3,"さんの勝ちです。")

        elif total1>21 and total2<22 and total2>totaldea and total3<22 and total3>totaldea:
          # プレイヤー１オーバー且つプレイヤー２勝ち且つプレイヤー３勝ち
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さんの合計は、",total2,"です。",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name2,name3,"さんの勝ちです。")

        elif total2>21 and total1<22 and total1>totaldea and total3<22 and total3>totaldea:
          # プレイヤー１勝ち且つプレイヤー２オーバー且つプレイヤー３勝ち
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name1,name3,"さんの勝ちです。")

        elif total3>21 and total2<22 and total2>totaldea and total1<22 and total1>totaldea:
          # プレイヤー１勝ち且つプレイヤー２勝ち且つプレイヤー３オーバー
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name1,name2,"さんの勝ちです。")

        elif total1>21 and total2<22 and total2<totaldea and total3<22 and total3<totaldea:
          # プレイヤー１オーバー且つプレイヤー２負け且つプレイヤー３負け
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さんの合計は、",total2,"です。",name3,"さんの合計は、",total3,"です。今回のゲームは私の勝ちです。")

        elif total2>21 and total1<22 and total1<totaldea and total3<22 and total3<totaldea:
          # プレイヤー１負け且つプレイヤー２オーバー且つプレイヤー３負け
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。",name3,"さんの合計は、",total3,"です。今回のゲームは私の勝ちです。")

        elif total3>21 and total2<22 and total2<totaldea and total1<22 and total1<totaldea:
          # プレイヤー１負け且つプレイヤー２負け且つプレイヤー３オーバー
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。",name2,"さんの合計は、",total2,"です。今回のゲームは私の勝ちです。")

        elif total1>21 and total2>21 and total3<22 and total3<totaldea:
          # プレイヤー１オーバー且つプレイヤー２オーバー且つプレイヤー３負け
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さんの合計は、",total3,"です。今回のゲームは私の勝ちです。")

        elif total1>21 and total3>21 and total2<22 and total2<totaldea:
          # プレイヤー１オーバー且つプレイヤー２負け且つプレイヤー３オーバー
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さんの合計は、",total2,"です。今回のゲームは私の勝ちです。")

        elif total2>21 and total3>21 and total1<22 and total1<totaldea:
          # プレイヤー１負け且つプレイヤー２オーバー且つプレイヤー３オーバー
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。今回のゲームは私の勝ちです。")
        

        elif 22>total1==totaldea and 22>total2==totaldea and 22>total3==totaldea:
          # 引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。今回のゲームは引き分けです。")

        elif total1<totaldea<22 and total2<totaldea<22 and total3==totaldea:
          # プレーヤー１負け且つプレイヤー２負け且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name2,"さんは負け、",name3,"さんは引き分けです。")

        elif total1<totaldea<22 and total3<totaldea<22 and total2==totaldea:
        # プレーヤー１負け且つプレイヤー２引き分け且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name3,"さんは負け、",name2,"さんは引き分けです。")

        elif total1<totaldea<22 and total2<totaldea<22 and total3==totaldea:
          # プレーヤー１引き分け且つプレイヤー２負け且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,name3,"さんは負け、",name1,"さんは引き分けです。")

        elif total1<totaldea<22 and total2==totaldea and total3==totaldea:
          # プレーヤー１負け且つプレイヤー２引き分け且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,"さんは負け、",name2,name3,"さんは引き分けです。")

        elif total2<totaldea<22 and total1==totaldea and total3==totaldea:
          # プレーヤー１引き分け且つプレイヤー２負け且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,"さんは負け、",name1,name3,"さんは引き分けです。")

        elif total3<totaldea<22 and total2==totaldea and total1==totaldea:
          # プレーヤー１引き分け且つプレイヤー２引き分け且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは負け、",name1,name2,"さんは引き分けです。")

        elif 22>total1>totaldea and 22>total2>totaldea and total3==totaldea:
          # プレーヤー１勝ち且つプレイヤー２勝ち且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name2,"さんは勝ち、",name3,"さんは引き分けです。")

        elif 22>total1>totaldea and 22>total3>totaldea and total2==totaldea:
          # プレーヤー１勝ち且つプレイヤー２引き分け且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name3,"さんは勝ち、",name2,"さんは引き分けです。")

        elif 22>total3>totaldea and 22>total2>totaldea and total1==totaldea:
          # プレーヤー１引き分け且つプレイヤー２勝ち且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,name3,"さんは勝ち、",name1,"さんは引き分けです。")

        elif 22>total3>totaldea and total2==totaldea and total1==totaldea:
          # プレーヤー１引き分け且つプレイヤー２引き分け且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは勝ち、",name1,name2,"さんは引き分けです。")

        elif 22>total2>totaldea and total3==totaldea and total1==totaldea:
          # プレーヤー１引き分け且つプレイヤー２勝ち且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,"さんは勝ち、",name1,name3,"さんは引き分けです。")

        elif 22>total1>totaldea and total2==totaldea and total3==totaldea:
          # プレーヤー１勝ち且つプレイヤー２引き分け且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,"さんは勝ち、",name2,name3,"さんは引き分けです。")

        elif 22>total3>totaldea and total2==totaldea and total1==totaldea:
          # プレーヤー１引き分け且つプレイヤー２引き分け且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは勝ち、",name1,name2,"さんは引き分けです。")

        elif total1<totaldea<22 and 22>total2>totaldea and 22>total3>totaldea:
          # プレーヤー１負け且つプレイヤー２勝ち且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,name3,"さんは勝ち、",name1,"さんは負けです。")

        elif total2<totaldea<22 and 22>total1>totaldea and 22>total3>totaldea:
        # プレーヤー１勝ち且つプレイヤー２負け且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name3,"さんは勝ち、",name2,"さんは負けです。")

        elif total3<totaldea<22 and 22>total1>totaldea and 22>total2>totaldea:
        # プレーヤー１勝ち且つプレイヤー２勝ち且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name2,"さんは勝ち、",name3,"さんは負けです。")

        elif total3<totaldea<22 and total2<totaldea<22 and 22>total1>totaldea:
        # プレーヤー１勝ち且つプレイヤー２負け且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,"さんは勝ち、",name2,name3,"さんは負けです。")

        elif total3<totaldea<22 and total1<totaldea<22 and 22>total2>totaldea:
        # プレーヤー１負け且つプレイヤー２勝ち且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,"さんは勝ち、",name1,name3,"さんは負けです。")

        elif total3<totaldea<22 and total2<totaldea<22 and 22>total1>totaldea:
        # プレーヤー１負け且つプレイヤー２負け且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは勝ち、",name1,name3,"さんは負けです。")

        elif 22>total1>totaldea and 22>total2>totaldea and 22>total3>totaldea:
          # プレーヤー１勝ち且つプレイヤー２勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。おめでとうございます。",name1,"さん",name2,"さん",name3,"さんは勝ちです。")
  

    # ディーラー17に達していないため新しく引く
    if totaldea<17:
      dea3=random.sample(num, k=1)
      deapat3=random.sample(patt, k=1)
      print("ディーラー：合計が17点に達していない為新しくカードを引きます。",deapat3,"の",dea3,"です。")
      totaldea2=(sum(dea+dea2+dea3))
      print("ディーラー：現在の私の合計は、",totaldea2,"です。")
      # ディーラーオーバー
      if totaldea2>21:
        # プレイヤー１オーバー
        if total1>21 and total2>21 and total3>21:
          # プレイヤー全員オーバー
          print("ディーラー：",name1,"さん、",name2,"さん、",name3,"さん、21をオーバーしている様ですね。今回のゲームは引き分けです。")

        elif total1>21 and total2>21 and total3<22 and total3>totaldea2:
          # プレイヤー１オーバー且つプレイヤー2オーバー且つプレイヤー3勝ち
          print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name3,"さんの勝ちです。")

        elif total1>21 and total3>21 and total2<22 and total2>totaldea2:
          # プレイヤー１オーバー且つプレイヤー2勝ち且つプレイヤー3オーバー
          print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name2,"さんの勝ちです。")

        elif total2>21 and total3>21 and total1<22 and total1>totaldea2:
          # プレイヤー１勝ち且つプレイヤー2オーバー且つプレイヤー3オーバー
          print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name3,"さんの勝ちです。")

        elif total1>21 and total2<22 and total2>totaldea2 and total3<22 and total3>totaldea2:
          # プレイヤー１オーバー且つプレイヤー２勝ち且つプレイヤー３勝ち
          print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さんの合計は、",total2,"です。",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name2,name3,"さんの勝ちです。")

        elif total2>21 and total1<22 and total1>totaldea2 and total3<22 and total3>totaldea2:
          # プレイヤー１勝ち且つプレイヤー２オーバー且つプレイヤー３勝ち
          print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name1,name3,"さんの勝ちです。")

        elif total3>21 and total2<22 and total2>totaldea2 and total1<22 and total1>totaldea2:
          # プレイヤー１勝ち且つプレイヤー２勝ち且つプレイヤー３オーバー
          print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name1,name2,"さんの勝ちです。")

        else:
          print("ディーラー：おっと、21を超えてしまいましたね。おめでとうございます。今回のゲームは、",name1,"さん",name2,"さん",name3,"さんの勝ちです。")
        

      if 16<totaldea2<22:
        # ディーラー17以上21以下
        print("ディーラー：準備は整いました。勝負です。")
        print("ディーラー：現在の私の合計は、",totaldea2,"です。")
        if total1>21 and total2>21 and total3>21:
          # プレイヤー全員オーバー
          print("ディーラー：",name1,"さん、",name2,"さん、",name3,"さん、21をオーバーしている様ですね。今回のゲームは私の勝ちです。")

        elif 22>totaldea2>total1 and 22>totaldea2>total2 and 22>totaldea2>total3:
          # ディーラープレイヤー全員に勝つ
          print("ディーラー：",name1,"さんの点数は",total1,"点、",name2,"さんの点数は",total2,"点、",name3,"さんの点数は",total3,"点、よって今回のゲームは私の勝ちです。")
        
        elif total1>21 and total2>21 and total3<22 and total3>totaldea2:
          # プレイヤー１オーバー且つプレイヤー2オーバー且つプレイヤー3勝ち
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name3,"さんの勝ちです。")

        elif total1>21 and total3>21 and total2<22 and total2>totaldea2:
          # プレイヤー１オーバー且つプレイヤー2勝ち且つプレイヤー3オーバー
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name2,"さんの勝ちです。")

        elif total2>21 and total3>21 and total1<22 and total1>totaldea2:
          # プレイヤー１勝ち且つプレイヤー2オーバー且つプレイヤー3オーバー
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name3,"さんの勝ちです。")

        elif total1>21 and total2<22 and total2>totaldea2 and total3<22 and total3>totaldea2:
          # プレイヤー１オーバー且つプレイヤー２勝ち且つプレイヤー３勝ち
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さんの合計は、",total2,"です。",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name2,name3,"さんの勝ちです。")

        elif total2>21 and total1<22 and total1>totaldea2 and total3<22 and total3>totaldea2:
          # プレイヤー１勝ち且つプレイヤー２オーバー且つプレイヤー３勝ち
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name1,name3,"さんの勝ちです。")

        elif total3>21 and total2<22 and total2>totaldea2 and total1<22 and total1>totaldea2:
          # プレイヤー１勝ち且つプレイヤー２勝ち且つプレイヤー３オーバー
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name1,name2,"さんの勝ちです。")

        elif total1>21 and total2<22 and total2<totaldea2 and total3<22 and total3<totaldea2:
          # プレイヤー１オーバー且つプレイヤー２負け且つプレイヤー３負け
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さんの合計は、",total2,"です。",name3,"さんの合計は、",total3,"です。今回のゲームは私の勝ちです。")

        elif total2>21 and total1<22 and total1<totaldea2 and total3<22 and total3<totaldea2:
          # プレイヤー１負け且つプレイヤー２オーバー且つプレイヤー３負け
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。",name3,"さんの合計は、",total3,"です。今回のゲームは私の勝ちです。")

        elif total3>21 and total2<22 and total2<totaldea2 and total1<22 and total1<totaldea2:
          # プレイヤー１負け且つプレイヤー２負け且つプレイヤー３オーバー
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。",name2,"さんの合計は、",total2,"です。今回のゲームは私の勝ちです。")

        elif total1>21 and total2>21 and total3<22 and total3<totaldea2:
          # プレイヤー１オーバー且つプレイヤー２オーバー且つプレイヤー３負け
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さんの合計は、",total3,"です。今回のゲームは私の勝ちです。")

        elif total1>21 and total3>21 and total2<22 and total2<totaldea2:
          # プレイヤー１オーバー且つプレイヤー２負け且つプレイヤー３オーバー
          print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name2,"さんの合計は、",total2,"です。今回のゲームは私の勝ちです。")

        elif total2>21 and total3>21 and total1<22 and total1<totaldea2:
          # プレイヤー１負け且つプレイヤー２オーバー且つプレイヤー３オーバー
          print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
          print("ディーラー：",name1,"さんの合計は、",total1,"です。今回のゲームは私の勝ちです。")
        

        elif 22>total1==totaldea2 and 22>total2==totaldea2 and 22>total3==totaldea2:
          # 引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。今回のゲームは引き分けです。")

        elif total1<totaldea2<22 and total2<totaldea2<22 and total3==totaldea2:
          # プレーヤー１負け且つプレイヤー２負け且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name2,"さんは負け、",name3,"さんは引き分けです。")

        elif total1<totaldea2<22 and total3<totaldea2<22 and total2==totaldea2:
        # プレーヤー１負け且つプレイヤー２引き分け且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name3,"さんは負け、",name2,"さんは引き分けです。")

        elif total1<totaldea2<22 and total2<totaldea2<22 and total3==totaldea2:
          # プレーヤー１引き分け且つプレイヤー２負け且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,name3,"さんは負け、",name1,"さんは引き分けです。")

        elif total1<totaldea2<22 and total2==totaldea2 and total3==totaldea2:
          # プレーヤー１負け且つプレイヤー２引き分け且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,"さんは負け、",name2,name3,"さんは引き分けです。")

        elif total2<totaldea2<22 and total1==totaldea2 and total3==totaldea2:
          # プレーヤー１引き分け且つプレイヤー２負け且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,"さんは負け、",name1,name3,"さんは引き分けです。")

        elif total3<totaldea2<22 and total2==totaldea2 and total1==totaldea2:
          # プレーヤー１引き分け且つプレイヤー２引き分け且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは負け、",name1,name2,"さんは引き分けです。")

        elif 22>total1>totaldea2 and 22>total2>totaldea2 and total3==totaldea2:
          # プレーヤー１勝ち且つプレイヤー２勝ち且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name2,"さんは勝ち、",name3,"さんは引き分けです。")

        elif 22>total1>totaldea2 and 22>total3>totaldea2 and total2==totaldea2:
          # プレーヤー１勝ち且つプレイヤー２引き分け且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name3,"さんは勝ち、",name2,"さんは引き分けです。")

        elif 22>total3>totaldea2 and 22>total2>totaldea2 and total1==totaldea2:
          # プレーヤー１引き分け且つプレイヤー２勝ち且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,name3,"さんは勝ち、",name1,"さんは引き分けです。")

        elif 22>total3>totaldea2 and total2==totaldea2 and total1==totaldea2:
          # プレーヤー１引き分け且つプレイヤー２引き分け且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは勝ち、",name1,name2,"さんは引き分けです。")

        elif 22>total2>totaldea2 and total3==totaldea2 and total1==totaldea2:
          # プレーヤー１引き分け且つプレイヤー２勝ち且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,"さんは勝ち、",name1,name3,"さんは引き分けです。")

        elif 22>total1>totaldea2 and total2==totaldea2 and total3==totaldea2:
          # プレーヤー１勝ち且つプレイヤー２引き分け且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,"さんは勝ち、",name2,name3,"さんは引き分けです。")

        elif 22>total3>totaldea2 and total2==totaldea2 and total1==totaldea2:
          # プレーヤー１引き分け且つプレイヤー２引き分け且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは勝ち、",name1,name2,"さんは引き分けです。")

        elif total1<totaldea2<22 and 22>total2>totaldea2 and 22>total3>totaldea2:
          # プレーヤー１負け且つプレイヤー２勝ち且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,name3,"さんは勝ち、",name1,"さんは負けです。")

        elif total2<totaldea2<22 and 22>total1>totaldea2 and 22>total3>totaldea2:
        # プレーヤー１勝ち且つプレイヤー２負け且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name3,"さんは勝ち、",name2,"さんは負けです。")

        elif total3<totaldea2<22 and 22>total1>totaldea2 and 22>total2>totaldea2:
        # プレーヤー１勝ち且つプレイヤー２勝ち且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name2,"さんは勝ち、",name3,"さんは負けです。")

        elif total3<totaldea2<22 and total2<totaldea2<22 and 22>total1>totaldea2:
        # プレーヤー１勝ち且つプレイヤー２負け且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,"さんは勝ち、",name2,name3,"さんは負けです。")

        elif total3<totaldea2<22 and total1<totaldea2<22 and 22>total2>totaldea2:
        # プレーヤー１負け且つプレイヤー２勝ち且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,"さんは勝ち、",name1,name3,"さんは負けです。")

        elif total3<totaldea2<22 and total2<totaldea2<22 and 22>total1>totaldea2:
        # プレーヤー１負け且つプレイヤー２負け且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは勝ち、",name1,name3,"さんは負けです。")

        elif 22>total1>totaldea2 and 22>total2>totaldea2 and 22>total3>totaldea2:
          # プレーヤー１勝ち且つプレイヤー２勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。おめでとうございます。",name1,"さん",name2,"さん",name3,"さんは勝ちです。")

        elif 22>total1>totaldea2 and total2==totaldea2 and total3<totaldea2<22:
          # プレーヤー１勝ち且つプレイヤー２引き分け且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,"さんは勝ち、",name2,"さんは引き分け、",name3,"さんは負けです。")

        elif 22>total2>totaldea2 and total1==totaldea2 and total3<totaldea2<22:
          # プレーヤー１引き分け且つプレイヤー２勝ち且つプレイヤー３負け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,"さんは勝ち、",name1,"さんは引き分け、",name3,"さんは負けです。")
          
        elif 22>total3>totaldea2 and total1==totaldea2 and total2<totaldea2<22:
          # プレーヤー１引き分け且つプレイヤー２負け且つプレイヤー３勝ち
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは勝ち、",name1,"さんは引き分け、",name2,"さんは負けです。")

        elif 22>total2>totaldea2 and total3==totaldea2 and total1<totaldea2<22:
          # プレーヤー１負け且つプレイヤー２勝ち且つプレイヤー３引き分け
          print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,"さんは勝ち、",name3,"さんは引き分け、",name1,"さんは負けです。")

        
  
      num2 = ( 8, 9, 10, 10, 10)
      if totaldea2<17:
        dea4=random.sample(num2, k=1)
        deapat4=random.sample(patt, k=1)
        print("ディーラー：合計が17点に達していない為新しくカードを引きます。",deapat4,"の",dea4,"です。")
        totaldea3=(sum(dea+dea2+dea3+dea4))
        print("ディーラー：現在の私の合計は、",totaldea3,"です。")

         # ディーラーオーバー
        if totaldea3>21:
          # プレイヤー１オーバー
          if total1>21 and total2>21 and total3>21:
            # プレイヤー全員オーバー
            print("ディーラー：",name1,"さん、",name2,"さん、",name3,"さん、21をオーバーしている様ですね。今回のゲームは引き分けです。")

          elif total1>21 and total2>21 and total3<22 and total3>totaldea3:
            # プレイヤー１オーバー且つプレイヤー2オーバー且つプレイヤー3勝ち
            print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name3,"さんの勝ちです。")

          elif total1>21 and total3>21 and total2<22 and total2>totaldea3:
            # プレイヤー１オーバー且つプレイヤー2勝ち且つプレイヤー3オーバー
            print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name2,"さんの勝ちです。")

          elif total2>21 and total3>21 and total1<22 and total1>totaldea3:
            # プレイヤー１勝ち且つプレイヤー2オーバー且つプレイヤー3オーバー
            print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name3,"さんの勝ちです。")

          elif total1>21 and total2<22 and total2>totaldea3 and total3<22 and total3>totaldea3:
            # プレイヤー１オーバー且つプレイヤー２勝ち且つプレイヤー３勝ち
            print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さんの合計は、",total2,"です。",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name2,name3,"さんの勝ちです。")

          elif total2>21 and total1<22 and total1>totaldea3 and total3<22 and total3>totaldea3:
            # プレイヤー１勝ち且つプレイヤー２オーバー且つプレイヤー３勝ち
            print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name1,"さんの合計は、",total1,"です。",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name1,name3,"さんの勝ちです。")

          elif total3>21 and total2<22 and total2>totaldea3 and total1<22 and total1>totaldea3:
            # プレイヤー１勝ち且つプレイヤー２勝ち且つプレイヤー３オーバー
            print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。")
            print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name1,"さんの合計は、",total1,"です。",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name1,name2,"さんの勝ちです。")

          else:
            print("ディーラー：おっと、21を超えてしまいましたね。おめでとうございます。今回のゲームは、",name1,"さん",name2,"さん",name3,"さんの勝ちです。")
          

        if 16<totaldea3<22:
          # ディーラー17以上21以下
          print("ディーラー：準備は整いました。勝負です。")
          print("ディーラー：現在の私の合計は、",totaldea3,"です。")
          if total1>21 and total2>21 and total3>21:
            # プレイヤー全員オーバー
            print("ディーラー：",name1,"さん、",name2,"さん、",name3,"さん、21をオーバーしている様ですね。今回のゲームは私の勝ちです。")

          elif 22>totaldea3>total1 and 22>totaldea3>total2 and 22>totaldea3>total3:
            # ディーラープレイヤー全員に勝つ
            print("ディーラー：",name1,"さんの点数は",total1,"点、",name2,"さんの点数は",total2,"点、",name3,"さんの点数は",total3,"点、よって今回のゲームは私の勝ちです。")
          
          elif total1>21 and total2>21 and total3<22 and total3>totaldea3:
            # プレイヤー１オーバー且つプレイヤー2オーバー且つプレイヤー3勝ち
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name3,"さんの勝ちです。")

          elif total1>21 and total3>21 and total2<22 and total2>totaldea3:
            # プレイヤー１オーバー且つプレイヤー2勝ち且つプレイヤー3オーバー
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name2,"さんの勝ちです。")

          elif total2>21 and total3>21 and total1<22 and total1>totaldea3:
            # プレイヤー１勝ち且つプレイヤー2オーバー且つプレイヤー3オーバー
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name3,"さんの勝ちです。")

          elif total1>21 and total2<22 and total2>totaldea3 and total3<22 and total3>totaldea3:
            # プレイヤー１オーバー且つプレイヤー２勝ち且つプレイヤー３勝ち
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さんの合計は、",total2,"です。",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name2,name3,"さんの勝ちです。")

          elif total2>21 and total1<22 and total1>totaldea3 and total3<22 and total3>totaldea3:
            # プレイヤー１勝ち且つプレイヤー２オーバー且つプレイヤー３勝ち
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name1,"さんの合計は、",total1,"です。",name3,"さんの合計は、",total3,"です。おめでとうございます。今回のゲームは",name1,name3,"さんの勝ちです。")

          elif total3>21 and total2<22 and total2>totaldea3 and total1<22 and total1>totaldea3:
            # プレイヤー１勝ち且つプレイヤー２勝ち且つプレイヤー３オーバー
            print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name1,"さんの合計は、",total1,"です。",name2,"さんの合計は、",total2,"です。おめでとうございます。今回のゲームは",name1,name2,"さんの勝ちです。")

          elif total1>21 and total2<22 and total2<totaldea3 and total3<22 and total3<totaldea3:
            # プレイヤー１オーバー且つプレイヤー２負け且つプレイヤー３負け
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さんの合計は、",total2,"です。",name3,"さんの合計は、",total3,"です。今回のゲームは私の勝ちです。")

          elif total2>21 and total1<22 and total1<totaldea3 and total3<22 and total3<totaldea3:
            # プレイヤー１負け且つプレイヤー２オーバー且つプレイヤー３負け
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name1,"さんの合計は、",total1,"です。",name3,"さんの合計は、",total3,"です。今回のゲームは私の勝ちです。")

          elif total3>21 and total2<22 and total2<totaldea3 and total1<22 and total1<totaldea3:
            # プレイヤー１負け且つプレイヤー２負け且つプレイヤー３オーバー
            print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name1,"さんの合計は、",total1,"です。",name2,"さんの合計は、",total2,"です。今回のゲームは私の勝ちです。")

          elif total1>21 and total2>21 and total3<22 and total3<totaldea3:
            # プレイヤー１オーバー且つプレイヤー２オーバー且つプレイヤー３負け
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name3,"さんの合計は、",total3,"です。今回のゲームは私の勝ちです。")

          elif total1>21 and total3>21 and total2<22 and total2<totaldea3:
            # プレイヤー１オーバー且つプレイヤー２負け且つプレイヤー３オーバー
            print("ディーラー：",name1,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name2,"さんの合計は、",total2,"です。今回のゲームは私の勝ちです。")

          elif total2>21 and total3>21 and total1<22 and total1<totaldea3:
            # プレイヤー１負け且つプレイヤー２オーバー且つプレイヤー３オーバー
            print("ディーラー：",name2,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name3,"さん、21をオーバーしている様ですね。")
            print("ディーラー：",name1,"さんの合計は、",total1,"です。今回のゲームは私の勝ちです。")
          

          elif 22>total1==totaldea3 and 22>total2==totaldea3 and 22>total3==totaldea3:
            # 引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。今回のゲームは引き分けです。")

          elif total1<totaldea3<22 and total2<totaldea3<22 and total3==totaldea3:
            # プレーヤー１負け且つプレイヤー２負け且つプレイヤー３引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name2,"さんは負け、",name3,"さんは引き分けです。")

          elif total1<totaldea3<22 and total3<totaldea3<22 and total2==totaldea3:
          # プレーヤー１負け且つプレイヤー２引き分け且つプレイヤー３負け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name3,"さんは負け、",name2,"さんは引き分けです。")

          elif total1<totaldea3<22 and total2<totaldea3<22 and total3==totaldea3:
            # プレーヤー１引き分け且つプレイヤー２負け且つプレイヤー３負け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,name3,"さんは負け、",name1,"さんは引き分けです。")

          elif total1<totaldea3<22 and total2==totaldea3 and total3==totaldea3:
            # プレーヤー１負け且つプレイヤー２引き分け且つプレイヤー３引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,"さんは負け、",name2,name3,"さんは引き分けです。")

          elif total2<totaldea3<22 and total1==totaldea3 and total3==totaldea3:
            # プレーヤー１引き分け且つプレイヤー２負け且つプレイヤー３引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,"さんは負け、",name1,name3,"さんは引き分けです。")

          elif total3<totaldea3<22 and total2==totaldea3 and total1==totaldea3:
            # プレーヤー１引き分け且つプレイヤー２引き分け且つプレイヤー３負け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは負け、",name1,name2,"さんは引き分けです。")

          elif 22>total1>totaldea3 and 22>total2>totaldea3 and total3==totaldea3:
            # プレーヤー１勝ち且つプレイヤー２勝ち且つプレイヤー３引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name2,"さんは勝ち、",name3,"さんは引き分けです。")

          elif 22>total1>totaldea3 and 22>total3>totaldea3 and total2==totaldea3:
            # プレーヤー１勝ち且つプレイヤー２引き分け且つプレイヤー３勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name3,"さんは勝ち、",name2,"さんは引き分けです。")

          elif 22>total3>totaldea3 and 22>total2>totaldea3 and total1==totaldea3:
            # プレーヤー１引き分け且つプレイヤー２勝ち且つプレイヤー３勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,name3,"さんは勝ち、",name1,"さんは引き分けです。")

          elif 22>total3>totaldea3 and total2==totaldea3 and total1==totaldea3:
            # プレーヤー１引き分け且つプレイヤー２引き分け且つプレイヤー３勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは勝ち、",name1,name2,"さんは引き分けです。")

          elif 22>total2>totaldea3 and total3==totaldea3 and total1==totaldea3:
            # プレーヤー１引き分け且つプレイヤー２勝ち且つプレイヤー３引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,"さんは勝ち、",name1,name3,"さんは引き分けです。")

          elif 22>total1>totaldea3 and total2==totaldea3 and total3==totaldea3:
            # プレーヤー１勝ち且つプレイヤー２引き分け且つプレイヤー３引き分け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,"さんは勝ち、",name2,name3,"さんは引き分けです。")

          elif 22>total3>totaldea3 and total2==totaldea3 and total1==totaldea3:
            # プレーヤー１引き分け且つプレイヤー２引き分け且つプレイヤー３勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは勝ち、",name1,name2,"さんは引き分けです。")

          elif total1<totaldea3<22 and 22>total2>totaldea3 and 22>total3>totaldea3:
            # プレーヤー１負け且つプレイヤー２勝ち且つプレイヤー３勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,name3,"さんは勝ち、",name1,"さんは負けです。")

          elif total2<totaldea3<22 and 22>total1>totaldea3 and 22>total3>totaldea3:
          # プレーヤー１勝ち且つプレイヤー２負け且つプレイヤー３勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name3,"さんは勝ち、",name2,"さんは負けです。")

          elif total3<totaldea3<22 and 22>total1>totaldea3 and 22>total2>totaldea3:
          # プレーヤー１勝ち且つプレイヤー２勝ち且つプレイヤー３負け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,name2,"さんは勝ち、",name3,"さんは負けです。")

          elif total3<totaldea3<22 and total2<totaldea3<22 and 22>total1>totaldea3:
          # プレーヤー１勝ち且つプレイヤー２負け且つプレイヤー３負け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name1,"さんは勝ち、",name2,name3,"さんは負けです。")

          elif total3<totaldea3<22 and total1<totaldea3<22 and 22>total2>totaldea3:
          # プレーヤー１負け且つプレイヤー２勝ち且つプレイヤー３負け
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name2,"さんは勝ち、",name1,name3,"さんは負けです。")

          elif total3<totaldea3<22 and total2<totaldea3<22 and 22>total1>totaldea3:
          # プレーヤー１負け且つプレイヤー２負け且つプレイヤー３勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。",name3,"さんは勝ち、",name1,name3,"さんは負けです。")

          elif 22>total1>totaldea3 and 22>total2>totaldea3 and 22>total3>totaldea3:
            # プレーヤー１勝ち且つプレイヤー２勝ち
            print("ディーラー：",name1,"さんの合計は",total1,"で、",name2,"さんの合計は",total2,"で、",name3,"さんの合計は",total3,"です。おめでとうございます。",name1,"さん",name2,"さん",name3,"さんは勝ちです。")

        


# プレイ人数が1名の場合ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
else:
  name=input("名前を入力してください")
  print(name,"さんですね。それではゲームをはじめるとしましょう。") 
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
  print("カードの絵柄はそれぞれ、「ハート」「クローバー」「スペード」「ダイヤ」です。")
  print("大まかな流れは以上になります。")
  print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  # カード配る
  import random
  num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
  patt=("ハート","クローバー,","スペード","ダイヤ")
  print("ディーラー:はじめに、私のカードを2枚引き、そのうち１枚をお見せします。")
  deapat=random.sample(patt, k=1)
  dea=random.sample(num, k=1)
  print(deapat)
  print(dea)

# ---プレーヤー1セットここから---
  print("ディーラー：",name,"さん、カードを2枚お配りします。")
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
    choices=input("ディーラー：カードを追加しますか1？ yes/no:")
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
        zzz=(input("次へ進みます。aを押してください"))

      elif choices in ['y', 'ye', 'yes']:
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
                zzz=(input("次へ進みます。aを押してください"))

          choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
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
                zzz=(input("次へ進みます。aを押してください"))

              choices=input("ディーラー：カードを追加しますか？オーバーした場合は[no]を押してください yes/no:")
        # カードを追加する
              if choices in ['y', 'ye', 'yes']:
                print(random.choices(patt, k=1))
                c=random.sample(num, k=1) 
                print(c)
                total1=(sum(a+b+c))
                print("合計は、")
                print(total1,"点です。")
                zzz=(input("次へ進みます。aを押してください"))
                # ここまで
  
    num1 = (6, 7, 8, 9, 10, 10, 10)
    print("ディーラー：",name,"さん、勝負の時間です。")
    zzz=(input("準備はよろしいですか？yを押してください"))
    dea2=random.sample(num1, k=1)
    deapat2=random.sample(patt, k=1)
    print("ディーラー：私が最初に引いたカードは、",deapat,"の",dea,"です。そして、もう１枚のカードは",deapat2,"の",dea2,"です。")
    totaldea=(sum(dea+dea2))
    print("ディーラー：現在の私の合計は、",totaldea,"です。")
          # ディーラー17以上
          # ディーラー17以上
    if 16<totaldea<22:
        print("ディーラー：準備は整いました。勝負です。")
        print("ディーラー：現在の私の合計は、",totaldea,"です。")
        if total1>21:
          # プレイヤーオーバー
          print("ディーラー：",name,"さん、21をオーバーしている様ですね。今回のゲームは私の勝ちです。")

        elif 22>totaldea>total1:
          # ディーラープレイヤー全員に勝つ
          print("ディーラー：",name,"さんの点数は",total1,"点です。今回のゲームは私の勝ちです。")

        elif 22>total1==totaldea:
          # 引き分け
          print("ディーラー：",name,"さんの合計は",total1,"です。今回のゲームは引き分けです。")

        elif 22>total1>totaldea:
          # プレーヤー１勝ち
          print("ディーラー：",name,"さんの合計は",total1,"です。おめでとうございます。",name,"さんは勝ちです。")
        

    num2 = ( 8, 9, 10, 10, 10)
    # ディーラー17に達していないため新しく引く
    if totaldea<17:
      dea3=random.sample(num2, k=1)
      deapat3=random.sample(patt, k=1)
      print("ディーラー：合計が17点に達していない為新しくカードを引きます。",deapat3,"の",dea3,"です。")
      totaldea2=(sum(dea+dea2+dea3))
      print("ディーラー：現在の私の合計は、",totaldea2,"です。")
      # ディーラーオーバー
      if totaldea2>21:
        print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。今回のゲームは",name,"さんの勝ちです。")
      elif total1>21:
          # ディーラー　プレイヤー１オーバー
          print("ディーラー：今回のゲームは全員21を超えてしまった為、引き分けです。")
        

      if 16<totaldea2<22:
        # ディーラー17以上21以下
        if 16<totaldea2<22:
          print("ディーラー：準備は整いました。勝負です。")
          print("ディーラー：現在の私の合計は、",totaldea2,"です。")
          if total1>21:
          # プレイヤーオーバー
            print("ディーラー：",name,"さん、21をオーバーしている様ですね。今回のゲームは私の勝ちです。")

          elif 22>totaldea2>total1:
            # ディーラープレイヤー全員に勝つ
            print("ディーラー：",name,"さんの点数は",total1,"点です。今回のゲームは私の勝ちです。")

          elif 22>total1==totaldea2:
            # 引き分け
            print("ディーラー：",name,"さんの合計は",total1,"です。今回のゲームは引き分けです。")

          elif 22>total1>totaldea2:
            # プレーヤー１勝ち
            print("ディーラー：",name,"さんの合計は",total1,"です。おめでとうございます。",name,"さんは勝ちです。")

      
    # ディーラー新しく引く
      if totaldea2<17:
        dea4=random.sample(num2, k=1)
        deapat4=random.sample(patt, k=1)
        print("ディーラー：合計が17点に達していない為新しくカードを引きます。",deapat4,"の",dea4,"です。")
        totaldea3=(sum(dea+dea2+dea3+dea4))
        print("ディーラー：現在の私の合計は、",totaldea3,"です。")

        if totaldea3>21:
        # ディーラーオーバー
          if totaldea3>21:
            print("ディーラー：おっと、21を超えてしまいましたね。私の負けです。今回のゲームは",name,"さんの勝ちです。")
          elif total1>21:
              # ディーラー　プレイヤー１オーバー
              print("ディーラー：今回のゲームは全員21を超えてしまった為、引き分けです。")
            

        if 16<totaldea3<22:
          # ディーラー17以上21以下
          if 16<totaldea3<22:
            print("ディーラー：準備は整いました。勝負です。")
            print("ディーラー：現在の私の合計は、",totaldea3,"です。")
            if total1>21:
            # プレイヤーオーバー
              print("ディーラー：",name,"さん、21をオーバーしている様ですね。今回のゲームは私の勝ちです。")

            elif 22>totaldea3>total1:
              # ディーラープレイヤー全員に勝つ
              print("ディーラー：",name,"さんの点数は",total1,"点です。今回のゲームは私の勝ちです。")

            elif 22>total1==totaldea3:
              # 引き分け
              print("ディーラー：",name,"さんの合計は",total1,"です。今回のゲームは引き分けです。")

            elif 22>total1>totaldea3:
              # プレーヤー１勝ち
              print("ディーラー：",name,"さんの合計は",total1,"です。おめでとうございます。",name,"さんは勝ちです。")