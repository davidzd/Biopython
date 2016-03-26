from Bio import SeqIO
from Bio.Seq import Seq
import os

'''
__author__ : Da
'''

if __name__ == '__main__':
	print str(os.path)
	# FIle Output
	f = open('output.txt','w')
	# read reference 
	for each_ref in SeqIO.parse("reference.fa", "fasta"):
		# type transfer
	    a = str(each_ref.seq)
	    # read reads file
	    for each_read in SeqIO.parse("reads.fa", "fasta"):
	        b = str(each_read.seq)
	        my_seq = Seq(b)
	        r_b = str(my_seq.reverse_complement())
	        # alignment
	        for x in range(0,len(a)):
	            if a[x:x+len(b)]==(b or r_b):
	                print "read_id:%s"%each_read.id
	                f.write("read_id:%s\n"%each_read.id)
	                print "positon:%s" %x
	                f.write("positon:%s\n" %x)
	                print "ref>%s"%a[x:x+len(b)]
	                f.write("ref>%s\n"%a[x:x+len(b)])
	                print ""
	                f.write('\n')
	f.close()
