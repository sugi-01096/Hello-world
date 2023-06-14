import Levenshtein
from gensim.models import KeyedVectors

# 禁止ワードのリスト
banned_words = ["馬鹿", "禁止ワード2", "禁止ワード3"]

# 事前学習済みのワードベクトルモデルの読み込み
word_vectors_path = "path_to_word_vectors.bin"  # ワードベクトルモデルのパス
word_vectors = gensim.models.KeyedVectors.load_word2vec_format(word_vectors_path, binary=True)

# スペルミスや変形を検出する閾値
levenshtein_threshold = 2  # Levenshtein距離の閾値
similarity_threshold = 0.8  # ワードベクトルの類似度の閾値

# 禁止ワードのスペルミスや変形を検出する関数
def detect_prohibited_words(post_content):
    detected_words = []
    for word in post_content.split():
        # スペルミスの検出
        for banned_word in banned_words:
            distance = Levenshtein.distance(banned_word, word)
            if distance <= levenshtein_threshold:
                detected_words.append(word)
                break
        
        # 変形の検出
        if word not in detected_words:
            for banned_word in banned_words:
                if word in word_vectors and banned_word in word_vectors:
                    similarity = word_vectors.similarity(word, banned_word)
                    if similarity >= similarity_threshold:
                        detected_words.append(word)
                        break
    
    return detected_words

# 掲示板アプリのメイン処理
def main():
    # ...

    # 投稿ボタンがクリックされた場合の処理
    if st.button("投稿"):
        # 禁止ワードのスペルミスや変形の検出
        detected_words = detect_prohibited_words(post_content)
        
        if detected_words:
            # 検出された禁止ワードを通知
            st.warning(f"禁止ワードが含まれています！検出されたワード: {', '.join(detected_words)}")
        
        # ...

# ...
import Levenshtein
from gensim.models import KeyedVectors

# 禁止ワードのリスト
banned_words = ["馬鹿", "禁止ワード2", "禁止ワード3"]

# 事前学習済みのワードベクトルモデルの読み込み
word_vectors = KeyedVectors.load_word2vec_format('path_to_word_vectors.bin', binary=True)

# スペルミスや変形を検出する閾値
levenshtein_threshold = 2  # Levenshtein距離の閾値
similarity_threshold = 0.8  # ワードベクトルの類似度の閾値

# 禁止ワードのスペルミスや変形を検出する関数
def detect_prohibited_words(post_content):
    detected_words = []
    for word in post_content.split():
        # スペルミスの検出
        for banned_word in banned_words:
            distance = Levenshtein.distance(banned_word, word)
            if distance <= levenshtein_threshold:
                detected_words.append(word)
                break
        
        # 変形の検出
        if word not in detected_words:
            for banned_word in banned_words:
                if word in word_vectors and banned_word in word_vectors:
                    similarity = word_vectors.similarity(word, banned_word)
                    if similarity >= similarity_threshold:
                        detected_words.append(word)
                        break
    
    return detected_words

# 掲示板アプリのメイン処理
def main():
    # ...

    # 投稿ボタンがクリックされた場合の処理
    if st.button("投稿"):
        # 禁止ワードのスペルミスや変形の検出
        detected_words = detect_prohibited_words(post_content)
        
        if detected_words:
            # 検出された禁止ワードを通知
            st.warning(f"禁止ワードが含まれています！検出されたワード: {', '.join(detected_words)}")
        
        # ...

# ...
mport streamlit as st

# 禁止ワードのリスト
banned_words = ["馬鹿", "禁止ワード2", "禁止ワード3"]

# ユーザーの投稿内容をチェックする関数
def check_post_content(post_content):
    # 禁止ワードの検出
    for banned_word in banned_words:
        if banned_word in post_content:
            # 禁止ワードを＠に置き換える
            post_content = post_content.replace(banned_word, "＠" * len(banned_word))
            return post_content, True # 禁止ワードが検出された場合は置き換えた投稿内容とTrueを返す
    return post_content, False # 禁止ワードが検出されなかった場合は投稿内容とFalseを返す

# 掲示板アプリのメイン処理
def main():
    st.title("掲示板アプリ")
    
    # ユーザーの投稿内容を入力
    post_content = st.text_input("投稿内容")
    
    # 投稿ボタンがクリックされた場合の処理
    if st.button("投稿"):
        # 禁止ワードのチェック
        post_content, banned = check_post_content(post_content)
        if banned:
            # 禁止ワードが検出された場合は警報を出す
            st.warning("禁止ワードが含まれています！")
        
        # 投稿内容を表示
        st.write("投稿内容:", post_content)

# アプリの実行
if __name__ == "__main__":
    main()
