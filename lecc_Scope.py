x0 = 10


def move(t):
    x = x0 * t
    return x


print(move(3))
# print(x)

a = "Good"


def test_local_data():
    a ="bad"
    print(a, id(a))


test_local_data()
print(a, id(a))

