def getSex(sex="Unknown"):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

getSex()
getSex("m")
getSex("f")