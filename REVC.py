def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1 
# Driver code 
seq=input("Enter the sequence: ")
seq_list = (Convert(seq)) 


for i in range(len(seq_list)):
    if seq_list[i] == 'T':
        seq_list[i] = 'A'
    elif seq_list[i] == 'C':
        seq_list[i] = 'G'
    elif seq_list[i] == 'A':
        seq_list[i] = 'T'
    elif seq_list[i] == 'G':
        seq_list[i] = 'C'
     
listToStr = ''.join([str(elem) for elem in seq_list])
print("Reverse compliment: ",listToStr[::-1])
