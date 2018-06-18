This Python Flask app will take a reference plasmid genome file and the 2 paired read NGS files and align them. 
This uses the program BWA mem for aligning the reads, Samtools for a consensus sequence and Clustal Omega for the alignment of the reference sequence to the consensus sequence. 
This will then output a graphic representation of the alignment against the reference sequence. 
