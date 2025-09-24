import pandas as pd
def generate_report(file_paths, key_cols, value_col, agg_func="sum"):
    dfs = [pd.read_csv(fp) for fp in file_paths]
    df = pd.concat(dfs, ignore_index=True)
    df.set_index(key_cols, inplace=True)
    report = pd.pivot_table(
        df.reset_index(),
        index=key_cols,
        values=value_col,
        aggfunc=agg_func,
    )
    report.to_csv("report.csv")
    return report
if __name__ == "__main__":
    file_paths = ["data1.csv", "data2.csv", "data3.csv"]   
    key_cols = ["Region", "Product"]                      
    value_col = "Sales"                                   
    report = generate_report(file_paths, key_cols, value_col, agg_func="sum")
    print("Report generated:\n", report)
