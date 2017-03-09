# -*- coding: utf-8 -*-

import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--subdirectory", metavar="DIR", help="Output directory name. By default = 'BBs'.", default="BBs", action="store", type=str, required=False, dest="subdir")
parser.add_argument("-ts", "--temporarySubdir", help="temporary subdirectory. By default = 'BBs_temp'.", default="BBs_temp", action="store", type=str, required=False, dest="tempSubdir")
parser.add_argument("-g", "--genome", help="specify version of the genome for which chromosome sizes file will be downloaded from UCSC (unles '-d False' would be specified). By default = 'hg38'.", default="hg38", action="store", type=str, required=False, dest="genome")
parser.add_argument("-d", "--UCSC_binariesDownload", help="Specify if program download binary bedToBigBed and fetchChromSizes files from UCSC (set to True) or not (set to False). By default = 'True'.", default=True, action="store", type=str, required=False, dest="down")
parser.add_argument("-os", "--operationSystem", help="Specify either 1 for MAC OS X (macOSX.x86_64), or 2 for linux (linux.x86_64). By default = '1'.", default=1, action="store", type=int, required=False, dest="system")
parser.add_argument("-c", "--chromosomeSizesFile", help="Flag to use if one want to specify chromosome sizes file. By default = 'fetchUCSC', which corresponds to download of the GENOME.chrom.sizes file from UCSC.", default="fetchUCSC", action="store", type=str, required=False, dest="chrSizes")
args = parser.parse_args()

subdirectory = args.subdir
temporarySubdir = args.tempSubdir
genome = args.genome
proceed = True

print subprocess.Popen("mkdir {}".format(subdirectory), shell=True, stdout=subprocess.PIPE).stdout.read()
print subprocess.Popen("mkdir {}".format(temporarySubdir), shell=True, stdout=subprocess.PIPE).stdout.read()
print subprocess.Popen("ls -1 *.bed > {}/listOfFiles.txt".format(temporarySubdir), shell=True, stdout=subprocess.PIPE).stdout.read()

if (args.down == "True"):
	if (args.system == 1):
		tmp = 'macOSX.x86_64'
	elif (args.system == 2):
		tmp = 'linux.x86_64'
	else:
		print "Value of -os / --operationSystem flag was wrongly specified. It should have been equal to either 1 for MAC OS X (macOSX.x86_64), or 2 for linux (linux.x86_64)."
		proceed = False
	if proceed:
		print subprocess.Popen("wget http://hgdownload.cse.ucsc.edu/admin/exe/{}/bedToBigBed".format(tmp), shell=True, stdout=subprocess.PIPE).stdout.read()
		print subprocess.Popen("wget http://hgdownload.cse.ucsc.edu/admin/exe/{}/fetchChromSizes".format(tmp), shell=True, stdout=subprocess.PIPE).stdout.read()
	
if (args.chrSizes == "fetchUCSC"):
	print subprocess.Popen("chmod +x ./bedToBigBed ./fetchChromSizes", shell=True, stdout=subprocess.PIPE).stdout.read()
	print subprocess.Popen("./fetchChromSizes {0} > {0}.chrom.sizes".format(genome), shell=True, stdout=subprocess.PIPE).stdout.read()
	chrSizeFileName = "{0}.chrom.sizes".format(genome)
else:
	chrSizeFileName = args.chrSizes

if proceed:
	infile = open("{}/listOfFiles.txt".format(temporarySubdir), 'r')
	for row in infile:
		tmp = row.split('.')
		
		print subprocess.Popen("bedtools sort -i {0}.bed > {1}/{0}.sorted.bed".format(tmp[0], temporarySubdir), shell=True, stdout=subprocess.PIPE).stdout.read()
		print "{} - bed file was sorted!".format(tmp[0])
		print subprocess.Popen("./bedToBigBed {1}/{0}.sorted.bed {3} {2}/{0}.bb".format(tmp[0], temporarySubdir, subdirectory, chrSizeFileName), shell=True, stdout=subprocess.PIPE).stdout.read()
		print "{} - bigBed(bb) file created!".format(tmp[0])
	
	print subprocess.Popen("rm -r {}".format(temporarySubdir), shell=True, stdout=subprocess.PIPE).stdout.read()
	print "Tmp folder deleted, everything completed. However, please inspect the result filese because bedtools, bedToBigBed and fetchChromSizes were working independently of this python script and the error could have occured at their side."
		
	infile.close()
