import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = {
    "hours":[1,2,3,4,5],
    "score":[50,55,65,70,80]
}

df = pd.DataFrame(data)
X = df[['hours']]
y = df['score']
model = LinearRegression()
model.fit(X, y)
hour = int(input("Enter  your study hours: "))

prediction = model.predict(pd.DataFrame([[hour]], columns=['hours']))

print(prediction)