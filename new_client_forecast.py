import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


table = pd.read_csv('./assets/clientes.csv')
coding = LabelEncoder()

table["profissao"] = coding.fit_transform(table["profissao"])
table["mix_credito"] = coding.fit_transform(table["mix_credito"])
table["comportamento_pagamento"] = coding.fit_transform(table["comportamento_pagamento"])

unused_columns = ["score_credito", "id_cliente"]

x = table.drop(columns=unused_columns)
y = table["score_credito"]

x_training, x_test, y_training, y_test = train_test_split(x, y)
model_random_forest = RandomForestClassifier()

model_random_forest.fit(x_training, y_training)
forecast_model_random_forest = model_random_forest.predict(x_test)



new_client = pd.read_csv("./assets/novos_clientes.csv")

new_client["profissao"] = coding.fit_transform(new_client["profissao"])
new_client["mix_credito"] = coding.fit_transform(new_client["mix_credito"])
new_client["comportamento_pagamento"] = coding.fit_transform(new_client["comportamento_pagamento"])


forecast = model_random_forest.predict(new_client)

print(forecast)