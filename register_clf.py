import argparse
import os
from azureml.core import Workspace, Run
from azureml.core.model import Model

parser = argparse.ArgumentParser()
parser.add_argument(
    '--model_path',
    dest="model_path",
    default="data/model_path/")

args = parser.parse_args()
print("all args: ", args)

run = Run.get_context()
try:
    ws = run.experiment.workspace
except AttributeError:
    ws = Workspace.from_config()

model = Model.register(
    ws,
    os.path.join(args.model_path, "model.pkl"),
    model_name="logistic_regression")
