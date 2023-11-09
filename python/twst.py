import random
import time
# 単語リスト
words = ["みなとみらい", "よこはまコスモワールド", "ランドマークタワー", "横浜赤レンガ倉庫", "山下公園", "中華街", "大さん橋", "カップヌードルミュージアム", "日本丸メモリアルパーク", "ぷかりさん橋", "スカイガーデン", "臨港パーク", "汽車道", "MARK IS みなとみらい", "象の鼻パーク", "港の見える丘公園", "神奈川大学"]
def play_typing_game():
    score = 0
    round_duration = 30 # ゲームの制限時間（秒）
    print("==== タイピングゲーム ====")
    print(f"30秒以内にできるだけ多くの単語を入力してください。正解ごとに5秒の時間が追加されます")
    print("ゲームを開始します")
    print("Now Loading...")
    
    print("Ready Fight..")
    start_time = time.time()
    while time.time() - start_time < round_duration:
        word = random.choice(words)
        print(f"単語: {word}")
        user_input = input("入力してください: ")
        if user_input == word:
            print("Mission clear!")
            score += 1
            round_duration += 5
        else:
            print("Mission failed...")
            score -= 1
    end_time = time.time()
    game_duration = end_time - start_time
    print("==== ゲーム終了 ====")
    print(f"スコア: {score}")
    print(f"制限時間内にタイプできた単語数: {score}")
    print(f"ゲーム時間: {game_duration:.2f}秒")
if __name__ == "__main__":
    play_typing_game()
