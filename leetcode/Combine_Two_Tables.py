# SELECT firstName, lastName, city, state
# FROM Person
# LEFT JOIN Address
# ON Person.personId = Address.personId

# ---------------------------------------------------------------
# SELECT Person.FirstName, Person.LastName, Address.City, Address.State
# FROM Person
# JOIN Address
# ON Person.personid = Address.personid
# UNION
# SELECT Person.FirstName, Person.LastName, NULL as City, NULL as State
# FROM Person
# WHERE not exists (SELECT 1 FROM Address WHERE Person.personid = Address.personid)
