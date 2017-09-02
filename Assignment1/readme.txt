Assignment 1 solution 
	- See 'Assignment 1 answers.txt' in this submission for the decrypted text.
	- To see output of both solutions, run Assignment1.py. The decrypted messages will output to console. The keys are included in the files.

Here's how I solved it:

Problem 1 - Substitution cipher
	- Tried to decode use Shift method. Tried all 25 shifts (ShiftMethod.py). Didn't work.
	- Wrote SubstitutionMethod.py to apply the statistical methods we reviewed for monoalphabetic subsitution encryption.
	- Created spreadsheet (worbook.xlsx) of single letter, bigram, and trigram distributions. Aligned letters based on english frequency.
	- Tried a couple of different dictionaries. Rinse and repeat.
	- Realized putting an underscore character for letters not mapped dictionary made the output easier to read.
	- Realized that first couple of words should have a vowel.
	- Was able to crack it from there.

Problem 2 - Vigenere cipher
	- Reviewed vigenere cipher in multiple books 

		Understanding Cryptography
		(https://www.amazon.com/Understanding-Cryptography-Textbook-Students-Practitioners/dp/3642041000/ref=sr_1_1?ie=UTF8&qid=1504360523&sr=8-1&keywords=understanding+cryptography)

		Hacking Secret Ciphers in Python
		https://www.amazon.com/s/ref=nb_sb_ss_c_1_14?url=search-alias%3Daps&field-keywords=hacking+secret+ciphers+with+python&sprefix=hacking+secret%2Caps%2C186&crid=25ANEP53X74QF&rh=i%3Aaps%2Ck%3Ahacking+secret+ciphers+with+python

	- Realized the keyword was probably an English word. Downloaded ~450,000 common english words.

		https://github.com/dwyl/english-words (words.txt)

	- Since we had the keyword length of 5, pulled in list of words with length of 5. Filtered out an words that contained numbers or punctuation.

	- Did brute force attack using all list of words. Wrote output of keyword and decrypted text (about 11,000 lines) to file.
	
	- After reviewing file realized the first 5 letter of decrypted text needed to include a vowel (a,e,i,o,u,y)

	- Did another brute force filtering out decrpyption where first 5 letters did not contain vowel. Only outputted first 20 or so characters to make it easier to review.

	- After a quick review saw the keyword was 'goofy'

	- Ran decryption for keyword 'goofy' and reviewed output to verify it was correct. 
