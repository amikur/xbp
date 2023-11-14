import random

# グローバル変数
suits = ['♠️', '♡', '♢', '♣️']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("ベットするチップの枚数を入力してください: "))
        except ValueError:
            print("無効な値です。もう一度入力してください。")
        else:
            if chips.bet > chips.total:
                print("チップが不足しています。もう一度入力してください。")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal_card())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        choice = input("ヒットするかスタンドするか選択してください (h/s): ")
        if choice.lower() == 'h':
            hit(deck, hand)
        elif choice.lower() == 's':
            print("プレイヤーがスタンドしました。ディーラーの番です。")
            playing = False
        else:
            print("無効な値です。もう一度入力してください。")
            continue
        break


def show_some(player, dealer):
    print("\nディーラーのカード:")
    print("  ??")
    print(f"  {dealer.cards[1]}")
    print("\nプレイヤーのカード:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nディーラーのカード:", *dealer.cards, sep='\n ')
    print("ディーラーの合計:", dealer.value)
    print("\nプレイヤーのカード:", *player.cards, sep='\n ')
    print("プレイヤーの合計:", player.value)


def player_busts(player, dealer, chips):
    print("プレイヤーがバストしました！")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("プレイヤーが勝ちました！")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("ディーラーがバストしました！")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("ディーラーが勝ちました！")
    chips.lose_bet()


def push(player, dealer):
    print("引き分けです！")


# ゲームの実行
while True:
    print("ブラックジャックへようこそ！")

    # デッキの作成とシャッフル
    deck = Deck()
    deck.shuffle()

    # プレイヤーとディーラーのハンドの作成
    player_hand = Hand()
    dealer_hand = Hand()

    # プレイヤーとディーラーに2枚ずつカードを配る
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    # プレイヤーのチップの作成
    player_chips = Chips()

    # ベットを受け付ける
    take_bet(player_chips)

    # カードを表示
    show_some(player_hand, dealer_hand)

    playing = True
    while playing:
        # プレイヤーの行動を選択
        hit_or_stand(deck, player_hand)

        # カードを表示
        show_some(player_hand, dealer_hand)

        # プレイヤーがバストした場合
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # プレイヤーがバストしなかった場合、ディーラーの手札を公開する
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # カードを表示
        show_all(player_hand, dealer_hand)

        # ディーラーがバストした場合
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        # プレイヤーが勝つ場合
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        # ディーラーが勝つ場合
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        # 引き分けの場合
        else:
            push(player_hand, dealer_hand)

    # プレイヤーのチップ残高を表示
    print(f"\nプレイヤーのチップ残高: {player_chips.total}")

    # ゲームを続けるか確認
    play_again = input("\nもう一度プレイしますか？ (y/n): ")
    if play_again.lower() == 'n':
        break
