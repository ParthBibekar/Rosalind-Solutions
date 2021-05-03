DNA_seq = input("Enter the DNA sequence: ")
motif = input("Enter the motif sequence: ")
l = []

for i in range(len(DNA_seq)):
    if DNA_seq[i:i+len(motif)] == motif:
        l.append(i+1)

string = " ".join(map(str, l))
print(string)
