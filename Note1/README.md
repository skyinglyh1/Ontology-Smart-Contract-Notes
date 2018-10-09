
### The defined methods need to return something.
In test1.py, there is no return within the methods that we define. When we compile and deploy the contract, there is nothing wrong. Yet, there may be a potential problem that we may not notice, and it may appear when some methods are actually invoked.
### Compare test1.py and test2.py within compare contracts dictionary.
After we compile and deploy the contracts, we can find that "calculate1" method can not be executed in test1.py, yet can be executed and get the correct result in test2.py.

So, when we invoke the methods that we define within another method, there should exist something for the methods to return leftside. Otherwise, there might appear something unexpected when the methods within smart contract are executed.
