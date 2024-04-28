print("Hello from Python")
print(type(2))
my_name = "Vasiliy"
print(my_name)
age = 21
age = age + 1
print(age)
age += 2
print(age)
a = [] #кортеж
print(type(a))
print(len(a))
a.append(2)
print(a)
print(len(a))
a.append("abc")
print(a)
a.append(True)
len(a)
print(a[-1])
a.clear()
print(a)
b = (2, "abc") #список
print(b)
print(type(b))
print(b[0])
print(b[1])
print(b.index("abc"))
#словари
person = {"name": "Vasiliy"}
print(person)
print(type(person))
print(person["name"])
print(person.get("age"))
person['happy'] = True
print(person)
print(len(person))
print(person.keys())
print(person.values())
print(type(person.keys()))
print(list(person.keys()))
print(type(list(person.keys())))
print(list(person.values())[0])
person["hobbies"] = ["books","snowbording"]
print(person)
person["hobbies"].pop()
print(person)
del person["hobbies"]
print(person)
#копирование по ссылке
another_person = person
another_person["name"] = "Bob"
print(another_person)
print(person)

numbers = [1,2]
another_numbers = numbers
numbers.append(3)
#копирование словарей или списков это копирование по ссылке
#наборы
my_set = {"abc","b",10}
print(my_set)
print(type(my_set))
my_set.add(True)
#наборы не сохраняют дубликатов
#контейнерные типы в питоне
#список - квадратные скобки
#кортеж - круглые скобки
#словари
#списки можно изменять
#словари наборо изменяемы в питоне
#список может иметь одинаковые значения
#набор может содержать только уникальные значения
import Module1
print(Module1.sum(4,6))
