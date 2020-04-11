class A:
    def __init__(self):
        print("in a Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 is working")


class B:
    def __init__(self):
        print("in B Init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

c1 = C()
c1.feature1()