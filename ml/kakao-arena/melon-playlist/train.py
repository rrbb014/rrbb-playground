#-*- coding: utf-8 -*-
""" Training script"""

import argparse
from common import read_json
from model


def train():
    """ Training Main Script """
    pass

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

    train_filepath = ARGS['train_data']

    train_dict = read_json(train_filepath)
    X_train
