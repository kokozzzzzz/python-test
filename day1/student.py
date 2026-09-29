import json
from pathlib import Path

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

    def to_dict(self):
        return {"name": self.name, "age": self.age, "score": self.score}


def load_students(file_path):
    """从 JSON 文件加载学生列表，若文件不存在或格式错误则返回空列表。"""
    path = Path(file_path)
    if not path.exists():
        print(f"文件{file_path}不存在")
        return []

    try:
        with open(path,"r",encoding="utf-8") as f:
            data=json.load(f)
            return [Student(**item) for item in data]
    except json.JSONDecodeError as e:
        print(f"JSON格式错误:{e}")
        return []
    except Exception as e:
        print(f"未知错误:{e}")
        return []
         


def save_students(students,file_path):
    """将学生列表保存到 JSON 文件。"""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in students], f, ensure_ascii=False, indent=4)
        print("保存成功！")
    except PermissionError:
        print("没有权限写入该文件！")
    except Exception as e:
        print(f"写入失败：{e}")


if __name__ == "__main__":
    # s = Student("小明", 18, 92.5)
    # print(s)
    data = [{"name": "koko", "age": 20, "score": 100}]
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    students = load_students("students.json")
    students.append(Student("小明", 18, 92.5))
    save_students(students, "students.json")


