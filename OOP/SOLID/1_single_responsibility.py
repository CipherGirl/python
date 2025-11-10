# A class should have only one reason to change — one job only.

"""Bad Example

class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Report: {self.data}"

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.generate())
"""

# Correct Way

class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Report: {self.data}"


class ReportSaver:
    def save_to_file(self, report: Report, filename):
        with open(filename, "w") as f:
            f.write(report.generate())

report = Report("Important Data")
report_saver = ReportSaver()

report_saver.save_to_file(report,"5_nov.txt")


"""
💡 Simple Explanation:

“Each class now has one reason to change. If the ReportSaver changes, I touch only ReportSaver class. 
If the Report generator changes, only modify the Report class. 
This keeps the code modular and easy to maintain.”
"""


