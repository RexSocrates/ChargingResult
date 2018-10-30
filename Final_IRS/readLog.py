import csv

nameListFile = open('nameList.txt')
lines = nameListFile.readlines()

logFileList = []
for line in lines :
	logFile = line.replace('\n', '')
	logFileList.append(logFile)

interactionDic = dict()
signalsDic = dict()
rateDic = dict()

for i in range(0, len(logFileList)) :
	logFileName = logFileList[i]
	file = open(logFileName)
	lines = file.readlines()

	for line in lines :
		dataArr = line.split(',')
		interaction = float(dataArr[0])
		signals = float(dataArr[1])
		rate = float(dataArr[2])

		interactionDic[str(i + 2)] = interaction
		signalsDic[str(i + 2)] = signals
		rateDic[str(i + 2)] = rate


	


with open('numOfDevicesLog.csv', 'w') as csvfile :
	fields = ['Number of devices', 'Interaction', 'Signals', 'Successful rate']
	
	writer = csv.DictWriter(csvfile, fieldnames=fields)
	writer.writeheader()

	for numOfDevices in range(2, 8) :
		interaction = interactionDic[str(numOfDevices)]
		signals = signalsDic[str(numOfDevices)]
		rate = rateDic[str(numOfDevices)]
		writer.writerow({'Number of devices': str(numOfDevices), 'Interaction' : str(interaction), 'Signals' : str(signals), 'Successful rate' : str(rate)})
