This Python Flask app will take a reference plasmid genome Fasta file and 2 paired read NGS FastQ files and align them. 
The program BWA mem is used for aligning the reads, Samtools for a consensus sequence and Clustal Omega for the alignment of the reference sequence to the consensus sequence. 
This will then output a graphic representation of the alignment against the reference sequence and a downloadable Fasta file of the consensus sequence. 
