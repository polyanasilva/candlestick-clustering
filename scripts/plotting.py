import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import seaborn as sns

def plot_box(data, column):
    sns.boxplot(data=data[column])
    plt.show()

def plot_candlestick(df, title='Candlestick Chart'):
    """Plots a candlestick chart using matplotlib."""
    df['date_num'] = mdates.date2num(df['date'])
    ohlc = df[['date_num', 'open', 'high', 'low', 'close']].values
    fig, ax = plt.subplots(figsize=(10, 6))
    candlestick_ohlc(ax, ohlc, width=0.6, colorup='g', colordown='r')
    ax.xaxis_date()
    plt.title(title)
    plt.show()

def plot_clusters(df, cluster_column):
    """Plots candles belonging to each cluster."""
    for cluster in df[cluster_column].unique():
        cluster_data = df[df[cluster_column] == cluster]
        plot_candlestick(cluster_data, title=f'Cluster {cluster}')
