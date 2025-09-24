import csv
import math

def mean(values):
    return sum(values) / len(values)

def pearson_correlation(x, y):
    n = len(x)
    mean_x, mean_y = mean(x), mean(y)
    num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    den_x = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)))
    den_y = math.sqrt(sum((y[i] - mean_y) ** 2 for i in range(n)))
    return num / (den_x * den_y) if den_x and den_y else 0

def csv_correlation(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader]
    numeric_cols = {}
    for col_idx, col_name in enumerate(header):
        try:
            numeric_cols[col_name] = [float(row[col_idx]) for row in rows]
        except ValueError:
            pass  
    col_names = list(numeric_cols.keys())
    n = len(col_names)
    matrix = []
    for i in range(n):
        row_vals = []
        for j in range(n):
            r = pearson_correlation(numeric_cols[col_names[i]], numeric_cols[col_names[j]])
            row_vals.append(r)
        matrix.append(row_vals)
    with open("correlation_matrix.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([""] + col_names)  # header row
        for i in range(n):
            writer.writerow([col_names[i]] + matrix[i])
    print("Correlation matrix saved to correlation_matrix.csv")
    return matrix
csv_correlation("data.csv")
