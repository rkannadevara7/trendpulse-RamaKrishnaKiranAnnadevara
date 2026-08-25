import os
import pandas as pd

def load_csv(path='data/trendpulse.csv'):
    if not os.path.exists(path):
        raise FileNotFoundError(f'{path} not found — run task1 first')
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    return df

def clean_and_smooth(df, window=3):
    df = df.copy()
    df = df.fillna(method='ffill').fillna(method='bfill')
    df = df.rolling(window=window, min_periods=1).mean()
    return df

def save_processed(df, path='data/trendpulse_processed.csv'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path)

def main():
    df = load_csv()
    df2 = clean_and_smooth(df)
    save_processed(df2)
    print('Saved processed data to data/trendpulse_processed.csv')

if __name__ == '__main__':
    main()
