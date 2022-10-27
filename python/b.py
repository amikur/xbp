import random
import copy
print("こんにちは")
print("これは、1対1で行うゲームです。まず先攻後攻を決めます。先攻から1から5の数字を選んでいき、先にすべて言い終わったほうの勝ちです。")
print("しかし、数字を選ぶ際、必ず相手より大きな数字を選ばなければなりません。自分の数字に相手より大きな数字がない場合パスになります。")
print("パスの場合は０を入力してください")
mochite_com=[1,2,3,4,5]
mochite_pla=[1,2,3,4,5]
te_com=0
te_player=0
for i in range(1,20):
    print(i,"ターン")
    # print("c",mochite_com)
    print("p",mochite_pla)
    if te_com!=5:
        te_player = int(input("数字を入れてください"))
        if 0<te_player <= 4:
            mochite_pla.remove(te_player)
            #プレイヤーの手が4以下だったらコンピュータにその数字以上の手を出してほしい
            #コンピュータの持ち手から出す候補を作成（プレイヤーの出してより大きい）
            dasu_koho = copy.copy(mochite_com)
            #出す候補のなかでプレイヤーの手より小さいものを削除
            for c in range(1, te_player+1):
                try:
                    dasu_koho.remove(c)
                except:
                    pass
            #出す手の候補からランダムにコンピュータの手を選ぶ
            try:
                te_com = random.choice(dasu_koho)
                print("COM", te_com)
                #コンピュータが出した手をコンピュータの持ち手から削除
                mochite_com.remove(te_com)
            except:
                print("COMパス")
                pass
        elif te_player==0:
            print("Playerパス")
            # コンピュータの手
            dasu_koho = copy.copy(mochite_com)
            # 出す手の候補からランダムにコンピュータの手を選ぶ
            te_com = random.choice(dasu_koho)
            print("COM", te_com)
            # コンピュータが出した手をコンピュータの持ち手から削除
            mochite_com.remove(te_com)
        else:
            mochite_pla.remove(te_player)
            #プレイヤーの手が５だったらパスしたい
            print("COMパス")
    else:
        print("Playerパス")
        #コンピュータの手
        dasu_koho = copy.copy(mochite_com)
        # 出す手の候補からランダムにコンピュータの手を選ぶ
        te_com = random.choice(dasu_koho)
        print("COM", te_com)
        # コンピュータが出した手をコンピュータの持ち手から削除
        mochite_com.remove(te_com)
    if len(mochite_pla)==0:
        print("Playerの勝ち")
        exit()
    elif len(mochite_com) == 0:
        print("COMの勝ち")
        exit()
