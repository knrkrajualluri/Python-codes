import sys,os
from scikits.audiolab import wavread, wavwrite

from shutil import copyfile


import numpy

with open(sys.argv[1]) as fin:
	
    for line in fin:
        parts = line.split() # split line into parts
        sid=parts[0]  # speaker id
	fid=parts[1]  # file id
	cg=parts[2]   # category ie human/spoof
	if not os.path.exists(str(sid)):
			os.makedirs(str(sid))
	if cg == "human":
		src="/media/knrk/MyWork/NCC&SPIN/ASV-Spoof/wav/"+sid+"/"+fid+".wav"  # source path
		dst="/media/knrk/MyWork/NCC&SPIN/ASV-Spoof/newdatabase/"+sid+"/"+fid+".wav" # destinaton path
		#print src
		#print dst
		print cg
		copyfile(src, dst)  # to copy files
				
		
	
	


