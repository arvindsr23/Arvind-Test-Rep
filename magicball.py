import random
theAnswers = ['A','B', 'C']
def checkstr(i):
	if i in range(len(theAnswers)):
		return theAnswers[i]+str(i)
	else:
		return 'Out of Range'+str(i)
		
def magicball():
	qstn = input("Ask me your question:  ")
	print ('The Question is %s:' % qstn)
	print ('The outlook looks %s:' % checkstr(random.randrange(0,10,1)))
	return












	

	
	
