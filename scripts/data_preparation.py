import pandas as pd

def load_data(file_path):
    """Loads the dataset."""
    return pd.read_csv(file_path, delimiter=',')

def create_columns(df):
    """Adds necessary columns to the dataframe."""
    df['body'] = ((df['Close'] - df['Open']) / df['Open']) * 100
    df['upper Shadow'] = ((df['High'] - df[['Open', 'Close']].max(axis=1)) / df['Open']) * 100
    df['lower Shadow'] = ((df[['Open', 'Close']].min(axis=1) - df['Low']) / df['Open']) * 100
    return df

def remove_outliers(df, column, limite):
    return df[(df[column] > int(limite))]


