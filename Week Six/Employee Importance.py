class Solution:
    def getImportance(self, employees, id: int) -> int:
        if len(employees) == 0:
            return 0
        emp = self.findEmp(employees, id)
        if emp:
            return self.helper(emp, employees)
        return 0

    def helper(self, employee, employees):
        if len(employee.subordinates) == 0:
            return employee.importance
        summ = 0
        for emp in employee.subordinates:
            currEmp = self.findEmp(employees, emp)
            summ += self.helper(currEmp, employees)
        return summ + employee.importance

    def findEmp(self, employees, id):
        for emp in employees:
            if emp and emp.id == id:
                return emp
