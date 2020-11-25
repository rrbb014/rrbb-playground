#-*- coding: utf-8 -*-
""" Training script"""

import argparse
from common import read_json



def train(train_data, model_type):
    """ Training Main Script """
    model = get_model_object(model_type)
    model.fit()

    return model
    

def get_model_object(model_type):
    if model_type in ['random', 'randomize']:
        from models.randomize import RandomizedModel
        model = RandomizedModel()
    elif model_type in []:
        raise Exception("no model")

    return model

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument(
        "--model-type", "-m", type='str', choices=[],
        help="recommendation model type key"
    )
    PARSER.add_argument(
        "--train-data", type=str,
        help="training dataset path"
    )

    ARGS = vars(parser.parse_args())

    # 
    # 1. Prepare training data
    #
    train_filepath = ARGS['train_data']
    train_dict = read_json(train_filepath)
    X_train = pd.DataFrame(train_dict)

    #
    # 2. Train model
    #
    model_type = ARGS["model_type"]

    train(
        train_data=X_train,
        model_type=model_type)

