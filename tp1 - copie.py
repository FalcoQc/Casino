from random import randrange



continuer_la_partie = True
gains_totaux = 0
print("Pour jouer à la roulette vous devez choisir une case entre 0 et 49 suivi d'une mise")
while continuer_la_partie == True:
	i = 0
	while i != 1:
		try:
			numero_choisi = int(input("Quelle case choisissez vous \n> "))
			mise_de_départ = int(input("Combien désirez vous misez ? \n> "))
		except ValueError:
			print("Veuillez saisir un nombre s.v.p.")
		else:
			if (numero_choisi < 0) or (numero_choisi > 49):
				print("Votre case, doit être entre 0 et 49")
			elif mise_de_départ < 0:
				print("Votre mise ne peut être négative.")
			elif(numero_choisi >= 0) and (numero_choisi <= 49):
				i = 1
			else:
				print("oups...")


	print("Voilà, le croupier va maintenant faire tourner la roulette et",
		"nous calculerons vos gains par la suite.")
	case_gagnante = randrange(50)
	gains = 0
	if numero_choisi == case_gagnante:
		gains = mise_de_départ * 3
	elif (numero_choisi % 2 == 0) and (case_gagnante % 2 == 0):
		gains = mise_de_départ / 2
	elif (numero_choisi % 2 == 1) and (case_gagnante % 2 == 1):
		gains = mise_de_départ / 2
	gains_totaux += gains
	print("La case gagnante est", case_gagnante)
	print("Donc vos gains sont de", gains)
	print("Vos gains totaux sont de", gains_totaux)

	choix = input("Désirez vous rejouer à la roulette ? \n> ")
	if choix == 'Oui' or choix == 'oui':
		continuer_la_partie = True
	else:
		print("D'accord bonne fin de journée.")
		continuer_la_partie = False

print("Je fais des éssais, plein d'essai :OOOOO")