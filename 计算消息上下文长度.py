import transformers

# 创建分词器
tokenizer = transformers.AutoTokenizer.from_pretrained(
    pretrained_model_name_or_path="./resources/tokenizer",
    trust_remote_code=True
)

prompt = "你好，你是？"
messages = [
    {"role": "user", "content": "帮我计算下123*456"}
]

print("prompt: ", len(tokenizer.encode("你好，你是？")))  # 应输出 4，实际输出 0
print("message: ", len(tokenizer.apply_chat_template(messages)))  # 应输出 9，实际输出 2
