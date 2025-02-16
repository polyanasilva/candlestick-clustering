from data_preparation import load_data, create_columns
from clustering import clusterize
from plotting import plot_candlestick, plot_clusters

def main():
    # Load data
    data = load_data('data/agzdus.txt')

    # Prepare data
    data = create_columns(data)
    
    # Cluster body, upper shadows, and lower shadows
    _, data = clusterize(data, 'body', n_clusters=11)
    # _, data = clusterize(data, 'upper_shadow', n_clusters=5)
    # _, data = clusterize(data, 'lower_shadow', n_clusters=5)
    
    # # Plot results
    # plot_candlestick(data, 'Candlestick with complete clustering')
    plot_clusters(data, 'body_cluster')

if __name__ == "__main__":
    main()

