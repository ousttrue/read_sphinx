import sys
import pickle
from docutils.writers import get_writer_class
from docutils.io import StringOutput

doctree = pickle.load(open(sys.argv[1], 'rb'))
print(type(doctree))
writer = get_writer_class('pseudoxml')()
output = StringOutput(encoding='utf-8')
print(writer.write(doctree, output))
