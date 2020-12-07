import gym
import numpy as np
import matplotlib.pyplot as plt
import random

env = gym.make('FrozenLake-v0')
env.reset()


#QUESTION 2
sq2 = 0
fq2 = 0
actions = [1,1,2,2,1,2]
for _ in range(1000):
	env.reset()
	for a in actions:
		s, r, d, i = env.step(a)
		
	if r == 1:
		sq2 += 1
	else:
		fq2 +=1

sq2 = sq2*100/1000
fq2 = fq2*100/1000
	
print ("Success Q2:",sq2, "%")
print ("Fails Q2:", fq2, "%")
	
		
##QUESTION 3
sq3 = 0
fq3 = 0
def F(state):
	action = 0
	if state == 0:
		action = 2
	elif state == 1:
		action = 2
	elif state == 2:
		action = 1
	elif state == 3:
		action = 0
	elif state == 4:
		action = 1
	elif state == 6:
		action = 1	
	elif state == 8:
		action = 2	
	elif state == 9:
		action = 2
	elif state == 10:
		action = 1
	elif state == 13:
		action = 2
	elif state == 14:
		action = 2
	else:
		print("Not a valid state")
	return action
	
for _ in range(1000):
	s = env.reset()
	d = False
	while not d:
		s, r, d, i = env.step(F(s))
	if r == 1:
		sq3 += 1
	else:
		fq3 += 1

		
sq3 = sq3*100/1000
fq3 = fq3*100/1000
	
print ("Success Q3:",sq3, "%")
print ("Fails Q3:", fq3, "%")

#BAR GRAPH
n_groups = 2                   #data to plot
success = [sq2, sq3]
fail = [fq2, fq3]

fig, ax = plt.subplots()       #plot creation
index = np.arange(n_groups)
bar_width = 0.35


rects1 = plt.bar(index, success, bar_width, 
color = 'r', 
label = 'success')

rects2 = plt.bar(index + bar_width, fail, bar_width,
color = 'b',
label = 'fails')

plt.xlabel('Type of Inspection')
plt.ylabel('Rate in %')
plt.title('Frozen Lake Inspection Results')
plt.xticks(index + bar_width, ('Manual', 'Function'))

plt.legend()

plt.tight_layout()
#plt.show()


#QUESTION 4
sq4 = 0  
fq4 = 0

def H(state):
	actions = []
	if state == 0:
		actions = [1,1,2,1,2,2]
	elif state == 1:
		actions = [2,1,1,1,2]
	elif state == 2:
		actions = [1,1,1,2]
	elif state == 3:
		actions = [0,1,1,1,2]
	elif state == 4:
		actions = [1,2,2,1,2]
	elif state == 6:
		actions = [1,1,2]
	elif state == 8:
		actions = [2,1,2,2]			
	elif state == 9:
		actions = [2,1,2]
	elif state == 10:
		actions = [1,2]
	elif state == 13:
		actions = [2,2]
	elif state == 14:
		actions = [2]
	else:
		print("Not a valid state")
	return actions
	
for _ in range(1000):
	s = env.reset()
	d = False
	while not d:
		actions = H(s)
		for a in actions:
			s, r, d, i = env.step(a)
			if d:
				break
	if r == 1:
		sq4 += 1
	else:
		fq4 += 1
	
sq4 = sq4*100/1000
fq4 = fq4*100/1000
	
print ("Success Q4:",sq4, "%")
print ("Fails Q4:", fq4, "%")

#Question 5
def getPiecewise(state, alpha):
	p = random.uniform(0,1)
	if p >= alpha:
		return [F(state)]
	else:
		return H(state)


alphas = np.arange(0., 1.1, 0.1)
#print(alpha)

i = 0
successes = []
for alpha in alphas:
	successes.append(0)
	for _ in range(1000):
		s = env.reset()
		d = False
		while not d:
			actions = getPiecewise(s, alpha)
			for a in actions:
				s, r, d, _ = env.step(a)
				if d:
					break
			if r == 1:
				successes[i] = successes[i] + 1
	i += 1
print(successes)





































