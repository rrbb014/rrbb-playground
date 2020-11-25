""" Randomized answer selection """
import pandas as pd

from tqdm import tqdm
from .model import Model


class RandomizedModel(Model):
    def __init__(self, random_seed=7014):
        self.random_seed = random_seed

    #### Training Interface ####
    def fit(self, train_data: pd.DataFrame):
        self._song_candidates = self._extract_unique_elements(
                train_data=train_data,
                column_name='songs')

        self._tag_candidates = self._extract_unique_elements(
                train_data=train_data,
                column_name='tags')
    
    def _extract_unique_elements(self, train_data, column_name):
        elements = []
        for idx in tqdm(range(train_data.shape[0])):
            elements += train_data[column_name].iloc[idx]
        uniq_elements = sorted(list(set(elements)))
        return uniq_elements

    #### Prediction Interface ####
    def predict(self, pred_data) -> :
        assert all([
            self._song_candidates is not None, 
            self._tag_candidates is not None
            ])

        np.random.seed(self.random_seed)

        predictions = []

        for idx in tqdm(range(pred_data.shape[0])):
            pred_row = pred_data.iloc[0]
            playlist_id = pred_row['id']
            songs = pred_row['songs']
            tags = pred_row['tags']
            
            songs_answer = self._fill_in_blank(
                    input_list=songs,
                    target_number=100,
                    candidates=self._song_candidates)

            tags_answer = self._fill_in_blank(
                    input_list=tags,
                    target_number=10,
                    candidates=self._tag_candidates)

            pred = dict(id=playlist_id, songs=songs_answer, tags=tags_answer)
            predictions.append(pred)

        return predictions    


    def _fill_in_blank(self, input_list, target_number, candidates):
        if len(input_list) >= target_number:
            return input_list

        filled_list = input_list.copy()

        filled_len = len(filled_list)

        while filled_len != target_number:
            if filled_len > target_number:
                filled_list = filled_list[:target_number]
            else:    
                filling_num = target_number - len(filled_list)
                extracted = np.random.choice(candidates, size=filling_num).tolist()
                filled_list += extracted
                filled_list = list(set(filled_list))

            filled_len = len(filled_list)

        return filled_list    
