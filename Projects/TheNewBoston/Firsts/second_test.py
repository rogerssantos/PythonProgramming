def allowedDatingAge(personAge):
    limitDateAge = personAge/2 + 7
    return limitDateAge

for age in range(50, 60, 1):
    limitDateAge = allowedDatingAge(age)
    print("The age of this person is", age, "and he(she) can only date someone who is older than", limitDateAge,"years old")