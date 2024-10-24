# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('勉強場所決定アプリ')

# テキスト入力ボックスを作成し、ユーザーからの入力を受け取る
user_input = st.text_input('あなたの名前を入力してください')

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('挨拶する'):
    if user_input:  # 名前が入力されているかチェック
        st.success(f'🌟 こんにちは、{user_input}さん! 🌟')  # メッセージをハイライト
    else:
        st.error('名前を入力してください。')  # エラーメッセージを表示

# スライダーを作成し、値を選択
number = st.slider('好きな数字（10進数）を選んでください', 0, 100)

# 補足メッセージ
st.caption("十字キー（左右）でも調整できます。")

# 選択した数字を表示
st.write(f'あなたが選んだ数字は「{number}」です。')

#5で割ったときの余りを出す
remainder = number % 5
if remainder ==1: 
   st.text("図書館")
if remainder == 2:
   st.text("同総会館")
if remainder == 3:
   st.text("自宅")
if remainder == 4:
   st.text("ホルトホール")
if remainder == 0:
   st.text("StarbucksCoffee")