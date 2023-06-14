import streamlit as st

# 禁止ワードのリスト
banned_words = ["禁止ワード1", "禁止ワード2", "禁止ワード3"]

# ユーザーの投稿内容をチェックする関数
def check_post_content(post_content):
    # 禁止ワードの検出
    for banned_word in banned_words:
        if banned_word in post_content:
            return True # 禁止ワードが検出された場合はTrueを返す
    return False # 禁止ワードが検出されなかった場合はFalseを返す

# 掲示板アプリのメイン処理
def main():
    st.title("掲示板アプリ")
    
    # ユーザーの投稿内容を入力
    post_content = st.text_input("投稿内容")
    
    # 投稿ボタンがクリックされた場合の処理
    if st.button("投稿"):
        # 禁止ワードのチェック
        if check_post_content(post_content):
            # 禁止ワードが検出された場合は警報を出す
            st.warning("禁止ワードが含まれています！")
        
        # 投稿内容を表示
        st.write("投稿内容:", post_content)

# アプリの実行
if __name__ == "__main__":
    main()
