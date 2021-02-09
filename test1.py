from glob import glob


def main():
    for file in glob('test1/*'):
        with open(file, 'r') as fo:
            print('-----------------')
            print(file)
            print('-----------------')
            print(fo.read())
            print('\n')


if __name__ == '__main__':
    main()
