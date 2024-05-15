# import random
# wylosowana=random.randint(1 ,10)
# print(wylosowana)


# import random
# wylosowana=random.random()
# print(wylosowana)
# zaokraglona=round(wylosowana,2)
# print(zaokraglona)


# import random
# wylosowana=random.random()
# print(f"{wylosowana:.2f}")



# import random
# slowo="Kognitywistyka"
# wylosowana=random.choice(slowo)
# print(wylosowana)

#losuje 2 kolejne literki:
# import random
# slowo="Maria"
# start=random.randint(0, len(slowo)-2)
# los=slowo[start:start+2]
# print(los)

# losuje 2 niekoniecznie kolejne literki:
# import random
# slowo="Maria"
# los=random.choice(slowo)+random.choice(slowo)
# print(los)

# #czas reakcji pokazuje
# import time
# cyfra=0
# start=time.time()
# while cyfra!=1:
#     print("Nie wcisnąłeś\"1\"\n")
#     cyfra=int(input())
# koniec=time.time()
# czas_trwania=koniec-start
# print("Na wciśnięcie 1 potrzebowałeś:", czas_trwania)


# import time
# print("Początek:",time.ctime())
# time.sleep(5)
# print("Koniec:",time.ctime())

#zadane 3
import random
sciany=6
wylosowana=random.randint(1,sciany)
print(wylosowana)

import random
wylosowana=random.randint(1,6)
print(wylosowana)

