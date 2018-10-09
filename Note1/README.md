
### The defined methods need to return something.
In test1.py, there is no return within the methods that we define. When we compile the contract, there may be a potential bug within neo-boa compiler. We may not notice that, yet it may appear when some methods are actually invoked.
### Compare test1.py and test2.py within compare contracts dictionary.
After we compile and deploy the contracts, we can find that "calculate1" method can not be executed in test1.py, yet can be executed and get the correct result in test2.py
