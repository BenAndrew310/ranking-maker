import os
import re
import sys
import platform

class Ranker:
	def __init__(self, title, description='', *items):
		self.title = title
		self.description = description
		self.ranking = []
		for item in items:
			self.add_item(item)

	def add_item(self, item):
		if item not in self.ranking:
			self.ranking.append(item)

	def export(self, dst):
		with open(dst, 'w') as file:
			file.writelines( self.get_ranking_text() )

	def get_ranking_text(self):
		r = ""
		for ind, item in enumerate(self.ranking):
			r += f"({ind+1}) {item}\n"
		return r

	def place(self, rank1, rank2):
		item = self.ranking[rank1-1]
		del self.ranking[rank1-1]
		assert rank2 >=1 and rank2 <= len(self.ranking)+1

		self.ranking.insert(rank2-1, item)

	def substitute(self, rank1, rank2):
		self.ranking[rank1-1], self.ranking[rank2-1] = self.ranking[rank2-1], self.ranking[rank1-1]

if __name__ == "__main__":
	ranker = Ranker("Anime", "", "Frieren", "Demon Slayer", "Mushoku Tensei", "OPM", "JJK", "86", "Hell's Paradise", "Mob Psycho")
	system = platform.system()

	while True:
		print(f"Ranking:\n{ranker.get_ranking_text()}\n")
		command = input(":")
		if command.lower() in ['quit', 'q']:
			break
		command = command.split(" ")
		a, b = int(command[1]), int(command[2])
		if command[0].lower() == "place":
			ranker.place(a, b)
		elif command[0].lower() == "sub":
			ranker.substitute(a, b)

		if system == "Windows":
			os.system('cls')
		elif system == "Linux" or system == "Darwin":
			os.system("clear")