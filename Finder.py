
class ManageData:
	def openData(data):
		dados = open(data, "r", -1, "UTF-8") # Abri o arquivo no enconding UTF-8
		print(dados.readline())
	def organizer():
		print("Organiza os dados")

class FindingTools:
	def Searcher():
		print("Procura")

ManageData.openData("Data.txt")