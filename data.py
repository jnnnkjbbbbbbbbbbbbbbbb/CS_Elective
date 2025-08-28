ages = [23, 25, 22, 30, 28, 23,26]
average_ages=sum(ages)/len(ages)
print("Average age:",average_ages)
unique_ages=set(ages)
print("unique_ages",unique_ages)

food = ["apple", "orange", "grapes", "shrimp","sinigang"]
food.append("adobo")
food.append("biscuits")
food.remove("biscuits")
print("fruit",food)




birth_date=(2,"Feb",2025)
birth_date[1]="March"
print(birth_date[0])

participant = {
    "name":"Rumi",
    "age": 20,
    "gender":"F"
}
print(participant["age"] )
participant["score"]=95


student= {
    "Name":"Jaylene",
    "Favorite Food":"EveryEgg"
}
student["favorite sport"] ="Badminton"
print (student["Name"])
print (student["Favorite Food"])
print (student["favorite sport"])


fruits={"apple", "banana", "apple","mango","banana"}
print(fruits)
fruits.add("cherry")
fruits.remove("apple")
print(fruits)
