import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_processed(path='data/trendpulse_processed.csv'):
    return pd.read_csv(path, index_col=0, parse_dates=True)

def plot_timeseries(df, out='output/trend_timeseries.png'):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    plt.figure(figsize=(10,6))
    for col in df.columns:
        plt.plot(df.index, df[col], label=col)
    plt.legend()
    plt.title('TrendPulse: Interest Over Time')
    plt.tight_layout()
    plt.savefig(out)
    plt.close()

def plot_correlation(df, out='output/corr_heatmap.png'):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    corr = df.corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation between keywords')
    plt.tight_layout()
    plt.savefig(out)
    plt.close()

def main():
    df = load_processed()
    plot_timeseries(df)
    plot_correlation(df)
    print('Saved plots to output/')

if __name__ == '__main__':
    main()
