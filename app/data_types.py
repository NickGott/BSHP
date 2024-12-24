from pydantic import BaseModel


class DataRow(BaseModel):
    """
    Loading, input or output data row
    """
    base_uid: str
    document: str
    article_cash_flow: str
    details_cash_flow: str
    qty: float
    price: float
    sum: float
    year: str
    unit_of_count: str
    with_without_count: bool
    moving_type: str
    base_document: str
    customer: str
    operation_type: str
    agreement_name: str



class BaseName(BaseModel):
    base_name: str
