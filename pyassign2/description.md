This assignment is from http://www.cs.cornell.edu/courses/cs1110/2016fa/assignments/assignment1/index.php#service.

http://cs1110.cs.cornell.edu/2016fa/a1server.php? provides a function to calculate exchange rate at a fixed rate, users will need to provide the parameters: *from=source&to=target&amt=amount* when using.

*source*, *target* are currencies represented by three alphabets, while *amt* is the value of the currency to be exchanged, 

for example, *from=USD&to=EUR&amt=2.5* means exchanging 2.5 USD to EUR.

The complet URL request is: http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5

在浏览器中输入该地址，得到的结果类似为：{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }

本次作业的主要目标，就是分析得到的字符串，从里面获取需要的结果。

你需要实现的函数:
```
def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
```

如何在Python3中访问URL
```
from urllib.request import urlopen

doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')
docstr = doc.read()
doc.close()
jstr = docstr.decode('ascii')
doc.read() 返回的是字节流, 如: b'{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }' 可以调用 decode方法得到正常的字符串.
```

迭代开发过程

本次作业建议采取迭代开发方法，从基本功能开始，逐渐完成最终功能，具体可参考：http://www.cs.cornell.edu/courses/cs1110/2016fa/assignments/assignment1/index.php#iterative

对于迭代开发中实现的每一个函数，需要提供一个测试函数，测试其是否正确，可以用Python语言的assert函数编写测试代码.
```
def test_get_from()
    assert('USD' == get_from(json))
```
你需要写一个 testAll 函数, 里面测试所有你编写的测试函数
```
def testAll()
    """test all cases"""
    test_get_from()
    test_B()
    test_C()
    print("All tests passed")
```
注意: 所有的测试函数和被测函数都在同一个文件 currency.py 中，不需要单独建立测试文件，这和http://www.cs.cornell.edu/courses/cs1110/2016fa/assignments/assignment1/index.php要求不同。