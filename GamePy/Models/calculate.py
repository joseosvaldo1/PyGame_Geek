from random import randint


class Calculate:
	def __init__(self: object, dificulty: int) -> None:
		self.__dificulty: int = dificulty
		self.__value1: float = self._generate_value
		self.__value2: float = self._generate_value
		self.__operation: int = randint(1, 3)
		# Operations: 1 - addition, 2 - subtraction
		# 3 - multiplication.
		self.__result: float = self._generate_result
	
	