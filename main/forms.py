from flask_wtf import Form
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class UploadReads(Form):
    genbank_file = FileField('Upload GenBank Reference File', validators=[DataRequired(), FileAllowed(['gb'], 'GenBank (.gb) files only!')])
    R1_file = FileField('Upload R1 FastQ File', validators=[DataRequired(), FileAllowed(['fastq', 'fastq.gz'], 'fastq and fastq.gz files only!')])
    R2_file = FileField('Upload R2 FastQ File', validators=[DataRequired(), FileAllowed(['fastq', 'fastq.gz'], 'fastq and fastq.gz files only!')])
    submit = SubmitField('Submit Items')