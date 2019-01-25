This assignment is from http://www.cs.cornell.edu/courses/cs1110/2016fa/assignments/assignment1/index.php#service.

http://cs1110.cs.cornell.edu/2016fa/a1server.php? provides a function to calculate exchange rate at a fixed rate, users will need to provide the parameters: *from=source&to=target&amt=amount* when using.

*source*, *target* are currencies represented by three alphabets, while *amt* is the value of the currency to be exchanged, 

for example, *from=USD&to=EUR&amt=2.5* means exchanging 2.5 USD to EUR.

The complet URL request is: http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5

The result of the URL will be something like: { "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }

The main purpose of this assignment is to analyze the result of the URL, and retrive the necessary information from it.

The function you need to realize looks something like this:
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

**How to visit a URL in Python3**
```
from urllib.request import urlopen

doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')
docstr = doc.read()
doc.close()
jstr = docstr.decode('ascii')
```
doc.read() returns a string, b'{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }' can be retrive as string with the decode function.


**Iterative Development Process**

We recommend using an iterative approach to complete the assignment, the exact process could be referenced from http://www.cs.cornell.edu/courses/cs1110/2016fa/assignments/assignment1/index.php#iterative

For each function developed, a test function should be provided, the assert function could be used for this.
```
def test_get_from()
    assert('USD' == get_from(json))
```
You need to write a testAll function, and test all your functions.
```
def testAll()
    """test all cases"""
    test_get_from()
    test_B()
    test_C()
    print("All tests passed")
```
Note: All the functions and test functions are in the same currency.py documents, unlike the request in http://www.cs.cornell.edu/courses/cs1110/2016fa/assignments/assignment1/index.php, there is no need to develop another documents for the test functions.
