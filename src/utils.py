import pandas as pd
import numpy as np

def create_rfm_features(df):
    """Generate Recency, Frequency, Monetary features for each customer."""
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    })

    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    return rfm


def create_behavioral_features(df):
    """Generate behavioral features such as AvgBasketSize, AvgUnitPrice, UniqueProducts."""
    behavioral = df.groupby('CustomerID').agg({
        'Quantity': 'mean',
        'UnitPrice': 'mean',
        'StockCode': 'nunique'
    })

    behavioral.columns = ['AvgBasketSize', 'AvgUnitPrice', 'UniqueProducts']
    return behavioral


def merge_features(rfm, behavioral):
    """Merge RFM and behavioral features into a single DataFrame."""
    return rfm.join(behavioral, how='inner')
