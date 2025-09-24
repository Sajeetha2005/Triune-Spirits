import csv
from typing import List, Dict

def prioritize_tasks(file_path: str) -> List[Dict]:
    """
    Reads tasks from a CSV file and ranks them based on a computed score.
    
    Ranking logic:
    - Score = urgency × impact
    - Higher score = higher priority
    - Returns a list of dictionaries sorted in descending order of score
    """
    tasks = []
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    urgency = float(row['urgency'])
                    impact = float(row['impact'])
                    score = urgency * impact
                    row['urgency'] = urgency
                    row['impact'] = impact
                    row['score'] = score
                    tasks.append(row)
                except ValueError:
                    print(f"Skipping task {row.get('task_id')} due to invalid urgency/impact")
        tasks.sort(key=lambda x: x['score'], reverse=True)
        return tasks
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
        return []
if __name__ == "__main__":
    file_path = "C:\Users\Rams\OneDrive\Desktop\tasks.csv"  
    prioritized = prioritize_tasks(file_path)
    
    if prioritized:
        print("\n=== Task Priorities ===")
        for i, task in enumerate(prioritized, start=1):
            print(f"Priority {i}: Task {task['task_id']} "
                  f"(Urgency: {task['urgency']}, Impact: {task['impact']}, Score: {task['score']})")
    else:
        print("No tasks to display.")
