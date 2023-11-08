import tensorflow as tf
import numpy as np
from keras.src.preprocessing.text import Tokenizer
from keras.src.utils import pad_sequences

data = [
    {"text": "这是摘要部分。", "label": 0},
    {"text": "这是正文部分。", "label": 1},
    # 更多数据示例
]

# 准备标签
labels = np.array([item['label'] for item in data])

# 创建分词器
tokenizer = Tokenizer()
tokenizer.fit_on_texts([item['text'] for item in data])

# 将文本转换为数字序列
sequences = tokenizer.texts_to_sequences([item['text'] for item in data])

# 填充序列，使它们具有相同的长度
max_sequence_length = max(len(seq) for seq in sequences)
sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

# 构建模型
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1,
                              output_dim=32, input_length=max_sequence_length),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# 编译模型
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 划分训练集和测试集
split_ratio = 0.8
split_index = int(len(sequences) * split_ratio)

train_sequences, test_sequences = sequences[:split_index], sequences[split_index:]
train_labels, test_labels = labels[:split_index], labels[split_index:]

# 训练模型
model.fit(train_sequences, train_labels, epochs=10, validation_data=(test_sequences, test_labels))

# 评估模型
test_loss, test_accuracy = model.evaluate(test_sequences, test_labels)
print(f"测试损失: {test_loss}, 测试准确率: {test_accuracy}")
