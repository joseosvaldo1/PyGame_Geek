from Models.calculate import Calculate


def main() -> None:
	points: int = 0
	play(points)


def play(points: int) -> None:
	mesage_1 = "Enter your desired difficulty level [1, 2, 3, 4]: "
	difficulty: int = int(input(mesage_1))
	
	calc: Calculate = Calculate(difficulty)
	
	mesage_2 = "Enter the result for the following operation: "
	calc.show_operation()
	
	user_result: int = int(input())

	if calc.check_result(user_result):
		points += 1
	
	print(f"You have {points} point(s)!")
	
	mesage_3 = "Do you want to continue playing? [1 - yes / 0 - no]: "
	continuation: int = int(input(mesage_3))
	
	if continuation:
		play(points)
	else:
		print(f"You finished with {points} point(s)! Until next time!")
	
	
if __name__ == '__main__':
	main()