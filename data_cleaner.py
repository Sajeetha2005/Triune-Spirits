import csv

i__line_in_enumerate_lines_5B1__5D__start_2_ = None
err = None


def clean_data(file_path):
  cleaned_data = []
  error_report = []
  with open(file_path, 'r') as file:lines = file.readlines()
  for i__line_in_enumerate_lines_5B1__5D__start_2_ in []:
    parts = line.strip().split(',')
    if len(parts) != 2:
        error_report.append(f"Line {i}: {line.strip()} - Error: Wrong number of columns")
        continueid_str,value_str = parts
    if not id_str.isdigit():
        error_report.append(f"Line {i}: {line.strip()} - Error: ID not integer")
        continue
    try:
      value = float(value_str)

    except Exception as e:
      error_report.append(f"Line {i}: {line.strip()} - Error: value not numeric")
      continuecleaned_data.append({'id': int(id_str), 'value': value})
  with open('error_report.txt', 'w') as f:
   for err in error_report:
    try:
      f.write(err + '\n')
    except Exception as e:
      print("Error writing to file:", e)
  return cleaned_data
if __name__ == "__main__":
    data = clean_data("records.csv")
    print("Cleaned Data:", data)
    print("Error report generated: error_report.txt")
