class EmployeeAttendanceTracker:
    def int(self, emp_id, name):
        self.emp_id= emp_id
        self.name=name

    def validate_emp_id(self, emp_id):
        if emp_id.startswith("reg") and emp_id[5:].is_digit(1-9):
            return True

while True:
    print("Employee attendance tracker:")


