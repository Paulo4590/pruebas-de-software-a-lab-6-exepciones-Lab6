import pytest
from Exceptions import ExceptionsDemo, MyException  

def test_division_zero():
    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10, 0)

def test_division_with_str():
    demo = ExceptionsDemo()
    with pytest.raises((TypeError,ZeroDivisionError)):
        demo.divide("10", 0)

def test_access_list():
    demo = ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([1,2,3], 7)

def test_access_dict():
    demo = ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_dict({"a": 1, "b": 2}, "c")

def test_read_file():
    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file("sabor.txt")

def test_access_attribute():
    demo = ExceptionsDemo()
    class Dummy:
        pass
    dummy_obj = Dummy()
    with pytest.raises(AttributeError):
        demo.access_attribute(dummy_obj)

def test_check_positive():
    demo = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-5)