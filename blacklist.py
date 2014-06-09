
class BlackList:


	"""  A class to be used to search Hyperion Gray's Punk Spider Blacklist of websites which contained
		 vulnerabilities. You can pass it in another list of hosts to see if any are found in the blacklist. """

	def __init__(self):

		##Attributes 

		self.blackListFile = "blacklist.list"


	def searchBlackList(self, query):

		foundList = []

		try:
			with open(self.blackListFile, mode="r", encoding="utf-8") as myFile:

				for line in myFile:
					if query in line:
						foundList.append(line)
		except:

			return False


		return foundList


	def showResults(self, foundList):

		for i in range(len(foundList)):
			print("{0}. {1}".format(i + 1, foundList[i]))


if __name__ == "__main__":

	bl = BlackList()

	foundList = bl.searchBlackList(".co.uk")

	showResults(foundList)






