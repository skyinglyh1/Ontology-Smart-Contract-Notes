from boa.interop.System.Runtime import *
from boa.interop.System.Storage import *
def Revert():
    """
    Revert the transaction. The opcodes of this function is `09f7f6f5f4f3f2f1f000f0`,
    but it will be changed to `ffffffffffffffffffffff` since opcode THROW doesn't
    work, so, revert by calling unused opcode.
    """
    raise Exception(0xF1F2F3F4F5F6F7F8)

def Require(condition):
	"""
	If condition is not satisfied, return false
	:param condition: required condition
	:return: True or false
	"""
	if not condition:
		tt = Revert()
	return True

def RequireScriptHash(key):
    """
    Checks the bytearray parameter is script hash or not. Script Hash
    length should be equal to 20.
    :param key: bytearray parameter to check script hash format.
    :return: True if script hash or revert the transaction.
    """
    tt = Require(len(key) == 20)
    return True


def RequireWitness(witness):
	"""
	Checks the transaction sender is equal to the witness. If not
	satisfying, revert the transaction.
	:param witness: required transaction sender
	:return: True if transaction sender or revert the transaction.
	"""
	tt = Require(CheckWitness(witness))
	return True

def Add(a, b):
	"""
	Adds two numbers, throws on overflow.
	"""
	c = a + b
	tt = Require(c >= a)
	return c

def Sub(a, b):
	"""
	Substracts two numbers, throws on overflow (i.e. if subtrahend is greater than minuend).
    :param a: operand a
    :param b: operand b
    :return: a - b if a - b > 0 or revert the transaction.
	"""
	tt = Require(a>=b)
	return a-b

def Mul(a, b):
	"""
	Multiplies two numbers, throws on overflow.
    :param a: operand a
    :param b: operand b
    :return: a - b if a - b > 0 or revert the transaction.
	"""
	if a == 0:
		return 0
	c = a * b
	tt = Require(c / a == b)
	return c

def Div(a, b):
	"""
	Integer division of two numbers, truncating the quotient.
	"""
	tt = Require(b > 0)
	c = a / b
	return c


KEY = "storage"

def Main(operation, args):
    if operation == "calculate1":
        return calculate1()

    return False

def calculate1():
    a = 1
    b = 2
    c = 3
    d = 4

    tmp1 = Div(d, c)
    tmp2 = Mul(b, tmp1)
    tmp3 = Sub(tmp2, b)
    tmp4 = Add(a, tmp3)
    Notify(["111 res is ", tmp4])

    # a + b * d /c - b, res1 is right
    res1 = Add(a,Sub(Mul(b, Div(d, c)),b))
    Notify(["111 res1 is", res1])
    Put(GetContext(), KEY, Add(a,Sub(Mul(b, Div(d, c)),b)))
    res2 = Get(GetContext(), KEY)
    Notify(["222 res2 is", res2])
    return True