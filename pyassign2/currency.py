"""
Python作业 Assign2 (Nov/20/2018)
Author: 黄新迪 1700094621 元培学院

This module provides a function as a simple currency exchange calculator 
using an online currency service. The module contains a main currency exchange 
function, and a few functions to check the exchange function.
"""

from urllib.request import urlopen

def exchange(currency_from,currency_to,amount_from):
    """
    The function receives three input and returns a float output, 
    acting as a currency exchange calculator. 
        currency_from: initial currency
        currency_to: output currency
        amount_from: initial amount in initial currency
        output: amount of exchanged output currency
    """
    
    url_full = "http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=" \
    + str(currency_from).upper() + "&to=" + str(currency_to).upper() \
    + "&amt=" + str(amount_from)
    
    doc = urlopen(url_full)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
        
    if "true" in jstr:
        jstr_edit = jstr.replace("true","True")
    elif "false" in jstr:
        jstr_edit = jstr.replace("false","False")
    output_dict = eval(jstr_edit)

    if output_dict["success"] == True:    
        output = output_dict["to"].split()
        return float(output[0])
    elif output_dict["error"] == "Exchange currency code is invalid.":
        return "Exchange currency code is invalid."
    elif output_dict["error"] == "Source currency code is invalid.":
        return "Source currency code is invalid."
    elif output_dict["error"] == "Currency amount is invalid.":
        return "Currency amount is invalid."  

def test_run():
    """
    The function checks if the result of a correctly input exchange function
    gives an output as expected.
    """
    assert exchange("USD","EUR",2.5) == 2.1589225
    assert exchange("MYR","CNY",20000.58) == 33094.538750002

def test_currency():
    """
    The function checks if the result of a wrong currency input in the exchange
    function gives an output as expected.
    """
    assert exchange("USD","XXX",2.5) == "Exchange currency code is invalid."
    assert exchange(5000,"LYD",5000) == "Source currency code is invalid."

def test_inputamt():
    """
    The function checks if the result of a wrong amount input in the exchange
    function gives an output as expected.
    """
    assert exchange("AOA","LYD",True) == "Currency amount is invalid."
    assert exchange("AOA","CNY","hello") == "Currency amount is invalid."

def testAll():
    """
    The function test all cases for possible error.
    """
    test_run()
    test_currency()
    test_inputamt()
    print("All test passed.")

def main():
    currency_from = input("Convert from currency: ")
    amount_from = input("Convert amount: ")
    currency_to = input("Convert to currency: ")
    
    print(exchange(currency_from,currency_to,amount_from))
    
if __name__ == "__main__":
    main()
