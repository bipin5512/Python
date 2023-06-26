class Employee:
    def __init__(self, name, emp_id, department):
        self._name = name
        self._emp_id = emp_id
        self._department = department
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if value.strip():  # Check if the value is not blank after stripping leading/trailing whitespaces
            self._name = value
        else:
            print("Invalid name value. Name cannot be blank.")
    
    @property
    def emp_id(self):
        return self._emp_id
    
    @emp_id.setter
    def emp_id(self, value):
        if value.strip():  # Check if the value is not blank after stripping leading/trailing whitespaces
            self._emp_id = value
        else:
            print("Invalid emp_id value. emp_id cannot be blank.")
    
    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, value):
        if value.strip():  # Check if the value is not blank after stripping leading/trailing whitespaces
            self._department = value
        else:
            print("Invalid department value. Department cannot be blank.")
    
    def display_info(self):
        print("Employee Information:")
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)


emp = Employee("John Doe", "12345", "Engineering")
emp.display_info()

emp.name = "  "   # Try to assign a blank value to the name
emp.emp_id = ""    # Try to assign a blank value to the emp_id
emp.department = "Sales"

emp.display_info()