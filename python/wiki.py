import wikipedia

# キーワードを設定
keyword = "犬"
# キーワードで検索
wikipedia.set_lang("ja")
result = wikipedia.search(keyword)
print("検索結果",result)

print("最初の検索結果を表示")
page_data = wikipedia.page(result[0])
print(page_data.content)
cd