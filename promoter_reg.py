from Bio import SeqIO
gene = SeqIO.read("genome_jejuni.fasta", "fasta")
genome_seq = str(gene.seq)
print len(genome_seq)


alt_map = {'ins':'0'}


len_genome=len(genome_seq)

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
def reverse_complement(seq):    
    for k,v in alt_map.iteritems():
        seq = seq.replace(k,v)
    bases = list(seq) 
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    for k,v in alt_map.iteritems():
        bases = bases.replace(v,k)
    return bases

reverse_comp = reverse_complement(genome_seq)
'''

for i in range(len_genome):
	if strin == reverse_comp[i:i+len(strin)]:
		print i

'''
string_to_write = ""
i=0
with open("gene_result.txt", 'r') as txt:
	for line in txt:
		tokens = line.split("\t")
		if i ==0:
			i+=1
		
		if tokens[14] == "minus":
			gen_start = int(tokens[13])
			gen_end = int(tokens[12])
			start = len_genome -gen_start
			end = start + (gen_start - gen_end) +1 
			string_to_write += (">" + tokens[5]+"-"+ tokens[7]+ "\n")
			string_to_write += genome_seq[start:end] +"\n\n"
			string_to_write += ("> 5' flanking region"+"\n")
			string_to_write += genome_seq[start-60:start] + "\n\n"
			string_to_write += ("> 3' flanking region"+"\n")
			string_to_write += genome_seq[end:end+10] + "\n\n\n"
			
		elif tokens[14] == "plus":
			gen_start = int(tokens[12])
			gen_end = int(tokens[13])
			string_to_write += (">" + tokens[5]+"-"+ tokens[7]+ "\n")
			string_to_write += reverse_comp[gen_start-1:gen_end] + "\n\n"
			string_to_write += ("> 5' flanking region"+"\n")
			string_to_write += reverse_comp[gen_start-61:gen_start-1] + "\n\n"
			string_to_write += ("> 3' flanking region"+ "\n")
			string_to_write += reverse_comp[gen_end:gen_end+10] + "\n\n\n"
	
with open("output.txt", "w") as text_file:
    text_file.write(string_to_write)

	

