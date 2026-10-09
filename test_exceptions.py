import pytest
from Exceptions import ExceptionsDemo, MyException  

def test_division_cero():
    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):   
        demo.divide(10,0)


def test_division_with_string():
    demo = ExceptionsDemo()
    with pytest.raises((TypeError, ZeroDivisionError)):   
        demo.divide('8',0)

def test_access_list_out_of_bounds():
    demo = ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([1,2,3], 7)

def test_access_list_dic():
    demo = ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_dict({"color": "rojo","from": "round"},"sabor")

def test_read_file():
    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file("sabor.txt")

def test_atribute():
    demo = ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(object())

def test_check_positive():
    demo = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-3)