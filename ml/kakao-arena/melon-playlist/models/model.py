#-*- coding: utf-8 -*-

""" Training models abstract class """

from abc import ABCMeta

class Model:
    @abstractmethod
    def fit(self, train_data):
        pass

    @abstractmethod
    def predict(self, pred_data):
        pass
