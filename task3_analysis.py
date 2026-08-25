import os
import pandas as pd

def load_processed(path='data/trendpulse_processed.csv'):
    if not os.path.exists(path):
        raise FileNotFoundError(f'{path} not found — run task2 first')
    return pd.read_csv(path, index_col=0, parse_dates=True)

def compute_top_movers(df, top_n=3):
    start = df.iloc[0]
    end = df.iloc[-1]
    delta = (end - start)
    movers = delta.sort_values(ascending=False).head(top_n)
    return movers

def compute_correlations(df):
    return df.corr()

def save_summary(movers, corr, path='data/summary.csv'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    movers.to_csv(path.replace('.csv', '_top_movers.csv'))
    corr.to_csv(path.replace('.csv', '_correlations.csv'))

def main():
    df = load_processed()
    movers = compute_top_movers(df)
    corr = compute_correlations(df)
    save_summary(movers, corr)
    print('Saved analysis outputs to data/*_top_movers.csv and *_correlations.csv')

if __name__ == '__main__':
    main()
