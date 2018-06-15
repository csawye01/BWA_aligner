from itertools import groupby
from operator import itemgetter
from PIL import Image, ImageDraw

def diff(a, b):
    index_list = []
    for index, (char1, char2) in enumerate(zip(a, b)):
        if char1 != char2:
            index_list.append(index)
    return index_list

def SNP_ranges(d):
    ranges = []
    for k, g in groupby(enumerate(d), lambda x: x[0] - x[1]):
        group = (map(itemgetter(1), g))
        group = list(map(int, group))
        ranges.append((group[0], group[-1]))
    return ranges

def fasta_split(fasta_file):
    seq1 = ''
    seq2 = ''
    count = 0
    for fasta in fasta_file:
        name, sequence = fasta.id, str(fasta.seq)
        if count == 0:
            seq1 = sequence
        elif count == 1:
            seq2 = sequence
        count += 1
    return seq1, seq2

def create_img(seq1, seq2, ranges):
    # size of image
    canvas = (len(seq1), 600)

    # scale ration
    scale = 6
    thumb = canvas[0] / scale, canvas[1] / 5

    # init canvas
    im = Image.new('RGBA', canvas, (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.rectangle([0, 0, (len(seq1)), 150], fill="gray")
    draw.rectangle([0, 250, (len(seq2)), 400], fill="gray")

    # draw rectangles
    for start, end in ranges:
        draw.rectangle([start, 250, end, 400], fill="red")

    # make thumbnail
    im.thumbnail(thumb)

    file_name = './static/temp/seq_align_PIL.png'
    # save image
    im.save(file_name)

    return file_name