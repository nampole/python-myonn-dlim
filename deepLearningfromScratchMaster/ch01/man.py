# coding: utf-8
class Man:
    """サンプルクラス"""

    def __init__(self, name):
        self.name = name
        print("Initilized! 초기화 되었습니다!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("대한민국")
m.hello()
m.goodbye()