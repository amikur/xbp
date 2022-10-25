""" BlackJackGame

Copyright:
    Fumi (https://fumisite.net/)

License:
    GNU General Public License version 3.
    (https://www.gnu.org/licenses/gpl-3.0.html)

"""
#-*- coding:utf-8 -*-
import sys
import random



"""開発するブラックジャックのルール
1.  初期カードは52枚。
2.  引く際にカードの重複は無いようにする
3.  プレイヤーとディーラーの2人対戦。
4.  プレイヤーは実行者、ディーラーは自動的に実行
5.  実行開始時、プレイヤーとディーラーはそれぞれ、カードを2枚引く。
    引いたカードは画面に表示する。ただし、ディーラーの2枚目のカードは分からないようにする
6.  その後、先にプレイヤーがカードを引く。
    プレイヤーが21を超えていたらバースト、その時点でゲーム終了
7.  プレイヤーは、カードを引くたびに、次のカードを引くか選択できる
8.  プレイヤーが引き終えたら、その後ディーラーは、自分の手札が17以上になるまで引き続ける
9.  プレイヤーとディーラーが引き終えたら勝負。より21に近い方の勝ち
10. JとQとKは10として扱う
11. Aはとりあえず「1」としてだけ扱う。「11」にはしない
12. ダブルダウンなし、スピリットなし、サレンダーなし、その他特殊そうなルールなし
"""



class EmptyError(Exception):
    pass



class Card:
    def __init__(self, name, number):
        def convert(num):
            if num ==  1: return "A"
            if num == 11: return "J"
            if num == 12: return "Q"
            if num == 13: return "K"
            return str(num)
        if not (1 <= number <=13):
            raise ValueError
        self.name   = name
        self.number = number
        self.card_name = "{0:>8}|{1:>2}".format(name, convert(number))



class PlayingCards:
    def __init__(self):
        self._initialize()

    def _initialize(self):
        names = ["diamond", "club", "heart", "spade"]
        self._cards = [Card(names[i % 4], i % 13 + 1) for i in range(52)]

    def new(self):
        self._cards.clear()
        self._initialize()

    def draw(self):
        card_size = len(self._cards)
        if card_size == 0:
            raise EmptyError
        number = random.randint(1, card_size)
        return self._cards.pop(number - 1)



class CardGamePlayer:
    def __init__(self):
        self._hold_cards = []

    def set_card(self, card):
        self._hold_cards.append(card)

    def get_total_value(self):
        def adjust(number):
            return number if number <= 10 else 10
        if len(self._hold_cards) == 0:
            return 0
        return sum([adjust(card.number) for card in self._hold_cards])

    def print_hold_card(self, name=None):
        if not name is None:
            print("-- [{0}] --".format(name))
        for cards in self._hold_cards:
            print("[{0}]".format(cards.card_name))
        print("--------------")
        print("Total: {0}".format(self.get_total_value()))



class BlackJackGame:
    def __init__(self):
        self._pcards = PlayingCards()
        self._player = CardGamePlayer()
        self._dealer = CardGamePlayer()

    def _draw(self, name, pobj, is_print):
        card = self._pcards.draw()
        pobj.set_card(card)
        if is_print:
            print('[{0}]=>[{1}]'.format(name, card.card_name))
        return pobj.get_total_value() <= 21

    def _print_total(self, name, pobj):
        print('[{0}] Total: {1}'.format(name, pobj.get_total_value()))

    def _next_draw(self, name, pobj, is_print_draw_card, is_print_total):
        is_safe = self._draw(name, pobj, is_print_draw_card)
        if is_print_total:
            self._print_total(name, pobj)
        return is_safe

    def first_player_draw(self):
        self._draw("Player", self._player, True)
        self._draw("Player", self._player, True)
        self._print_total("Player", self._player)

    def first_dealer_draw(self):
        self._draw("Dealer", self._dealer, True)
        self._draw("Dealer", self._dealer, False)
        # self._print_total("Dealer", self._dealer)

    def next_player_draw(self):
        return self._next_draw("Player", self._player, True, True)

    def next_dealer_draw(self):
        is_safe = self._next_draw("Dealer", self._dealer, True, True)
        return is_safe and self._dealer.get_total_value() < 17

    def result(self):
        dealer_total = self._dealer.get_total_value()
        player_total = self._player.get_total_value()
        if dealer_total > 21:
            print("Dealer having a total over 21.")
            print("")
            self._dealer.print_hold_card("Dealer")
            print("")
            self._player.print_hold_card("Player")
            print("")
            print("You win. ٩( 'ω' )و")
        elif dealer_total > player_total:
            print("The total value of the dealer is greater than your total.")
            print("Dealer:{0} > Your:{1}".format(dealer_total, player_total))
            print("")
            self._dealer.print_hold_card("Dealer")
            print("")
            self._player.print_hold_card("Player")
            print("")
            print("You lose. (T^T)")
        elif dealer_total < player_total:
            print("Your total is greater than the total value of the dealer.")
            print("Dealer:{0} < Your:{1}".format(dealer_total, player_total))
            print("")
            self._dealer.print_hold_card("Dealer")
            print("")
            self._player.print_hold_card("Player")
            print("")
            print("You win. ٩( 'ω' )و")
        else:
            print("The total of your dealer and your total are the same.")
            print("Dealer:{0} = Your:{1}".format(dealer_total, player_total))
            print("")
            self._dealer.print_hold_card("Dealer")
            print("")
            self._player.print_hold_card("Player")
            print("")
            print("This game is a draw. ( ˘ω˘ )")



def is_continue():
    while True:
        flag = input("continue? [Yes/No]")
        if flag.lower() in ["y", "yes"]:
            return True
        if flag.lower() in ["n", "no"]:
            return False
        if flag.lower() in ["q", "quit"]:
            sys.exit()
        print("Invalid value. Please input yes or no.")



def run_game():
    game = BlackJackGame()
    print("<< Let's play >>")
    print("<< First >>")
    game.first_player_draw()
    game.first_dealer_draw()
    print("")
    while True:
        if not is_continue():
            print("")
            break
        if not game.next_player_draw():
            print("Your having a total over 21.")
            print("")
            print("You lose. (T^T)")
            return
    while game.next_dealer_draw():
        pass
    print("")
    game.result()



def main():
    run_game()



if __name__ == '__main__':
    main()
