from glob import glob


def main():
    for file in glob('test1/*'):
        with open(file, 'r') as fo_in:
            with open(f'{file}_result', 'w') as fo_out:
                fo_out.write(fo_in.read())


if __name__ == '__main__':
    main()
