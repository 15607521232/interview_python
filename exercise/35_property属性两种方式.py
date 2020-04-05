#coding=utf-8

class Goods():

    #3.1 装饰器方式

    # def __init__(self):
    #
    #     self.original_price = 100
    #
    #     self.discount = 0.8
    #
    #
    # @property
    # def price(self):
    #     new_price = self.original_price * self.discount
    #     return new_price
    #
    # @price.setter
    # def price(self,value):
    #     self.original_price = value
    #
    # @price.deleter
    # def price(self):
    #     del self.original_price

    #3.2类属性方式，创建值为property对象的类属性

    def __init__(self):

        self.original_price = 100
        self.discount = 0.8

    def get_price(self):
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self,value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    '''
    property方法中有个四个参数
    第一个参数是方法名，调用 对象.属性 时自动触发执行方法
    第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
    第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
    第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
    '''
    PRICE = property(get_price,set_price,del_price,"价格属性描述")


g = Goods()
# print(g.price)

# 修改商品原价
# g.price = 200
# print(g.price)

# 删除商品原价
#del g.price

#3.2调用
print(g.PRICE)
#修改商品原价
g.PRICE = 200
print(g.PRICE)
print(Goods.PRICE.__doc__)
del g.PRICE
