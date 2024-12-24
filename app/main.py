import pandas as pd
from dotenv import load_dotenv
import time, os
import joblib
from Model_BSHP.processor import Processor
from Model_BSHP.model import RFModel
from Model_BSHP.prepare_data import encode_objects_fit, prepare_to_train, prepare_to_predict, decode_objects
from Model_BSHP.connector import Connector

# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)

# start_time = time.time()
# df = pd.read_json('from_odin_ass_2.json')
# print(len(df))
#
# """
# Fit model
# # """
# base_name = df['base_uid'][0]
# Processor(base_name, df).fit()
# """
# Predict
# """
# base_name = df['base_uid'][0]
# result_df = Processor(base_name, df).predict_process()
# print(result_df.columns)
#
# end_time = time.time()
# finish_time = end_time - start_time
# print('Elapsed time: ', finish_time)

# print(f"compressed Random Forest: {np.round(os.path.getsize('details_cash_flow.model') / 1024 / 1024, 2) } MB")







