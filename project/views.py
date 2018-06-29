from flask import redirect, url_for, flash, render_template, Flask
from . import app
from werkzeug.utils import secure_filename
from .forms import UploadReads
import os
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio import SeqIO
from Bio.Align.Applications import ClustalOmegaCommandline
from .helper_functions import diff, SNP_ranges, fasta_split, create_img


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadReads()
    message = flash('Please note that the alignment may take several minutes.')
    if form.validate_on_submit():

        # sale files to temp folder
        GB_filename = secure_filename(form.genbank_file.data.filename)
        form.genbank_file.data.save('static/temp/' + GB_filename)
        R1_filename = secure_filename(form.R1_file.data.filename)
        form.R1_file.data.save('static/temp/' + R1_filename)
        R2_filename = secure_filename(form.R2_file.data.filename)
        form.R2_file.data.save('static/temp/' + R2_filename)

        # use BWA aligner to index the GenBank file and align the paired reads
        ref_fasta = 'static/temp/' + GB_filename
        read_1 = 'static/temp/' + R1_filename
        read_2 = 'static/temp/' + R2_filename
        cmd_index = "bwa index " + ref_fasta
        cmd_align = "bwa mem " + ref_fasta + " " + read_1 + " " + read_2 + \
                    " | samtools sort -O BAM -o static/temp/output.bam -"
        os.system(cmd_index)
        os.system(cmd_align)

        # create consensus sequence from bam file
        cdm_sortbam = "samtools sort static/temp/output.bam  -o output_sorted.bam"
        cmd_bam2fasta = "samtools mpileup -uf " + ref_fasta + " static/temp/output_sorted.bam | bcftools call -c| vcfutils.pl vcf2fq > static/temp/cons.fq"
        os.system(cdm_sortbam)
        os.system(cmd_bam2fasta)

        SeqIO.convert("static/temp/cons.fq", "fastq", "static/temp/cons_fasta.fasta", "fasta")
        ref_record = SeqIO.read(ref_fasta, "fasta")
        RefSeq = ref_record.seq
        plas_record = SeqIO.read('static/temp/cons_fasta.fasta', "fasta")
        AlignedSeq = plas_record.seq

        records = (SeqRecord(Seq(seq, IUPAC.protein), id=str(index), name="Seq", description="Seq") for index, seq in
                   enumerate([str(RefSeq), str(AlignedSeq)]))

        with open("static/temp/combined_seqs.fasta", 'w') as output_handle:
            SeqIO.write(records, output_handle, "fasta")

        clustalomega_cline = ClustalOmegaCommandline(infile="static/temp/combined_seqs.fasta",
                                                     outfile="static/temp/aligned_seqs.fasta",
                                                     verbose=True, auto=True, force=True)
        clustalomega_cline()

        fasta_sequences = SeqIO.parse(open("static/temp/aligned_seqs.fasta"), 'fasta')

        seq1, seq2 = fasta_split(fasta_sequences)

        d = diff(seq1, seq2)
        ranges = SNP_ranges(d)

        create_img(seq1, seq2, ranges)


        return redirect(url_for('Aligned_Seqs'))

    return render_template('index.html', form=form, message=message)

@app.route('/Aligned_Seqs', methods=['GET', 'POST'])
def Aligned_Seqs():
    return render_template('Aligned_Seqs.html')











