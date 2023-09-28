import pandas as pd
from sklearn.preprocessing import LabelEncoder


table = pd.read_csv('./assets/clientes.csv')
coding = LabelEncoder()

table["profissao"] = coding.fit_transform(table["profissao"])
table["mix_credito"] = coding.fit_transform(table["mix_credito"])
table["comportamento_pagamento"] = coding.fit_transform(table["comportamento_pagamento"])


print(table.info())
