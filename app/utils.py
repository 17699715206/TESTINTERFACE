class test():
    def testtt(self, kwargs={}):

        print(kwargs["name"])







if __name__ == '__main__':
    dict = {"name":"张三"}
    print(type(dict))
    test().testtt(dict)
