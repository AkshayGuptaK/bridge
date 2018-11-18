from random import randint

def generatenumber():
	return randint(1,13)

def generatesuit():
	return randint(0,3)
		
def generatecard():
	return [generatenumber(), generatesuit()]
	
def generatehand():
	hand = []
	while len(hand) < 13:
		newcard = generatecard()
		if hand.count(newcard) == 0:
			hand.append(newcard)
	return hand
			
def convertfacecards(number):
	if number == 1:
		return "Ace"
	elif number == 11:
		return "Jack"
	elif number == 12:
		return "Queen"
	elif number == 13:
		return "King"
	else:
		return str(number)

def convertsuit(number):
	if number == 0:
		return "Spades"
	elif number == 1:
		return "Hearts"
	elif number == 2:
		return "Diamonds"
	elif number == 3:
		return "Cloves"
	else:
		return "No Trump"

def displayhand(hand):
	for card in hand:
		name = convertfacecards(card[0])
		suit = convertsuit(card[1])
		print("%s of %s" %(name,suit))

def calculatehcp(hand):
	score = 0
	for card in hand:
		value = card[0] - 10
		if value > 0:
			score +=value
		elif value == -9:
			score +=4
	return score

def suitlengths(hand):
	lengths = [0,0,0,0]
	for card in hand:
		lengths[card[1]] +=1
	return lengths

def determinelargestelementlargerthan(list, minimum):
	highestvalue = 0
	indexofhighestvalue = -1
	index = 0
	for number in list:
		if number > highestvalue and number >= minimum:
			highestvalue = number
			indexofhighestvalue = index
		index += 1
	return indexofhighestvalue
	
def determine1strengthbid(lengths):
	majors = [lengths[0], lengths[1]]
	minors = [lengths[2], lengths[3]]
	suit = determinelargestelementlargerthan(majors, 5)
	if suit == -1:
		return [1, determinelargestelementlargerthan(minors, 3)+2]
	else:
		return [1, suit]

def determine2strengthbid(lengths):
	del lengths[3]
	suit = determinelargestelementlargerthan(lengths, 6)
	if suit == -1:
		return [0, 0]
	else:
		return [2, suit]
	
def determinebid(hand):
	hcp = calculatehcp(hand)
	lengths = suitlengths(hand)
	if hcp > 27:
		return [4, 4]
	elif hcp >= 25:
		return [3, 4]
	elif hcp >= 22:
		return [2, 3]
	elif hcp >= 12:
		return determine1strengthbid(lengths)
	elif hcp >= 5:
		return determine2strengthbid(lengths)
	else:
		return [0, 0]
	
def displaybid(bid):
	if bid[0] == 0:
		print("Pass")
	else:
		suit = convertsuit(bid[1])
		print("Bid is %d %s" %(bid[0],suit))
	
hand = generatehand()
displayhand(hand)
displaybid(determinebid(hand))
