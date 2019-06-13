# spezzaVideo
script in python per spezzare i video delle dashcam a partire da un file csv.
Usa avconv chiamato con os.system 


Opzioni obbligatorie:

-f --file  : nome del file csv contenente le descrizioni degli spezzoni da tagliare
-d --dir   : directory dove sono cotenuti i file originali
-o --outdir: directory dove verranno messi i file spezzati

Opzione supplementare:
-D --dummy : non taglia i file ma stampa su stdout il comando che farebbe.

Le directory e i nomi dei file sono usati per "comporre" il comando avconv, che è il programma che effettua il taglio dei file. 
Ai nomi dei file è "preposto" un numero in modo da non dover garantire che i nomi dei file siano univoci nel file csv

python spezzaVideo.py -f esempio.csv -o destinazione/ -d originali/


