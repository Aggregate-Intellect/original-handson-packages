import pandas as pd
import mlflow.pyfunc

# Load the model in `python_function` format
loaded_model = mlflow.pyfunc.load_model('./iris_model_pyfunc')

# Create test input
test_input = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]])

# Evaluate the model
test_predictions = loaded_model.predict(test_input)

# Print the predictions
print(test_predictions)