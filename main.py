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

