from fastapi import FastAPI
import joblib
import uvicorn

import pickle
from models import Website

app = FastAPI()
# pkl
phish_model = open('phishing.pkl', 'rb')
phish_model_ls = joblib.load(phish_model)


@app.get("/{name}")
def hello(name):
    return {"Hello {} and Welcome to this API".format(name)}


@app.get("/")
def greet():
    return {"Hello World"}


# ML Aspect
@app.post('/predict')
async def predict(reg: Website):
    feat = [reg.url]
    feature = feat

    y_Predict = phish_model_ls.predict(feature)
    probab = phish_model_ls.predict(feature)

    if(y_Predict==1):
        return {"type": "{This is a phishing site}"}
    else:
        return {"type": "{This is a legitimate site}"}


if __name__ == "__main__":
    uvicorn.run(app)

