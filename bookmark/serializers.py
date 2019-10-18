'''
定义一个序列化器
'''


from rest_framework import serializers
from .models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    '''
    书籍  数据序列化器
    serializer不是只能为数据库模型类定义，也可以为非数据库模型类的数据定义。serializer是独立于数据库之外的存在。
    '''
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()
    published_time = serializers.DateTimeField()
    last_updated_time = serializers.DateTimeField()



    class Meta:
        model = BookInfo  # 指明该序列化器处理的数据字段从模型类BookInfo参考生成
        fields = '__all__'  #  指明该序列化器包含模型类中的哪些字段，'__all__'指明包含所有字段



'''
serializer不是只能为数据库模型类定义，也可以为非数据库模型类的数据定义。serializer是独立于数据库之外的存在。

定义好Serializer类之后，就可以创建Serializer对象了。
Serializer的构造方法为：

Serializer(instance=None, data=empty, **kwarg)

说明：

1）用于序列化时，将模型类对象传入instance参数

2）用于反序列化时，将要被反序列化的数据传入data参数

3）除了instance和data参数外，在构造Serializer对象时，还可通过context参数额外添加数据，如
serializer = AccountSerializer(account, context={'request': request})


通过context参数附加的数据，可以通过Serializer对象的context属性获取。




'''