class Student:
    """学生类：保存姓名、年龄和分数。"""

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, score={self.score})"

    def show_info(self):
        print(self)


if __name__ == "__main__":
    s = Student("小明", 18, 92.5)
    print(s)
