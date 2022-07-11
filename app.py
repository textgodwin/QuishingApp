from fastapi import FastAPI
import joblib
import uvicorn

import pickle
from models import Website

app = FastAPI()
# pkl
phish_model = open('phishing.pkl', 'rb')
phish_model_ls = joblib.load(phish_model)


@app.get("/")
def greet():
    return {"Hello World"}

app = FastAPI()
#pkl
phish_model = open('phishing.pkl', 'rb')
phish_model_ls = joblib.load(phish_model)

#ML Aspect
@app.post('/predict')
async def predict(features):
	url = []
	url.append(str(features))
	y_Predict = phish_model_ls.predict(url)
	if y_Predict == 1:
		result = "This is a phishing Site"
	else:
		result = "This is a legitimate Site"
	return result


if __name__ == "__main__":
    uvicorn.run(app)
