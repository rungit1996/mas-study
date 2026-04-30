# -------------- 直接使用，第一次运行会自动下载 cl100k_base 等词表到本地缓存目录，之后断网也能用。--------------

# import tiktoken
#
# enc1 = tiktoken.get_encoding("o200k_base")
# prompt = "你好，你是？"
#
# enc2 = tiktoken.encoding_for_model("gpt-5")
#
# print("prompt: ", enc1.encode(prompt))
# print("prompt len: ", len(enc1.encode(prompt)))

# -------------- 计算哈希（固定值，直接用） --------------
# import hashlib
#
# url = "https://openaipublic.blob.core.windows.net/encodings/o200k_base.tiktoken"
# print(hashlib.sha1(url.encode()).hexdigest())

# -------------- 离线 --------------
import os

import tiktoken

# 1. 设置缓存目录（自己建个文件夹）
cache_dir = "./resources/tiktoken"
os.makedirs(cache_dir, exist_ok=True)
os.environ["TIKTOKEN_CACHE_DIR"] = cache_dir

# 2. 把改名后的文件放到这个文件夹里

# 3. 离线加载（不会再下载）
enc = tiktoken.get_encoding("o200k_base")

# 测试
print(enc.encode("你好，你是？"))  # 输出token id列表
print(len(enc.encode("你好，你是？")))  # 预期输出 4
