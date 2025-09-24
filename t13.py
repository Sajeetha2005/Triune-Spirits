from typing import List, Dict
import datetime
def format_logs(file_path: str) -> List[Dict]:
    logs = []
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
            try:
                timestamp_str, message = line.split(' ', 1)
                timestamp = datetime.datetime.fromisoformat(timestamp_str)
                logs.append({'timestamp': timestamp, 'message': message})
            except ValueError:
                print(f"Warning: Skipping invalid line -> {line}")
    
    return logs
if __name__ == "__main__":
    result = format_logs('logs.txt')
    for log in result:
        print(log)
