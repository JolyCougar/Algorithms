# SELECT Name AS Employee
# FROM Employee e
# WHERE e.ManagerId IS NOT NULL AND e.Salary > (SELECT Salary
#                           FROM Employee
#                           WHERE e.ManagerId = Id)

# ----------------------------------------------------
# SELECT m.name as 'Employee'
# FROM employee e
# JOIN employee m on e.id=m.managerId AND m.salary>e.salary
