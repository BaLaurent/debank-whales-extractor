import requests
import json
import os

if __name__ == "__main__":
	currCount = 0
	maxCount = 17115
	arrWhales = list()
	arrAddresses = list()
	while currCount < maxCount:
		currLimit = currCount+100
		if(currLimit > maxCount):
			currLimit = maxCount
		url = f"https://api.debank.com/whale/list?start={currCount}&limit={currLimit}&order_by=-usd_value"
		r = requests.get(url)
		response = r.json()["data"]["whales"]
		for whale in response :
			os.system("clear")
			print(f"{currCount} / {maxCount}")
			print(f"Checking address {whale['id']}")
			try:
				#check if multisig
				multisig = whale["desc"]["contract"]["op"]["multisig"]
				print("Multisig address, skiping")
			except:
				arrWhales.append(whale["desc"])
				arrAddresses.append(whale["id"])
		currCount = currLimit
	with open("whalesFull.json","w+") as f:
		json.dump(arrWhales,f,indent=4)
	with open("whalesAddr.json","w+") as f:
		json.dump(arrAddresses,f,indent=4)
