from dataclasses import dataclass,asdict
class HelloMetaclass(type):
    def hello(cls):
        return f"Hello  class {cls.__name__}"








@dataclass
class Students(metaclass=HelloMetaclass):
    name: str
    age: int
    @staticmethod
    def find_out_the_name(article):
        return article.name
    @classmethod
    def data_students(cls):
        return cls('Лиза', 23)  
person_1 = Students("Олег", 20)
person_2 = Students('Ирина', 29)
person_3 = Students('Дима', 22)
person_4 = Students('Ольга', 20)
person_5 = Students('Лиза', 23)
print([f"{asdict(person_1)},{asdict(person_2)},{asdict(person_3)},{asdict(person_4)},{asdict(person_5)}"])
print(Students.find_out_the_name(person_2))
person_1 = Students.data_students()
print(asdict(person_1))
print(Students.hello())