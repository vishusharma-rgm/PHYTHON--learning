class Employee:
    company = "Google"
    name = "unknown"
    salary = 0
    location = "Earth"
   
    def getDetails(self):
        return f"Name: {self.name}, Salary: {self.salary}, Location: {self.location}"
    
vishu = Employee()
print(vishu.getDetails())  # Output: Name: unknown, Salary: 0,  
