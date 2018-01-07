#!/usr/bin/python
# -*- coding: utf-8 -*-

import inspect


class EnumItem(object):
    creation_counter = 0

    def __init__(self, value):
        self.value = value
        self.creation_order = EnumItem.creation_counter
        EnumItem.creation_counter += 1


class EnumMeta(type):
    def __new__(mcs, classname, bases, class_dict):
        cls = type.__new__(mcs, classname, bases, class_dict)
        items = sorted(inspect.getmembers(cls, lambda o: isinstance(o, EnumItem)), key=lambda i: i[1].creation_order)

        cls.initialize()
        for i, item in enumerate(items):
            name = item[0]
            value = item[1].value

            # Add the translation to the list
            cls.values.append((name, value))

            # Modify the property value to its index
            setattr(cls, name, str(i))

        return cls


class Enum(object):
    __metaclass__ = EnumMeta

    values = []

    @classmethod
    def initialize(cls):
        cls.values = []

    @classmethod
    def to_tuples(cls):
        tuples = []
        for i, (key, value) in enumerate(cls.values):
            tuples.append((str(i), value))
        return tuples

    @classmethod
    def to_string(cls, value):
        return cls.values[int(value)][0]

    @classmethod
    def to_value(cls, value):
        return cls.values[int(value)][1]

    @classmethod
    def to_inx(cls, value):
        for i, (key, value) in enumerate(cls.values):
            if value == key:
                return i
        raise Exception(u'Theres no {} in enum {}'.format(value, cls))