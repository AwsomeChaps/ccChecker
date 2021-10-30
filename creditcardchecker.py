
def main():
	with open('credit_cards.txt', 'r') as f:
		cards = f.read().splitlines()
	f.close()
	issuers = []
	validity = []
	checkdigits = [] 
	for card in cards:
		if card[0]=='3':
			issuers.append("Travel")
			validity.append('y')
			checkdigits.append(card[-1])
		elif card[0]=='4':
			issuers.append("Visa")
			validity.append('y')
			checkdigits.append(card[-1])
		elif card[0]=='5':
			issuers.append("MasterCard")
			validity.append('y')
			checkdigits.append(card[-1])
		elif card[0]=='6':
			issuers.append("Discover")
			validity.append('y')
			checkdigits.append(card[-1])
		else:
			issuers.append("N/A")
			validity.append('n')
			checkdigits.append("N/A")



	open('cc_out.txt', 'w').close()
	with open('cc_out.txt', 'a') as f:
		f.write("ccNumber, Issuers, Validity, Check Digit\n")
		for i in range(0, len(cards)-1):
			f.write(cards[i] + ", " + issuers[i] + ", " + validity[i] + ", " +checkdigits[i] + "\n")

	f.close()


if __name__ == '__main__':
	main()