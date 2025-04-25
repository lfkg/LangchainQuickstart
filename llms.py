 from langchain_community.llms import Ollama
​# 初始化Ollama类的实例，选择模型"qwen2.5:7b"。
# 选择模型时，考虑模型的大小和性能平衡。
# model = Ollama(model="qwen2.5:1.5b")
model = Ollama(model="qwen2.5:7b")​
# 使用Ollama模型实例生成一个鬼故事。
# 输入是一个简单的中文请求，要求模型输出一个鬼故事。
result = model.invoke("请给我讲个鬼故事")
print(result)
