import sys,os
from scikits.audiolab import wavread, wavwrite

from shutil import copyfile


import numpy

with open(sys.argv[1]) as fin:
	
    for line in fin:
        parts = line.split() # split line into parts
        sid=parts[0]
	fid=parts[1]
	cg=parts[2]
	if not os.path.exists(str(sid)):
			os.makedirs(str(sid))
	if cg == "human":
		src="/media/knrk/MyWork/NCC&SPIN/ASV-Spoof/wav/"+sid+"/"+fid+".wav"
		dst="/media/knrk/MyWork/NCC&SPIN/ASV-Spoof/newdatabase/"+sid+"/"+fid+".wav"
		#print src
		#print dst
		print cg
		copyfile(src, dst)
				
		
	
	


