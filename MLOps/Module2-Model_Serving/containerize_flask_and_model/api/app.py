from flask import Flask, request, jsonify
import mlflow.pyfunc
import pandas as pd
import json

# Name of the apps module package
app = Flask(__name__)

# Load in the model at app startup
model = mlflow.pyfunc.load_model('./model')

# Load in our meta_data
f = open("./model/code/meta_data.txt", "r")
load_meta_data = json.loads(f.read())

# Meta data endpoint
@app.route('/', methods=['GET'])
def meta_data():

	return jsonify(load_meta_data)

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
	req = request.get_json()
	
	# Log the request
	print({'request': req})

	# Format the request data in a DataFrame
	inf_df = pd.DataFrame(req['data'])

	# Get model prediction - convert from np to list
	pred = model.predict(inf_df).tolist()

	# Log the prediction
	print({'response': pred})

	# Return prediction as reponse
	return jsonify(pred)

app.run(host='0.0.0.0', port=5000)
