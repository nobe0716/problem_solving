class Employee:
    def __init__(self, _id, _income, _boss):
        self.id = _id
        self.income = _income
        self.boss = _boss

class EmployeeGroup:
    def __init__(self, _income, _employee, _bosses):
        self.income = _income
        self.employee = _employee
        self.bosses = _bosses


def raiseIncome(employee_group_mapping, newbie):
    if employee_group_mapping[newbie.boss.id].employee.id == newbie.boss.id and employee_group_mapping[newbie.boss.id].income < newbie.income: # succeed
        employee_group = employee_group_mapping[newbie.boss.id]
        employee_group.employee = newbie
        employee_group.income = newbie.income
        employee_group.bosses.append(newbie.boss)
    else:
        employee_group = EmployeeGroup(newbie.income, newbie, [])
    employee_group_mapping[newbie.id] = employee_group

    boss = newbie.boss
    while boss is not None:
        if boss not in employee_group.bosses:
            employee_group_of_boss = employee_group_mapping[boss.id]

            if employee_group_of_boss.income < employee_group.income:
                employee_group_mapping[boss.id] = employee_group
                employee_group.bosses.append(boss)

                if employee_group_of_boss.employee.id == boss.id:
                    for e in employee_group_of_boss.bosses:
                        employee_group_mapping[e.id] = employee_group
                        employee_group.bosses += employee_group_of_boss.bosses
                        employee_group_of_boss.bosses.clear()
                else:
                    employee_group_of_boss.bosses.remove(boss)
        boss = boss.boss
    return len(employee_group.bosses)


n = int(input())
i = int(input())
employees = [Employee(0, i, None)]
employee_group_mapping = {0:EmployeeGroup(i, employees[0], [])}

for id in range(1, n + 1):
    i, b = map(int, input().split())
    newbie = Employee(id, i, employees[b])
    employees.append(newbie)
    print(raiseIncome(employee_group_mapping, newbie))
