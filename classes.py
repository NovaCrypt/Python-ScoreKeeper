# PARENT CLASSES
class User:
	def __init__(self, username, score) -> None:
		self.name = username
		self.score = score

	def __str__(self):
		return f"{self.name}: {self.score} points"
