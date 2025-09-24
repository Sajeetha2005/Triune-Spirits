import csv
def schedule_jobs(file_path):
    jobs = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            jobs.append({
                'job_id': row['job_id'],
                'duration': int(row['duration']),
                'deadline': int(row['deadline'])
            })
    jobs.sort(key=lambda x: x['deadline'])
    current_time = 0
    schedule = []
    for job in jobs:
        start_time = current_time
        finish_time = start_time + job['duration']
        status = "On Time" if finish_time <= job['deadline'] else "Late"

        schedule.append({
            'job_id': job['job_id'],
            'start_time': start_time,
            'finish_time': finish_time,
            'status': status
        })
        current_time = finish_time
    with open('schedule.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['job_id','start_time','finish_time','status'])
        writer.writeheader()
        for row in schedule:
            writer.writerow(row)
    return schedule
if __name__ == "__main__":
    sched = schedule_jobs("jobs.csv")
    print("Schedule saved to schedule.csv")
    print(sched)
