import sys
from math import ceil, log, sqrt
from random import randint, random, sample
from multiprocessing import Pool
from cqc.pythonLib import CQCConnection, qubit
#from teleportation import accept_teleportation
from time import sleep

correct_basis = []
correct_key = []
bits_alice = []
basis_alice = []
bits_bob = []
basis_bob = [] 
received = []
wait = 1
subset = []
a=[]
newkey = []
newkeybasis = []

def preparation_Bob():
	with CQCConnection("Bob") as Bob:
		for i in range(20):
            
			q = Bob.recvQubit()
			random_basis_bob = randint(0,1)
			basis_bob.append(random_basis_bob)
            
			if random_basis_bob == 1:
				q.H()
               
			m = q.measure()
			received.append(m)
            
		r = Bob.recvClassical()
		basis_alice[:] = list(r)
        
		print ("basis of bob ", basis_bob)
		print ("measurement results of bob: ",received)
		print ("received basis by bob ",basis_alice)
		print ("Sending Bob basis to Alice.... ")
		Bob.sendClassical("Alice", basis_bob)
		print ("Sent basis to Alice")
		calculation_of_shiftKey()
		a = Bob.recvClassical()
		subset[:] = list(a)
		print ("received subset by bob ", subset)
		#newkey = list(set(correct_key) - set(subset))
		if all(i in correct_basis for i in subset):
			newkeybasis=[x for x in correct_basis if x not in subset]
			#newkey=removeSublistFromList(subset,correct_key)
			print("new key gen basis= ",newkeybasis)
			
			for i in range(len(newkeybasis)):
				#d = newkeybasis[i]
				#c = received[d]
				newkey.append(received[newkeybasis[i]])
			
			print("new key gen= ",newkey)
			
		else:
			print("wrong key recieved may be eve presence")
		
		#print("new key gen= ",newkey)
		#Bob.closeClassicalChannel("Alice")
    		#closeClassicalServer()

		
    
    
def calculation_of_shiftKey(): 
	error = 0
	for i in range(len(received)):
		if (basis_alice[i] == basis_bob[i]):
			correct_basis.append(i)
			correct_key.append(received[i])
		else:
			error = error + 1  
	print ("Correct Basis: ", correct_basis)        
	print ("Correct Key :", correct_key)
	print ("error:", error)
	error_percentage = error/len(received) # maximum value is 1
	print("error_percentage", error_percentage)
	size = ceil(sqrt(len(correct_basis)))
	print ("size: ", size) 
	global qber
	#global qber2
	qber = error_percentage/size # lies btween 0 and 1
	print("qber:", qber)
	
	

	
def key_generation():
	with CQCConnection("Bob") as Bob:
		#startClassicalServer()
		Bob.openClassicalChannel("Alice")
		a = Bob.recvClassical()
		H[:] = list(a)
		print ("received subset by bob ", H)
		sleep(wait)
		#Bob.closeClassicalChannel("Alice")
    		#closeClassicalServer()
    		
    		
    		
# Returns that starting and ending point (index) of the sublist, if it exists, otherwise 'None'.
def findSublist(subList, inList):
    subListLength = len(subList)
    for i in range(len(inList)-subListLength):
        if subList == inList[i:i+subListLength]:
            return (i, i+subListLength)
    return None




# Removes the sublist, if it exists and returns a new list, otherwise returns the old list.
def removeSublistFromList(subList, inList):
    indices = findSublist(subList, inList)
    if not indices is None:
        return inList[0:indices[0]] + inList[indices[1]:]
    else:
        return inList
        
        


    

if __name__ == "__main__":

    preparation_Bob()  
    #calculation_of_shiftKey()
    #key_generation()
    
