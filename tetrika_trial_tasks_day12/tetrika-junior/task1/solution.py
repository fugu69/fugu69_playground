"""
Необходимо реализовать декоратор @strict
Декоратор проверяет соответствие типов переданных в вызов функции аргументов типам аргументов, объявленным в прототипе функции.
(подсказка: аннотации типов аргументов можно получить из атрибута объекта функции func.__annotations__ или с помощью модуля inspect)
При несоответствии типов бросать исключение TypeError
Гарантируется, что параметры в декорируемых функциях будут следующих типов: bool, int, float, str
Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию

Нобходимо написать тесты
"""
import inspect

def strict(func):
    def wrapper(*args, **kwargs):

        # Get parameters from prototype; func(*a*:int)
        # Returns list of keys name like [a, b, c]
        func_params = list(inspect.signature(func).parameters)

        # Get annotations of expected types from prototype; func(a: *int*)
        # Returns dict like {"a": <class int>, "b": <class str>}
        annotations = func.__annotations__ 

        for index, value in enumerate(args):
            # Get parameter name by index from func_parameters list [a, b, c]
            # Return value is a string
            param_name = func_params[index]

            # Get expected type of param_name from annotations dict by key param_name
            # Return value is a class object
            expected_type = annotations.get(param_name)

            # Check expected type against value type of passed argument
            # __name__ provides clean type name insted of <class name>
            if expected_type is not None and not isinstance(value, expected_type):
                raise TypeError(
                    f"Argument '{param_name}' must be {expected_type.__name__}, "
                    f"not {type(value).__name__}"
                )
            
        return func(*args, **kwargs)
    return wrapper