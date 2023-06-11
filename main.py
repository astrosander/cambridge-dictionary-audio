import Parser
import os, time

def Start():
	word = input('Enter the word you wish to load here:')

	save_path = f"{word}.mp3" #Generating of file name

	print("Downloading..")
	Parser.define(word, save_path)

	try:
		os.startfile(save_path)
		time.sleep(2)

	except:
		print("Such word wasn't found")

	
	os.system('cls')
	Start()

Start()

