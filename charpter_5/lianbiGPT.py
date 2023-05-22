# 开发时间：2023-04-28 10:23
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 读取数据
df = pd.read_csv('bankloan.csv')
known_customers = df.iloc[:700, :]
unknown_customers = df.iloc[700:, :]

# 指定特征和目标变量
features = ['age', 'ed', 'employ', 'address', 'income', 'debtinc', 'creddebt', 'othdebt']
target = 'default'

# 训练模型
model = DecisionTreeClassifier()
model.fit(known_customers[features], known_customers[target])

# 对待预测客户进行研判
predictions = model.predict(unknown_customers[features])


print(predictions)

from sklearn.metrics import accuracy_score

# 计算模型在已知客户数据集上的准确率
train_predictions = model.predict(known_customers[features])
train_accuracy = accuracy_score(train_predictions, known_customers[target])

# 计算模型在待预测客户数据集上的准确率
test_predictions = model.predict(unknown_customers[features])
test_accuracy = accuracy_score(test_predictions, unknown_customers[target])

print('训练集准确率:', train_accuracy)
print('测试集准确率:', test_accuracy)
