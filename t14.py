import pandas as pd
import matplotlib.pyplot as plt
from typing import Union
def smooth_series(file_path: str, window: int) -> pd.DataFrame:
    if window <= 0:
        raise ValueError("window must be a positive integer")
    df = pd.read_csv(file_path)
    if 'date' not in df.columns:
        raise ValueError("Input CSV must contain a 'date' column")
    value_col = 'value' if 'value' in df.columns else [c for c in df.columns if c != 'date'][0]
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)
    df[value_col] = pd.to_numeric(df[value_col], errors='coerce')
    df['smoothed'] = df[value_col].rolling(window=window, center=True, min_periods=1).mean()
    out_df = df[['date', value_col, 'smoothed']].rename(columns={value_col: 'value'})
    out_df.to_csv('smoothed_series.csv', index=False)
    plt.figure(figsize=(10, 5))
    plt.plot(out_df['date'], out_df['value'], label='Original', linewidth=1)
    plt.plot(out_df['date'], out_df['smoothed'], label=f'{window}-point MA', linewidth=2)
    plt.title('Original vs Smoothed Time Series')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('smoothed_series.png')
    plt.show()
    return out_df
if __name__ == "__main__":
    df_out = smooth_series('timeseries.csv', window=5)
    print("Saved: smoothed_series.csv and smoothed_series.png")
    print(df_out.head())
