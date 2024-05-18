import pandas as pd


def main():
    sybils = pd.read_csv('initialList.csv')

    with open('wallets.txt', 'r') as f:
        wallets = set(map(str.lower, f.read().split()))
    sybils = sybils[sybils['ADDRESS'].isin(wallets)]
    sybils['ADDRESS'] = sybils['ADDRESS'].map(lambda x: x.lower())

    if len(sybils) == 0:
        print('Good job! 0 wallets in sybil report!')
    else:
        print(f'Found {len(sybils)} sybil wallets:')
        print('\n'.join(sybils['ADDRESS'].tolist()))


if __name__ == '__main__':
    main()
