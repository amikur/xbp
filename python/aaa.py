import random

# カードデッキの生成
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6', '7': 7', '8': 8', '9': 9', '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

deck = [{'suit': suit, 'rank': rank, 'value': values[rank]} for suit in suits for rank in ranks]

# カードをシャッフル
random.shuffle(deck)

# カードを配る関数
def deal_card(deck):
    return deck.pop()

# ハンドの合計を計算する関数
def calculate_hand_value(hand):
    value = sum(card['value'] for card in hand)
    # エースが含まれていて、合計が21を超える場合、エースの値を11から1に変更
    num_aces = sum(1 for card in hand if card['rank'] == 'A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

# 初期設定
player_hand = [deal_card(deck), deal_card(deck)]
dealer_hand = [deal_card(deck), deal_card(deck)]

# プレイヤーのターン
while True:
    print(f"Your hand: {player_hand}, value: {calculate_hand_value(player_hand)}")
    action = input("Hit or Stand? (h/s): ")
    if action == 'h':
        player_hand.append(deal_card(deck))
        if calculate_hand_value(player_hand) > 21:
            print(f"Your hand: {player_hand}, value: {calculate_hand_value(player_hand)}")
            print("Bust! You lose.")
            break
    elif action == 's':
        break

# ディーラーのターン
if calculate_hand_value(player_hand) <= 21:
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    print(f"Dealer's hand: {dealer_hand}, value: {calculate_hand_value(dealer_hand)}")

    # 勝敗判定
    if calculate_hand_value(dealer_hand) > 21 or calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
        print("You win!")
    elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
        print("You lose!")
    else:
        print("Push!")

