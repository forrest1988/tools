============== BED2BB Converter ==============

<h5>What is this script for?</h5>
The purpose of BED2BB_Converter is to convert all BED files (i.e. *.bed) from current directory, to bigBed files (i.e. *.bb) that will be stored in a subfolder.

<h5>Dependencies:</h5>
Script is written in Python (2.7) and is using bedtools (http://bedtools.readthedocs.io/en/latest/) and internet connection to download binaries from UCSC (http://hgdownload.cse.ucsc.edu/admin/exe/). The latter may be skipped if "-d" flag is used with "False" variable and if the file with chromosome sizes is provided using "-c" flag.

<h5>Installation and usage:</h5>
Just download the script and copy it to the catalog in which you have stored all *.bed files, that you wish to convert to bigBed format. 
For the default parameters run the following command:

<code>python BED2BB_Converter_1.00.py</code>


<b>usage</b>: BED2BB_Converter_1.00.py [-h] [-s DIR] [-ts TEMPSUBDIR] [-g GENOME] [-d DOWN] [-os SYSTEM] [-c CHRSIZES]

optional arguments:

-h, --help -> show this help message and exit
  
-s DIR, --subdirectory DIR ->  Output directory name. By default = 'BBs'.
  
-ts TEMPSUBDIR, --temporarySubdir TEMPSUBDIR -> temporary subdirectory. By default = 'BBs_temp'.
  
-g GENOME, --genome GENOME -> specify version of the genome for which chromosome sizes file will be downloaded from UCSC (unles '-d False' would be specified). By default = 'hg38'.
  
-d DOWN, --UCSC_binariesDownload DOWN -> Specify if program download binary bedToBigBed and fetchChromSizes files from UCSC (set to True) or not (set to False). By default = 'True'.
  
-os SYSTEM, --operationSystem SYSTEM -> Specify either 1 for MAC OS X (macOSX.x86_64), or 2 for linux (linux.x86_64). By default = '1'.
  
-c CHRSIZES, --chromosomeSizesFile CHRSIZES -> Flag to use if one want to specify chromosome sizes file. By default = 'fetchUCSC', which corresponds to download of the GENOME.chrom.sizes file from UCSC.
  

================================================

