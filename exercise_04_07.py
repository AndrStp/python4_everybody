x=input('Enter score: ')
try:
    score=float(x)
except:
    print('Bad score')
    quit()
def computegrade (score):
    if score > 0 and score < 1:
	    if score >= .9:
		    print('A')
	    elif score >= .8:
		    print('B')
	    elif score >= .7:
		    print('C')
	    elif score >= .6:
		    print('D')
	    else:
		    print('F')
    else:
	    print('Bad score!')

computegrade(score)
