import re
import unittest
def analyze_passwords(file_path):
    with open(file_path, "r") as f:
        passwords = [line.strip() for line in f if line.strip()]
    total = len(passwords)
    if total == 0:
        return {
            "average_length": 0,
            "percent_with_specials": 0,
            "percent_meeting_complexity": 0
        }
    avg_len = sum(len(p) for p in passwords) / total
    specials = sum(1 for p in passwords if re.search(r"[^A-Za-z0-9]", p))
    complexity = sum(
        1 for p in passwords
        if len(p) >= 8 and re.search(r"[A-Z]", p) and re.search(r"[a-z]", p) and re.search(r"\d", p)
    )
    return {
        "average_length": avg_len,
        "percent_with_specials": (specials / total) * 100,
        "percent_meeting_complexity": (complexity / total) * 100
    }
class TestPasswordAnalyzer(unittest.TestCase):
    def test_metrics(self):
        file_path = r"C:\Users\sajur\AppData\Local\Programs\Python\Python311\Password.txt"
        result = analyze_passwords(file_path)
        print(result)   
        self.assertIn("average_length", result)
        self.assertIn("percent_with_specials", result)
        self.assertIn("percent_meeting_complexity", result)
if __name__ == "__main__":
    unittest.main()
