import os
import sys
import logging
import pandas as pd

try:
    from pytrends.request import TrendReq
except Exception:
    TrendReq = None
    logging.basicConfig()
    logging.error('pytrends is not installed or failed to import. Run `pip install -r requirements.txt`.')

def fetch_trends(keywords=None, timeframe='now 7-d', geo=''):
    if TrendReq is None:
        raise RuntimeError('pytrends is not available; install requirements first')
    if keywords is None:
        keywords = ['Python', 'AI', 'Bitcoin', 'Football']
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)
        df = pytrends.interest_over_time()
    except Exception as e:
        logging.exception('Failed to fetch trends: %s', e)
        return pd.DataFrame()

    if df is None or df.empty:
        return pd.DataFrame()
    df = df.drop(columns=['isPartial']) if 'isPartial' in df.columns else df
    return df

def save_csv(df, path='data/trendpulse.csv'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # ensure index is saved (timestamps)
    df.to_csv(path, index=True)

def main():
    try:
        df = fetch_trends()
    except RuntimeError as e:
        print(str(e))
        sys.exit(1)

    if df.empty:
        print('No trend data fetched. Check network, keywords or pytrends access.')
        return
    try:
        save_csv(df)
        print('Saved raw trend data to data/trendpulse.csv')
    except Exception as e:
        logging.exception('Failed to save CSV: %s', e)
        print('Failed to save CSV:', e)

if __name__ == '__main__':
    main()
