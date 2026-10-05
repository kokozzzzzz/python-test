from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    skills: list[str]


student = Student(
    name="koko",
    age=20,
    skills=["Python", "Java"]
)

print(student)