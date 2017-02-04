
class Employee:
    def __init__(self, _id, _income, _boss):
        self.id = _id
        self.income = _income
        self.boss = _boss
        self.raised = 0
        self.raiser = _id


def invoke_raise(employees, employee):
    employee.raised = 0

    boss = employees[employee.boss]
    while True:
        if employee.income <= employees[boss.raiser].income:
            break

        if boss.raiser != boss.id:
            employees[boss.raiser].raised -= 1
        boss.raiser = employee.id
        employee.raised += 1

        raised_by_boss = boss.raised
        if raised_by_boss > 0:
            employee.raised += raised_by_boss
            for _ in range(raised_by_boss):
                boss = employees[boss.boss]
                if boss.raiser != boss.id:
                    employees[boss.raiser].raised -= 1
                boss.raiser = employee.id

        if boss.boss is None:
            break
        boss = employees[boss.boss]
    return employee.raised

n = int(input())
i = int(input())
employees = [Employee(0, i, None)]

for i in range(1, n + 1):
    income, boss = map(int, input().split())
    employee = Employee(i, income, boss)
    employees.append(employee)
    raised = invoke_raise(employees, employee)
    print(raised)
