from flask import redirect, request, url_for, flash, render_template
from werkzeug.utils import secure_filename
from . import main
from .forms import UploadReads
import os
from flask.ext.bootstrap import Bootstrap

@main.route('/', methods=['GET', 'POST'])
def uploadparts_BWA():
    form = UploadReads()
    if form.validate_on_submit():
        flash('Please wait while program is aligning. This may take some time.')
        # sale files to temp folder
        GB_filename = secure_filename(form.genbank_file.data.filename)
        form.genbank_file.data.save('./static/temp/' + GB_filename)
        R1_filename = secure_filename(form.R1_file.data.filename)
        form.R1_file.data.save('./static/temp/' + R1_filename)
        R2_filename = secure_filename(form.R2_file.data.filename)
        form.R2_file.data.save('./static/temp/' + R2_filename)

        # use BWA aligner to index the GenBank file and align the paired reads
        read_1 = './static/temp/' + R1_filename
        read_2 = './static/temp/' + R2_filename
        cmd_index = "bwa index ./static/temp/" + GB_filename
        cmd_align = "bwa mem ./static/temp/" + GB_filename + " " + read_1 + " " + read_2 + \
                    " | samtools sort -O BAM -o ./static/temp/output.bam -"
        os.system(cmd_index)
        os.system(cmd_align)

        # create consensus sequence from bam file
        cmd_bam2fasta = "samtools bam2fq ./static/temp/output.bam | seqtk seq - A - > ./static/temp/output.fa"
        os.system(cmd_bam2fasta)











