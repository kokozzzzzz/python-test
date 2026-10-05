
def num(n):
    for i in range(n):
        yield i


def read_lines(path):
    with open(path,"r",encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def fake_stream():
    words = ["Hello", " ", "AI", " ", "World"]

    for word in words:
        yield word


# for line in read_lines("data/test.txt"):
#     print(line)

for chunk in fake_stream():
    print(chunk, end="", flush=True)


