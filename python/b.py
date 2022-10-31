from unicodedata import name
name=input("名前を入力してください：")
print(name,"さんですね")
print("ルール説明です。")
print("ブラックジャックとは配られたカードの合計が「21」に近い人が勝ちというゲームです。")
print("ゲーム開始後カードが2枚配られます。ディーラーのカードは一枚伏せられた状態です。")
print("プレイヤーの皆様は合計数が21になるまでカードを引くことができます。しかし、21を超えた時点で負けとなってしまいます。また合計数が同じ場合は引き分けとなります。")
print("ディーラーはカードの合計数が17を越えるまで引き続けます。")
print("ディーラーよりプレイヤーの方が合計数が高い、もしくは、ディーラーが21をオーバーしたら、プレイヤーの皆様の勝ちです。")
print("カードの数字が、「２〜１０」までは、数字のままカウントします。")
print("カードの数字が、「J・Q・K」の場合、すべて「10」としてカウントします。")
print("カードの数字が、「A」の場合、今回は「1」としてカウントします。")
print("hitはカードを引く、stayはパスとなります。")
import random
#数をランダムに配布する
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
def deal():
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 1:
            card = "A"
        hand.append(card)
    return hand
def hit(hand):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 1:
        card = "A"
    hand.append(card)
    return hand
def total(hand):
    score = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            score = score + 10
        elif card == "A":
            if score >= 1:
                score = score + 1
        else:
            score += card
    return score
def play_again():
    again = input("もう１度プレイしますか？ (Y/N): ")
    if again == "y" or again == "Y":
        # game()
        return
    else:
        print("お疲れ様でした。")
        exit()
def result(dealer_hand, player_hand):
    if total(player_hand) > total(dealer_hand):
        print(
            f"\nディーラーの合計は {total(dealer_hand)} あなたの合計は {total(player_hand)} です。\033[32mYOU WIN!\033[0m")
    elif total(dealer_hand) > total(player_hand):
        print(
            f"\nディーラーの合計は {total(dealer_hand)} あなたの合計は {total(player_hand)} です。\033[91mYOU LOSE...\033[0m")
def game():
    dealer_hand = deal()
    player_hand = deal()
    print(f"ディーラーのカードは {dealer_hand[0]} です。")
    print(f"プレイヤーのカードは {player_hand} 合計が {total(player_hand)} です。")
    choice = 0
    while choice != quit:
        choice = input("ヒットしますか？ ステイしますか？ (HIT/STAY): ").lower()
        if choice == "hit":
            hit(player_hand)
            print(
                f"\nあなたに {player_hand[-1]} が配られ、カードは {player_hand} 合計は {total(player_hand)} です。")
            if total(player_hand) > 21:
                print("あなたは 21 を超えてしまいました。\033[91mYOU LOSE...\033[0m")
                choice = quit
        elif choice == "stay":
            print(
                f"\nディーラーの２枚めのカードは {dealer_hand[1]} 合計は {total(dealer_hand)} です。")
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(
                    f"ディーラーに {dealer_hand[-1]} が配られ、カードは {dealer_hand} 合計は {total(dealer_hand)} です。")
                if total(dealer_hand) > 21:
                    print("ディーラーは 21 を超えてしまいました。\033[32mYOU WIN!\033[0m")
                    choice = quit
            if total(dealer_hand) <= 21:
                result(dealer_hand, player_hand)
                choice = quit
game()
