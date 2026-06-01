"""
PyJWT を用いたエンコード/デコードの方法
"""

import jwt

# ペイロード(送信したい中身)
payload = {
    "id": 1234,
    "name": "Tanaka Taro"
}

# HS256 の場合は秘密鍵にあたる、秘密の文字列
SECRET_KEY="laisufoewf1as93asidjfawihefawkeh"

# 署名で使用するアルゴリズム
ALGORITHM="HS256"

# エンコードして JWT 形式にする
encoded = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)
print(encoded)

# デコードして payload を取り出す
decoded = jwt.decode(encoded, SECRET_KEY, algorithms=ALGORITHM)
print(decoded)
