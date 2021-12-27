import pickle
import pathlib
from pprint import pprint

ENV = pathlib.Path('build/.doctrees/environment.pickle')


def main():
    env = pickle.loads(ENV.read_bytes())
    # print("docname:", env.docname)
    for domain, data in env.domaindata.items():
        print("domain:", domain)
        pprint(data)


if __name__ == '__main__':
    main()
