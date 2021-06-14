import torch
import pickle

class ModelWrapper():
  def __init__(self, model, tokenizer):
    self._model = model
    self._tokenizer = tokenizer

  def predict(self, data):
    input_ids = torch.tensor([self._tokenizer.encode(data.iloc[0]['text'], add_special_tokens=True)])

    return self._model(input_ids)[0]

def _load_pyfunc(path):
  # Load the model object
  model = torch.load(f'{path}/model.pt')

  # Load in the tokenizer
  tokenizer = torch.load(f'{path}/tokenizer.pt')

  return ModelWrapper(
      model=model,
      tokenizer=tokenizer,
  )