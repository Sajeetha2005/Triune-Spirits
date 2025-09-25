import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys

def visualize_timeline(file_path, output_format='png'):
    try:
        df = pd.read_csv(file_path, sep=None, engine='python')
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)
    df.columns = df.columns.str.strip().str.lower()
    if 'timestamp' not in df.columns or 'event' not in df.columns:
        print("CSV must have 'timestamp' and 'event' columns.")
        print("Available columns:", df.columns.tolist())
        sys.exit(1)
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna(subset=['timestamp'])
    df = df.sort_values('timestamp')
    plt.figure(figsize=(12, 4))
    plt.plot(df['timestamp'], [1]*len(df), "ro")
    for i, row in df.iterrows():
        plt.text(row['timestamp'], 1.02, row['event'], rotation=45, ha='right')

    plt.yticks([])
    plt.title("Event Timeline")
    plt.xlabel("Timestamp")
    plt.tight_layout()
    plt.savefig(f"timeline.{output_format}")
    print(f"Timeline saved as timeline.{output_format}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize event timeline from CSV")
    parser.add_argument("file_path", help="Path to events CSV file")
    parser.add_argument("--format", default="png", help="Output format: png, pdf, jpg, etc.")
    args = parser.parse_args()

    visualize_timeline(args.file_path, args.format)
