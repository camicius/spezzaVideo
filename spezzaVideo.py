import sys
import csv
import os
import os.path
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="filename csv",  required=True)
parser.add_argument("-d", "--dir", help="directory dei file originali", required=True)
parser.add_argument("-o", "--outdir", help="directory dei file spezzati", required=True)
parser.add_argument("-D", "--dummy", action="store_true",      help="fai finta")

args = parser.parse_args()

dummy=args.dummy
filename=args.file
filedir=args.dir
outdir=args.outdir



outfile=filename[0:-4]+"_tomerge"
fh=open(outfile, 'w')
count=0
with open(filename, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		
		filenum=row[0]
		if filenum=="nomefile": continue
		minstart=row[1]
		secstart=row[2]
		durata=row[3]
		nome=row[4]
		
		if count<10: nome='0'+str(count)+nome
		else: nome=str(count)+nome
		count=count+1
		outfilename=outdir+nome+'.mov'
		fh.write("file "+outfilename+"\n")
		if os.path.isfile(outfilename) : 
			print ("esiste " + outfilename)
			continue
		command='avconv -y  -ss 00:'+minstart+':'+secstart+' -i '+filedir+filenum+'.mov  -t '+durata+' -codec copy '+outfilename
		
		if dummy:
			print (command)
		else:
			os.system(command)
fh.close()
sys.exit()
mergefile=filename[0:-4]+".MOV"
commandMerge="ffmpeg -safe 0 -f concat -i "+outfile+" -vcodec copy -acodec copy "+mergefile
if dummy:
	print (commandMerge)
else:
	print (commandMerge)
	os.system(commandMerge)

