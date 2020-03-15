import random,json,time
def main():
	
	with open("virus.txt",'r') as file:
		data1 = json.load(file)
		file.close()
	with open("napas.txt",'r') as file:
			data2 = json.load(file)
			file.close()
	while 1==1:
		print("update")
		m = random.randint(1,5)
		with open("bot{}.txt".format(m),'r') as file:
			data = json.load(file)
			file.close()
		i = 1
		unvirus = list(data1.keys())
		while i <= int(data["lvl"])*9:
			data["port{}".format(i)] = []
			data["port{}".format(i)].append(unvirus[random.randint(0,len(unvirus)-1)])
			i+=1
		with open("bot{}.txt".format(m),'w') as file:
			data = json.dump(data,file)
			file.close()

		login = data2["name"][random.randint(0,len(list(data2["name"]))-1)]
		with open("{}.txt".format(login),'r') as file:
			data3 = json.load(file)
			file.close()
		virus = "Tor"
		#virus = list(data1[list(data1.keys())[random.randint(0,len(list(data1.keys()))-1)]])[0]
		#virus = list(data1[virus])[random.randint(0,len(list(data1[virus]))-1)]
		with open("{}.txt".format(login),'r' ) as file:
			data4 = json.load(file)
			file.close()
		i=0
		k=0
		n=0
		r=0
		port = "port{}".format(random.randint(1,int(data4["lvl"])*9))
		print(login,"Yes",port,virus)
		if data4[port] == []:
			data4[port].append("1")	
		if data4[port][0] == "Error":
			pass
		else:
			virs=list(data1.keys())
			unvirs=[]
			while i < len(list(data1.keys())):
				if str(virus) in data1[virs[i]] :
					unvirs.append(virs[i])
				i+=1
			if unvirs == [] or virus == "" :
				pass
			else:
				virs1 = list(data4[port])
				for n in range(0,len(virs1)):
					for k in range(0,len(unvirs)):
						if str(unvirs[k]) == str(virs1[n]):						
							r = 1
				if r == 1:
					pass
				else:
					print(login,"Yes",port,virus)
					data4[port] = ['Error' , "bot{}".format(m)]
					with open("{}.txt".format(login),'w') as file:
						data4 = json.dump(data4,file)
						file.close()
		time.sleep(0.1)

if __name__ == "__main__":
			main()
	