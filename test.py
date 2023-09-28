import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


table = pd.read_csv('./assets/clientes.csv')
coding = LabelEncoder()

table["profissao"] = coding.fit_transform(table["profissao"])
table["mix_credito"] = coding.fit_transform(table["mix_credito"])
table["comportamento_pagamento"] = coding.fit_transform(table["comportamento_pagamento"])

unused_columns = ["score_credito", "id_cliente"]

x = table.drop(columns=unused_columns)
y = table["score_credito"]

x_training, x_test, y_training, y_test = train_test_split(x, y)

#models IA
model_random_forest = RandomForestClassifier()
model_knn = KNeighborsClassifier()

model_random_forest.fit(x_training, y_training)
model_knn.fit(x_training, y_training)


forecast_model_random_forest = model_random_forest.predict(x_test)
forecast_model_knn = model_knn.predict(x_test.to_numpy())

print(accuracy_score(y_test, forecast_model_random_forest))
print(accuracy_score(y_test, forecast_model_knn))

