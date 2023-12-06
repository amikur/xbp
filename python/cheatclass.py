import pyautogui
import pytesseract
from PIL import Image
import pyperclip

# pytesseractのパスを設定（あなたの環境に合わせて変更してください）
pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'

# スクリーンショットを取得する範囲を指定
x, y, width, height = 100, 100, 300, 200  # 例として、画面の(x, y)位置から横幅300px、縦幅200pxの範囲

# スクリーンショットを取得
screenshot = pyautogui.screenshot(region=(x, y, width, height))

# OCRを使用して画像からテキストを抽出
text = pytesseract.image_to_string(screenshot)

# 抽出したテキストが一定の文字数に達したら、クリップボードにコピー
min_length = 100  # 最低限必要な文字数
if len(text) >= min_length:
    pyperclip.copy(text)

# ここで必要に応じてテキストをペーストするコードを書く
# 例: pyautogui.typewrite(pyperclip.paste())
