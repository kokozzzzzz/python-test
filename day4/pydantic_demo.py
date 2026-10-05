from pydantic import BaseModel,Field
from pydantic import ValidationError


class User(BaseModel):
    name: str
    age: int = Field(gt=0,le=150)


try:
    user = User(
        name="koko",
        age=20
    )
except ValidationError as e:
    print(e)


# print(user)
# print(user.name)
# print(user.age)

data = user.model_dump() #类转换成字典类型
print(data)
print(type(data))

json_data = user.model_dump_json() #类转换成json字符串
print(json_data)
print(type(json_data))