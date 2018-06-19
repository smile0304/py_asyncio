import numbers


class Field():
    pass


class ModeMetaclass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        fields = {}
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)
        for key,value in attrs.items():
            if isinstance(value,Field):
                fields[key] = value

        attrs_meta = attrs.get("Meta",None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta,"db_table",None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kwargs)


class IntField(Field):
    #数据描述符
    def __init__(self,db_column,min_value=None,max_value=None):
        self._value = None
        self.db_column = db_column
        self.min_value = min_value
        self.max_value = max_value
        if self.min_value is not None:
            if not isinstance(self.min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif self.min_value<0:
                raise ValueError("min_value must be positice int")
        if self.max_value is not None:
            if not isinstance(self.max_value,numbers.Integral):
                raise ValueError("max_value must be int")
            elif self.max_value<0:
                raise ValueError("max_value must be positice int")

        if self.min_value and max_value is not None:
            if self.min_value > self.max_value:
                raise ValueError("min_value must be smaller than max_value")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError(" int value need")

        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value")
        self._value = value


class CharField(Field):
    def __init__(self,db_column,max_length=None):
        self._value = None
        self.db_column = db_column

        if max_length is None:
            raise ValueError("you must spcify max_length for charfied")
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value,str):
            raise ValueError(" String value need")

        if len(value) > self.max_length:
            raise ValueError("value length excess len of max_length")
        self._value = value


class BaseModel(metaclass=ModeMetaclass):
    def __init__(self, *args, **kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        return super().__init__()

    def save(self):
        filds = []
        values = []
        for key,value in self.fields.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            filds.append(db_column)
            value = getattr(self,key)
            values.append(str(value))
        sql = "insert {db_table}({filds}) value ({values})".format(db_table=self._meta["db_table"],filds=",".join(filds), values=",".join(values))
        print(sql)
        pass


class User(BaseModel):
    name = CharField(db_column="name",max_length=10)
    age = IntField(db_column="age",min_value=0,max_value=100)

    class Meta:
        db_table = "user_table"

if __name__ == "__main__":
    user = User()
    user.name = "bobby"
    user.age =28
    user.save()

