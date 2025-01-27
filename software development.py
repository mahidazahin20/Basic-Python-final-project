import re
import datetime


class EmployeeAttendanceTracker:
    def __init__(self, filename="text.txt"):
        self.filename = filename
        self.attendance_records = self.load_attendance_records()

    def load_attendance_records(self):

            with open(self.filename, 'r') as file:
                lines = file.readlines()
                records = {}
                for line in lines:
                    date, employee_id = line.strip().split(',')
                    if date not in records:
                        records[date] = []
                    records[date].append(employee_id)
                return records

    def save_attendance(self):

        with open(self.filename, 'a') as file:
            for date, employees in self.attendance_records.items():
                for employee_id in employees:
                    file.write(f"{date},{employee_id}\n")

    def validate_employee_id(self, employee_id):

        pattern = r'[A-Za-z]{3}\d{4}'
        if re.match(pattern, employee_id):

            print("Valid employee ID.")
            return True

        else:
            print("Invalid employee ID. Please enter a valid ID.")
            return False

    def mark_attendance(self, employee_id):

        if not self.validate_employee_id(employee_id):
            return

        date_today = datetime.datetime.now().strftime("%Y-%m-%d")
        if date_today not in self.attendance_records:
            self.attendance_records[date_today] = []

        if employee_id not in self.attendance_records[date_today]:
            self.attendance_records[date_today].append(employee_id)
            print(f"Attendance marked for employee {employee_id} on {date_today}.")
        else:
            print(f"Attendance already marked for employee {employee_id} on {date_today}.")

    def view_attendance(self, date):

        if date in self.attendance_records:
            print(f"Attendance for {date}:")
            for employee_id in self.attendance_records[date]:
                print(employee_id)
        else:
            print(f"No attendance records found for {date}.")


def main():
    tracker = EmployeeAttendanceTracker()
    while True:
        print("\nAttendance Tracker Menu:")
        print("1. Mark attendance")
        print("2. View Previous attendance for a specific date")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            employee_id = input("Enter employee ID: ").strip()
            tracker.mark_attendance(employee_id)
        elif choice == '2':
            date = input("Enter the date: ").strip()
            tracker.view_attendance(date)
        elif choice == '3':
            tracker.save_attendance()
            print("Attendance records saved.")
            break
        else:
            print("Invalid ID. Please select a valid format.")
if __name__ == "__main__":
    main()