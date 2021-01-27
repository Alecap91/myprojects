risposte_giuste = 0
risposta_1 = str(input("\nCompleta la frase: \n'Questa amico mio non è una ...'"))


if str(risposta_1) == 'Miniera' or 'una miniera' or 'Moria':
    print('\n\nBravo')
    risposte_giuste+=1
    print('\nLe tue risposte giuste:', risposte_giuste)
else:
    print('\n\nNon è la chiave di Orthanc')
    risposte_giuste+=-1
    print('\nLe tue risposte giuste:', risposte_giuste)

risposta_2 = input("\nRispondi alla domanda: \nCosa vuoi Gandalf il Rimbambito? ")
if risposta_2 == 'La chiave di Orthanc' or 'La chiave di Ortanc' or 'La chiave di Ortnac':
    print('\n\nBravo')
    risposte_giuste+=1
    print('\nLe tue risposte giuste:', risposte_giuste)
else:
    print('\n\nNon è Theoden, signore dei calli')
    risposte_giuste+=-1
    print('\nLe tue risposte giuste:', risposte_giuste)

risposta_3 = input("\nCompleta la frase: \nProvi lei a telefonare a Richard Benson e provi a urlare come urlo io ")
if risposta_3 == 'POLLO' or 'UN POLLO!' or 'POLLO!' or 'Un pollo!':
    print('\nBravo')
    risposte_giuste+=1
    print('\nLe tue risposte giuste:', risposte_giuste)
else:
    print('\n\nNon sei pronto per essere il signore dei signori')

if risposte_giuste == 3:
    print('\n\nSei il Signore dei Signori!')
elif risposte_giuste == 2:
    print('\n\nSei un Sovrintendente!')
else:
    print('\n\nIdiota di un Tuc!')
