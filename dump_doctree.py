import sys
import pathlib
import pickle
import docutils.nodes


def traverse(node: docutils.nodes.Node, level=0):
    indent = '  ' * level
    match node:
        case docutils.nodes.Text():
            print(f'{indent}{node}')

        case _:
            print(f'{indent}{type(node)}:{node.line}')
    for child in node.children:
        traverse(child, level+1)


if __name__ == '__main__':
    document = pickle.loads(pathlib.Path(sys.argv[1]).read_bytes())
    traverse(document)
