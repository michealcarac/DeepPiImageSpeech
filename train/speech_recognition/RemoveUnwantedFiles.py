#Small script to reconstruct the dataset in the following order:
#Say we want 3 wake words, and each word has roughly 2000 wav files. Now the rest of the dataset is say 50000 files. Would it be fair to train something like 'other'
#on these 50000 files? No, it would not, so this program makes sure all of the other words only have roughly 2000 wav files TOTAL, so that every single word trained for 
#including 'other' has roughly the same amount of wav files. This program will not just delete every other word and leave 2000 of one word, it keeps an equal amount of 
#each word. 
#Also, make sure it is just folders with data in your dataset, no misc files like txt files or anything.
import shutil
import os
from random import sample
from math import ceil

#WARNING:
#This is irreversible, so make sure to have a backup beforehand, it may dump in your trash though. 
#ESTABLISH what words you do not want
dataset_path ='/home/spixy/Downloads/Dataset_1/' #If on windows, still use '/' for directories 
words =  ['bed','bird','cat','dog','down','eight','five','four','go','happy','house','left','marvin','nine','one','right','seven','six','three','tree','two','up','wow','zero','_background_noise_'] 
#Example: ['sheila','bed']

#DO NOT TOUCH BELOW UNLESS COMFORTABLE
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#to delete unwanted files
def deletefiles():
	print('\033[91m', 'Do you want to delete ',count-count3*len(sortedwords),' WAV files from ', len(sortedwords),' folders? (Y/N)') 
	userin = input('Please enter (Y/N): ') #User input is dangerous, but we aren't really worried about security. Never trust user input. 
	print('\033[0m','You entered', userin)
	if  userin.lower() == 'y':
		print('\033[91m', 'Deleting ',count-count3*len(sortedwords),' WAV files from ', len(sortedwords),' folders.....') 
		for folder in words:
			lendatafolder = len(os.listdir(dataset_path +folder) )
			if lendatafolder <= count3:
				pass
			else:
				for file in sample(os.listdir(dataset_path+folder),lendatafolder- count3):
					os.remove(dataset_path+folder+'/'+file) #Comment out if you don't want to remove while testing
					print(dataset_path + folder+'/' +file) 	
		print('\033[0m')
	else:
		print('Cancelling...')


count = 0 #count of words not wanted total wav files
count2 = 0 #count of words wanted total wav files
i = 0 #index
j = 0 #index
wws = [] #Wanted wake words, leave blank, program will satisfy
sortedwords = sorted(words)  #We sort the words to recursively search through 
sorteddata = sorted(os.listdir(dataset_path))

while j < len(os.listdir(dataset_path)): #Algorithm to find the displayed info 
	if sortedwords[i] == sorteddata[j]:
		i +=1
		count += len(os.listdir(dataset_path+sorteddata[j]))
	elif sortedwords[i] != sorteddata[j]:
		wws.append(sorteddata[j])
		count2 += len(os.listdir(dataset_path+sorteddata[j]))
	j+=1

#Displays some info
print('\033[1m','Not wanted words:','\033[0m','\033[96m', '\n',sortedwords, '\n','\033[0m')
print('\033[1m','Wanted words:','\033[0m','\033[96m', '\n',wws, '\n','\033[0m')
print('\033[1m','# of files we dont want:','\033[0m','\033[92m',count,'\033[0m')
print('\033[1m','# of files we want:','\033[0m','\033[92m',count2,'\033[0m')
print('\033[1m','# of words we dont want:','\033[0m','\033[92m',len(sortedwords),'\033[0m','\033[1m','(not including other)', '\033[0m')
print('\033[1m','# of words we want:','\033[0m','\033[92m',len(wws),'\033[0m','\033[1m','(not including other)', '\033[0m')
print('\033[1m','# average of files in words wanted:','\033[0m','\033[92m',ceil(count2/len(wws)),'\033[0m')
count3 = ceil((count2/len(wws))/len(sortedwords)) #Gets how many files we want in each "not wanted" folder 
print('\033[1m','# of files in each word not wanted folder after:','\033[0m','\033[92m',count3,'\033[0m')
print('\033[1m','# math:','\033[0m','\033[92m',count3, '*' ,len(sortedwords),'=',count3*len(sortedwords),'\033[0m','\033[1m','(roughly same as avg per word wanted)', '\033[0m')

if count3 > 1: #This will happen unless 1. # of files we dont want is smaller than files we do or 2. This program is being run a second time <- don't run it 2nd time
	for folder in words:
		lensorted = len(os.listdir(dataset_path + folder))
	if lensorted >= count3: #This makes sure none of the folders have less than count3, so we dont have indexxing issues 
		deletefiles()
	else:
		print('\033[91m','Error: One folder has less than or equal to', count3,'files',)
		userin = input('Continue anyways and ignore that folder? (Y/N):')
		print('\033[0m','You entered',userin)
		if  userin.lower() == 'y':
			deletefiles()
		else:
			print('Cancelling...')
	
else:
	print('\033[91m','Error: Program has already deleted files','\033[0m')

	
# Following code is specific for the google dataset if you want to change the testing_list.txt and validation_list.txt  for the wav files, not actually needed. 
''' #Uncomment to use
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#to correct testing_list.txt
path = '/home/spixy/Downloads/Dataset_1/'  #If on windows, still use '/' for directories
f = open('testing_list.txt','r') #Change if different txt file
lst = []
for line in f:
	for word in words:
		if word in line:
			line = line.replace(line,'')
	lst.append(line)
f.close()
f = open('testing_list.txt','w')#Change if different txt file
for line in lst:
	f.write(line)
f.close()
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#to correct validation_list.txt
f = open('validation_list.txt','r')#Change if different txt file
lst = []
for line in f:
	for word in words:
		if word in line:
			line = line.replace(line,'')
	lst.append(line)
f.close()
f = open('validation_list.txt','w')#Change if different txt file
for line in lst:
	f.write(line)
f.close()
'''
