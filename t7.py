import requests
import csv
def url_status_checker(path: str):
    urls = []
    with open(path, "r") as f:
        urls = [line.strip() for line in f.readlines()]

    status_report = []
    for url in urls:
        try:
            response = requests.get(url)
            status_code = response.status_code
        except requests.exceptions.RequestException as e:
            status_code = "Error" 
            print(f"Error with URL {url}: {e}")
        
        status_report.append([url, status_code])
    with open("status_report.csv", mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Status Code"])  
        writer.writerows(status_report)
    print("Status report saved to 'status_report.csv'.")
if __name__ == "__main__":
    url_status_checker("urls.txt")
