def allowedDatingAge(myAge):
    girlAge = myAge/2 + 7
    return girlAge

myLimit = allowedDatingAge(22)
myFriendLimit = allowedDatingAge(49)
print("I can date girls that are ", myLimit, " or older")
print("My friend can date girls that are ", myFriendLimit, " or older")