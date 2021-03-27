import sys

def Convert(seq): 
    list1 = [] 
    list1[:0] = seq 
    return list1 

RNA_seq = input("Enter the RNA sequence: ")
b = Convert(RNA_seq)
a = []
protein = []

for j in range(len(b)):
    if (j+1)%3 == 0:
        a.append(b[j-2:j+1])

for i in range(len(a)):
    if(a[i] == ['U','U','U'] or a[i] == ['U','U','C']):
        protein.append('F')

    if(a[i] == ['U','U','A'] or a[i] == ['U','U','G'] or a[i] == ['C','U','U'] or a[i] == ['C','U','C'] or a[i] == ['C','U','A'] or a[i] == ['C','U','G']):
        protein.append('L')

    if(a[i] == ['U','C','U'] or a[i] == ['U','C','C'] or a[i] == ['U','C','A'] or a[i] == ['U','C','G'] or a[i] == ['A','G','U'] or a[i] == ['A','G','C']):
        protein.append('S')

    if(a[i] == ['U','A','U'] or a[i] == ['U','A','C']):
        protein.append('Y')

    if(a[i] == ['U','G','C'] or a[i] == ['U','G','U']):
        protein.append('C')

    if(a[i] == ['U','G','G']):
        protein.append('W')

    if(a[i] == ['C','C','U'] or a[i] == ['C','C','C'] or a[i] == ['C','C','A'] or a[i] == ['C','C','G']):
        protein.append('P')

    if(a[i] == ['C','A','U'] or a[i] == ['C','A','C']):
        protein.append('H')

    if(a[i] == ['C','A','A'] or a[i] == ['C','A','G']):
        protein.append('Q')

    if(a[i] == ['C','G','U'] or a[i] == ['C','G','C'] or a[i] == ['C','G','A'] or a[i] == ['C','G','G'] or a[i] == ['A','G','A'] or a[i] == ['A','G','G']):
        protein.append('R')

    if(a[i] == ['A','U','U'] or a[i] == ['A','U','C'] or a[i] == ['A','U','A']):
        protein.append('I')

    if(a[i] == ['A','U','G']):
        protein.append('M')

    if(a[i] == ['A','C','U'] or a[i] == ['A','C','C'] or a[i] == ['A','C','A'] or a[i] == ['A','C','G']):
        protein.append('T')

    if(a[i] == ['A','A','U'] or a[i] == ['A','A','C']):
        protein.append('N')

    if(a[i] == ['A','A','A'] or a[i] == ['A','A','G']):
        protein.append('K')

    if(a[i] == ['G','U','U'] or a[i] == ['G','U','C'] or a[i] == ['G','U','A'] or a[i] == ['G','U','G']):
        protein.append('V')

    if(a[i] == ['G','C','U'] or a[i] == ['G','C','C'] or a[i] == ['G','C','A'] or a[i] == ['G','C','G']):
        protein.append('A')

    if(a[i] == ['G','A','U'] or a[i] == ['G','A','C']):
        protein.append('D')

    if(a[i] == ['G','A','A'] or a[i] == ['G','A','G']):
        protein.append('E')

    if(a[i] == ['G','G','U'] or a[i] == ['G','G','C'] or a[i] == ['G','G','A'] or a[i] == ['G','G','G']):
        protein.append('G')

    if(a[i] == ['U','A','A'] or a[i] == ['U','A','G'] or a[i] == ['U','G','A']):
        listToStr = ''.join(map(str, protein))
        print(listToStr)
        sys.exit()    
