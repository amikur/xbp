def start_game():
    print("あなたは古代の寺院を探検する探検家です。寺院の奥深くには宝物が眠っています。")
    print("各部屋には難解な謎があり、それを解くことで次の部屋に進むことができます。")
    print("では、探検を始めましょう！\n")
    room1()

def room1():
    print("最初の部屋に入りました。壁には次のような文字が刻まれています：")
    print("'3人の探検家がいます。Aは嘘をつかない、Bは真実しか言わない、Cはランダムに嘘をついたり真実を言ったりします。'")
    print("'A: 私は宝物を見つけた'")
    print("'B: Cは嘘をついている'")
    print("'C: 私は嘘をついていない'")
    print("宝物を見つけたのは誰ですか？ (A/B/C)")
    answer = input("答えは？: ")
    if answer.upper() == "B":
        print("正解です！次の部屋に進みます。\n")
        room2()
    else:
        print("間違いです。もう一度考えてください。\n")
        room1()

def room2():
    print("次の部屋には暗号が刻まれた石板があります。")
    print("暗号: 'Uifsf jt b tfdsfu dpef jo uijt tfoufodf.'")
    print("この暗号を解読してください。")
    answer = input("答えは？: ")
    if answer.lower() == "there is a secret code in this sentence":
        print("正解です！次の部屋に進みます。\n")
        room3()
    else:
        print("間違いです。もう一度考えてください。\n")
        room2()

def room3():
    print("最後の部屋にたどり着きました。ここには宝箱がありますが、開けるには最後の謎を解かなければなりません。")
    print("宝箱には次のような問題が刻まれています：")
    print("ある家に5人の人が住んでいます。")
    print("1. 赤い家に住む人はコーヒーを飲んでいます。")
    print("2. 緑の家の左隣にある白い家に住む人は紅茶を飲んでいます。")
    print("3. 犬を飼っている人は黄色い家に住んでいます。")
    print("4. ある家に住む人は牛乳を飲んでいます。")
    print("5. 中央の家に住む人は鳥を飼っています。")
    print("誰が魚を飼っているのですか？ (赤/緑/白/黄色/中央)")
    answer = input("答えは？: ")
    if answer == "中央":
        print("正解です！宝箱が開きました。中には古代の宝物があります。おめでとうございます、探検は成功しました！\n")
        end_game()
    else:
        print("間違いです。もう一度考えてください。\n")
        room3()

def end_game():
    print("ゲームを終了します。ありがとうございました！")

if __name__ == "__main__":
    start_game()
