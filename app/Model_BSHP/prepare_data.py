from sklearn.model_selection import train_test_split
import pandas as pd


def encode_objects_fit(df: pd.DataFrame):
    df.drop(['base_uid', 'document'], axis=1, inplace=True)
    neworder = ['qty', 'price', 'sum', 'customer', 'operation_type', 'moving_type', 'base_document', 'agreement_name',
                'article_cash_flow', 'details_cash_flow', 'with_without_count', 'unit_of_count', 'year']
    df = df.reindex(columns=neworder)
    target_list = ['article_cash_flow', 'details_cash_flow', 'year', 'unit_of_count', 'with_without_count']
    target_dict = {}
    df = df.fillna(0)
    df.with_without_count = df.with_without_count.astype('str')
    list_cols = ['article_cash_flow', 'details_cash_flow', 'year', 'customer', 'operation_type', 'moving_type',
                 'base_document', 'agreement_name', 'unit_of_count', 'with_without_count']
    for col in list_cols:
        details = df[col].unique()
        numbers = [i for i in range(len(details))]
        details_dict = dict(zip(details, numbers))
        if col in target_list:
            target_dict[col] = details_dict
        df[col] = df[col].apply(lambda x: details_dict[x])
        df[col] = df[col].astype('int')

    return df, target_dict


def prepare_to_train(df: pd.DataFrame, target_name: str):
    if target_name == 'article_cash_flow':
        x = df.drop(columns=[target_name, 'details_cash_flow', 'year', 'unit_of_count', 'with_without_count'], axis=1)
        y = df[target_name]
    elif target_name == 'details_cash_flow':
        x = df.drop(columns=[target_name, 'year', 'unit_of_count', 'with_without_count'], axis=1)
        y = df[target_name]
    elif target_name == 'with_without_count':
        x = df.drop(columns=[target_name, 'year', 'unit_of_count'], axis=1)
        y = df[target_name]
    elif target_name == 'unit_of_count':
        x = df.drop(columns=[target_name, 'year'], axis=1)
        y = df[target_name]
    elif target_name == 'year':
        x = df.drop(columns=[target_name], axis=1)
        y = df[target_name]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.05, random_state=4)

    return x_train, x_test, y_train, y_test


def prepare_to_predict(df: pd.DataFrame):
    df.drop(['base_uid', 'document'], axis=1, inplace=True)
    neworder = ['qty', 'price', 'sum', 'customer', 'operation_type', 'moving_type', 'base_document', 'agreement_name',
                'article_cash_flow', 'details_cash_flow', 'with_without_count', 'unit_of_count', 'year']
    df = df.reindex(columns=neworder)
    target_list = ['article_cash_flow', 'details_cash_flow', 'with_without_count', 'unit_of_count', 'year']
    df = df.fillna(0)
    df.drop(target_list, axis=1, inplace=True)
    list_cols = ['customer', 'operation_type', 'moving_type', 'base_document', 'agreement_name']
    for col in list_cols:
        details = df[col].unique()
        numbers = [i for i in range(len(details))]
        details_dict = dict(zip(details, numbers))
        df[col] = df[col].apply(lambda x: details_dict[x])
        df[col] = df[col].astype('int')
    return df


def decode_objects(predicts: list, target_dict: dict):
    result_list = []
    for i in range(len(predicts)):
        for key in target_dict.keys():
            if predicts[i] == target_dict[key]:
                result_list.append(key)
    return result_list
