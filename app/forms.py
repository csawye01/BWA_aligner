from flask_wtf import Form
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class UploadReads(Form):
    genbank_file = FileField('Upload Reference File (GenBank or Fasta)', validators=[DataRequired()])
    R1_file = FileField('Upload R1 FastQ File', validators=[DataRequired()])
    R2_file = FileField('Upload R2 FastQ File', validators=[DataRequired()])
    submit = SubmitField('Submit Items')