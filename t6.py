import csv
import re
from typing import List
SEPARATOR_RE = re.compile(r'^\s*\|?\s*(:?-+:?\s*\|+\s*)+:?\s*$')
def split_markdown_row(line: str) -> List[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    cells = [cell.strip() for cell in line.split("|")]
    return cells
def md_table_parser(path: str) -> List[List[List[str]]]:
    tables = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].rstrip("\n")
        if "|" in line and not line.strip().startswith("```"):
            j = i + 1
            while j < n and lines[j].strip() == "":
                j += 1
            if j < n and SEPARATOR_RE.match(lines[j]):
                header_line = line
                sep_line = lines[j].rstrip("\n")
                table_rows = []
                header_cells = split_markdown_row(header_line)
                table_rows.append(header_cells)

                k = j + 1
                while k < n:
                    cur = lines[k].rstrip("\n")
                    if cur.strip() == "":
                        break
                    if "|" not in cur:
                        break
                    if cur.strip().startswith("```"):
                        break
                    row_cells = split_markdown_row(cur)
                    table_rows.append(row_cells)
                    k += 1
                tables.append(table_rows)
                i = k
                continue
        i += 1
    out_csv = "tables.csv"
    with open(out_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for t_idx, table in enumerate(tables, start=1):
            writer.writerow([f"--- TABLE {t_idx} ---"])
            for row in table:
                writer.writerow(row)
            writer.writerow([])
    print(f"Wrote {len(tables)} table(s) to '{out_csv}'")
    return tables
if __name__ == "__main__":
    tables = md_table_parser("notes.md")

    for idx, tbl in enumerate(tables, start=1):
        print(f"\nTABLE {idx}:")
        for r in tbl:
            print(r)
