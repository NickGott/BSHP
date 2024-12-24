import fastapi
import uvicorn
from data_types import DataRow
from connector import Connector
from processor import Processor
import pandas as pd


app = fastapi.FastAPI(title="BSHP App")


@app.get('/')
async def get_info():
    """
    Root method returns html ok description
    @return: HTML response with ok micro html
    """
    return fastapi.responses.HTMLResponse('<h2>BSHP module</h2> <br> <h3>Connection established</h3>')


@app.post('/fit_model')
def fit(data_in: list[DataRow]) -> str:
    data_fit = pd.DataFrame([row.model_dump() for row in data_in])
    base_name = data_fit['base_uid'][0]
    return Processor(base_name, data_fit).fit_process()


@app.post('/get_predicts')
def predict(data_in: list[DataRow]) -> list[DataRow]:
    data_to_predict = pd.DataFrame([row.model_dump() for row in data_in])
    base_name = data_to_predict['base_uid'][0]
    return Processor(base_name, data_to_predict).predict_process()


@app.post('/get_model_info')
def get_model_info(base_name: str) -> str:
    return Connector(base_name).get_model_status()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8070, log_level="info")
