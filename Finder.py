class Find:
	def ManageData(data):
		dados = open(data, "r", -1, "UTF-8") # Abri o arquivo no enconding UTF-8
		print(dados.readline())

Find.ManageData("Data.txt")