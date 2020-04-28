#coding=utf-8
import json

class OperationJson():

    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        with open("../dataconfig/login.json") as fp:
            data = json.load(fp)
            return data
        
    def get_data(self,id):
        return self.data[id]

if __name__ == "__main__":
    oj = OperationJson()
    print(oj.get_data("login"))