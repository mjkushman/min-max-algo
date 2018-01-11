'''Scratch paper.

The goal of the algorithm is to identify the words that appear in people’s profiles that are most unique to them.

It would require some known inputs for comparison.
1. Two or more distinct group traits, such as male vs female, geo location, or age/age range.

2. Must have a body of text to analyze that all subjects have, such as profile description or even profile name.


I think it would essentially do this:
1. Find all words in all profiles.
2. For group A, rank the words by frequency. Do the same for Group B.
3. Each word has a ranking in its respective list. For instance for Group A, the word “pizza” might rank #10 out of a list of 10,000 (or more). For group B, the word “pizza” ranks at #56.

4. Find the word pairs that have the largest discrepancy in frequency, aka the widest gap in ranking. The result should be something like this:
- “gasoline” separated by 8000 spots, higher on group A.
- “ elephant” separated by 7678 spots, higher on group B.

5. Then assemble those words into lists, top X highest for each group.'''


#TODO: compile 2+ blocks of text, one for each group being compared
import os
groupA = {} #a dict of word, freq
textA = [] #a list of all the words in string A
groupB = {} #a dict of word, freq
textB = [] #a list of all the words in string B


import re
sReg = re.compile(r'\w+\'*\w*')

#Open the files and read the contents to variables



#Open file A and create a list of it's contents, then close file
textFileA = open('./textblockA.txt')
textContentA = textFileA.read()
textFileA.close()

textContentA = textContentA.lower()
textContentA = sReg.findall(textContentA)

#trying a faster version. It works!
for w in textContentA:
	if w in groupA.keys():
		groupA[w] += 1
	else:
		groupA[w] = 1


#for debug
#print(groupA)


#Open file B and create a list of it's contents, then close file

textFileB = open('./textblockB.txt')
textContentB = textFileB.read()
textFileB.close()

textContentB = textContentB.lower()
textContentB = sReg.findall(textContentB)

for w in textContentB:
	if w in groupB.keys():
		groupB[w] += 1
	else:
		groupB[w] = 1




#both files now closed
#At this point, there are two dictionaries that have the word as keys and frequency of word as values.


#TODO: iterate through all the words and sort by freuency
print('\n')

#This section adds each other's keys to the other's dict
for key in groupB:
	if key not in groupA:
		groupA[key] = 0

for key in groupA:
	if key not in groupB:
		groupB[key] = 0

#now they both have each other's words (keys)

#debug printing
#print('new g a', groupA)
#print('new g b', groupB)


#This little section prints out all the words in order of frequency in the dict. It's a lot of words.
'''
groupA_view = [ (v,k) for k,v in groupA.items() ]
groupA_view.sort(reverse=True) # natively sort tuples by first element
for v,k in groupA_view:
    print('%s: %d' % (k,v))
'''
#END OF printing out all words section




#TODO:  Create a new list that is a combination of both lists, but ordered by the difference in frequency between the two previous lists
#groupDiff is the absolute differences in all word frequencies, in a single dict
groupDiff = {}
for key in groupA:
	diff = 0
	diff = abs(groupA[key] - groupB[key])
	#print(key, diff) for debug, use this to print the key, and difference in occourences
	groupDiff[key] = diff

#debug printing. Prints the dictionary with the absolute value difference in frequency between keys of Group A and Group B
#This little section prints out all the words in order of frequency in the dict. It's a lot of words.
'''
groupDiff_view = [ (v,k) for k,v in groupDiff.items() ]
groupDiff_view.sort(reverse=True) # natively sort tuples by first element
for v,k in groupDiff_view:
    print('%s: %d' % (k,v))
'''
#END OF printing out all words section



#these lists re-sort the words to their original source. lists of touples - key, diff pair.
groupAPrime = [] #(key, diff)
groupBPrime = [] #(key, diff)

for key in groupDiff:
	if groupA[key] > groupB[key]:
		groupAPrime.append((key, groupDiff[key]))
	else:
		groupBPrime.append((key, groupDiff[key]))

#debug printing:
'''print('\n','groupAPrime:')
print(groupAPrime)
print('\n','groupBPrime:')
print(groupBPrime)
'''

from operator import itemgetter
#Sort the Prime lists so that they are ordered highest to lowest by the value at index 1 of tuple
sortedA = sorted(groupAPrime, key=itemgetter(1), reverse = True) #sorted list of tuples
sortedB = sorted(groupBPrime, key=itemgetter(1), reverse = True) #sorted list of tuples

#AAAND Print out the results:
print('Most unique to group A:')
for w in sortedA[:25]:
	print(sortedA.index(w)+1, sortedA[sortedA.index(w)][0], '        delta: ',sortedA[sortedA.index(w)][1])

print()


print('Most unique to group B:')
for w in sortedB[:25]:
	print(sortedB.index(w)+1, sortedB[sortedB.index(w)][0], '        delta: ',sortedB[sortedB.index(w)][1])


#TODO:  Create two new lists, matching the groups being compared, 