inseq1 = input("Enter DNA sequence 1:")
inseq2 = input("Enter DNA sequence 2:")

compseq = str(inseq1 + inseq2).upper()

print("DNA length = %d" % (len(compseq)+5))

print(compseq)

DNA_comp_table = str.maketrans("ATCG", "TAGC")

revcompseq = compseq[::-1].translate(DNA_comp_table)

print("Reverse Complement")

print(revcompseq)

rna = compseq.replace("T", "F") + "AAAAAAA"

print("RNA length = %d" % (len(rna)))
print(rna)
