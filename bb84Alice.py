    
import sys
from math import ceil, log, sqrt
from random import randint, random, sample
from multiprocessing import pool
from cqc.pythonLib import CQCConnection, qubit
#from teleportation import send_teleportation
from time import sleep
import random 

bits_alice = []
basis_alice = []
test = []
#mesaj = []
wait = 1
basis_bob = [] 
received = []
correct_basis = []
correct_key = []
sample = []
#L = []
subset = []
H = []
def preperation_Alice():
	with CQCConnection("Alice") as Alice:
		for i in range(20):
			random_bits_alice = randint(0,1)
			random_basis_alice = randint(0,1)
			bits_alice.append(random_bits_alice)
			basis_alice.append(random_basis_alice)
            
			q = qubit(Alice)
			if random_bits_alice == 1:
				q.X()
         
			if random_basis_alice == 1:    
				q.H()
			#Alice.sendQubit(q, "Bob")
			Alice.sendQubit(q,"Bob")
            
			#send_teleportation(q,location,'Bob')
			
			#q.measure(inplace=False)
			#test.append(random_bits_alice)
		print("sended basis by alice",basis_alice)
		print ("bits of alice:", bits_alice)
		print ("#####################################################################")
		#sleep(wait)
		print ("Sending Alice basis to Bob.... ")
		Alice.sendClassical("Bob", basis_alice)
		print ("Sent basis to Bob")
		#sleep(wait)
		R = Alice.recvClassical()
		basis_bob[:] = list(R)
		print ("received basis by Alice from bob ",basis_bob)
		calculation_of_shiftKey()
		#random_sublist(correct_key)
		#left = randint(0, len(correct_key) - 1)
		#right = randint(left + 1, len(correct_key))
		#subset = correct_key[left:right]
		#print("sublist ", subset)
		
		#H = sample(correct_basis,4)
		#print(random.sample(correct_basis,5))
		subset = random.sample(correct_basis , 5)
		
		print("With sublist:", subset)
		#H = subset
		print("sending...")
		Alice.sendClassical("Bob", subset)
		print("sent")
		
		
		
		#Alice.closeClassicalChannel("Bob")
		
		
		
		
def calculation_of_shiftKey(): 
	error = 0
	received=bits_alice
	for i in range(len(received)):
		if (basis_alice[i] == basis_bob[i]):
			correct_basis.append(i)
			correct_key.append(received[i])
		else:
			error = error + 1  
	print ("Correct Basis: ", correct_basis)        
	print ("Correct Key :", correct_key) 
	print ("error:", error)
	#print(sample(correct_key,5))
	#H = random.sample(correct_key,size)
	#print(random.sample(correct_key,5))
	error_percentage = error/len(received) # maximum value is 1
	print("error_percentage", error_percentage)
	size = ceil(sqrt(len(correct_basis)))
	print ("size: ", size) 
	global qber
	#global qber2
	#qber = error_percentage/size # lies btween 0 and 1
	#print("qber:", qber)
	
def random_sublist(L):
	left = randint(0, len(L) - 1)
	right = randint(left + 1, len(L))
	subset = L[left:right]
	print("sublist ", subset)
	return subset
	
def shiftkeysending():
	with CQCConnection("Alice") as Alice:	
		Alice.openClassicalChannel("Bob")
		H = subset
		print("sending...")
		Alice.sendClassical("Bob", H)
		print("sent")
		sleep(wait)
		#Alice.closeClassicalChannel("Bob")
		
def keygenration():
	
       

if __name__ == "__main__":

	preperation_Alice()
	#calculation_of_shiftKey()
	#keygenration()
