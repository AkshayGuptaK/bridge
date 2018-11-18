from random import randint

def generateNumber():
	return randint(1,13)

def generateSuit():
	return randint(0,3)
		
def generateCard():
	return [generateNumber(), generateSuit()]
	
def generateHand():
	hand = []
	while len(hand) < 13:
		newcard = generateCard()
		if hand.count(newcard) == 0:
			hand.append(newcard)
	return hand
			
def convertFaceCards(number):
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

def convertSuit(number):
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

def displayHand(hand):
	for card in hand:
		name = convertFaceCards(card[0])
		suit = convertSuit(card[1])
		print("%s of %s" %(name,suit))

def calculateHighCardPoints(hand):
	score = 0
	for card in hand:
		value = card[0] - 10
		if value > 0:
			score +=value
		elif value == -9:
			score +=4
	return score

def suitLengths(hand):
	lengths = [0,0,0,0]
	for card in hand:
		lengths[card[1]] +=1
	return lengths

def determineLargestElementLargerThan(list, minimum):
	highestvalue = 0
	indexofhighestvalue = -1
	index = 0
	for number in list:
		if number > highestvalue and number >= minimum:
			highestvalue = number
			indexofhighestvalue = index
		index += 1
	return indexofhighestvalue
	
def determine1StrengthBid(lengths):
	majors = [lengths[0], lengths[1]]
	minors = [lengths[2], lengths[3]]
	suit = determineLargestElementLargerThan(majors, 5)
	if suit == -1:
		return [1, determineLargestElementLargerThan(minors, 3)+2]
	else:
		return [1, suit]

def determine2StrengthBid(lengths):
	del lengths[3]
	suit = determineLargestElementLargerThan(lengths, 6)
	if suit == -1:
		return [0, 0]
	else:
		return [2, suit]
	
def determineBid(hand):
	hcp = calculateHighCardPoints(hand)
	lengths = suitLengths(hand)
	if hcp > 27:
		return [4, 4]
	elif hcp >= 25:
		return [3, 4]
	elif hcp >= 22:
		return [2, 3]
	elif hcp >= 12:
		return determine1StrengthBid(lengths)
	elif hcp >= 5:
		return determine2StrengthBid(lengths)
	else:
		return [0, 0]
	
def displayBid(bid):
	if bid[0] == 0:
		print("Pass")
	else:
		suit = convertSuit(bid[1])
		print("Bid is %d %s" %(bid[0],suit))
	
hand = generateHand()
displayHand(hand)
displayBid(determineBid(hand))
