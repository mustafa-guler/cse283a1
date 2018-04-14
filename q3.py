import numpy as np
import sys
import matplotlib.pyplot as plt

# C,H,N,O,S
comp = { 'G' :np.array([2, 3, 1, 1,0]),
        'A' : np.array([3,5,1,1,0]),
        'S' : np.array([3,5,1,2,0]),
        'P' : np.array([5,7,1,1,0]),
        'V' : np.array([5,9,1,1,0]),
        'T' : np.array([4,7,1,2,0]),
        'C' : np.array([3,5,1,1,1]),
        'L' : np.array([6,11,1,1,0]),
        'I' : np.array([6,11,1,1,0]),
        'N' : np.array([4,6,2,2,0]),
        'D' : np.array([4,5,1,3,0]),
        'Q' : np.array([5,8,2,2,0]),
        'K' : np.array([6,12,2,1,0]),
        'E' : np.array([5,7,1,3,0]),
        'M' : np.array([5,9,1,1,1]),
        'H' : np.array([6,7,3,1,0]),
        'F' : np.array([9,9,1,1,0]),
        'R' : np.array([6,12,4,1,0]),
        'Y' : np.array([9,9,1,2,0]),
        'W' : np.array([11,10,2,1])}

weights = [12.0107, 1.0079, 14.0067, 15.9994, 32.065]
peptide = sys.argv[1]
pC13,pN15,pO18 = map(float,sys.argv[2:5])
#pH2 = 0
#if len(sys.argv) == 6:
#    pH2 = float(sys.argv[5])

# account for extra water
pep_composition = np.array([0,3,0,1,0])

for AA in peptide:
    pep_composition += comp[AA]

mass = np.dot(weights,pep_composition)
print("mass:", mass)
print(pep_composition)

polyC = np.fft.fft(np.array([pC13,1-pC13]),6)
polyN = np.fft.fft(np.array([pN15,1-pN15]),6)
polyO = np.fft.fft(np.array([pO18,0,1-pO18]),6)
#polyH = np.fft.fft(np.array([pH2, 1-pH2]),6)

profile = polyC**pep_composition[0] * polyN**pep_composition[2] * polyO**pep_composition[3]
profile = np.fft.ifft(profile)

result = np.flipud(profile.real)
print(result)
