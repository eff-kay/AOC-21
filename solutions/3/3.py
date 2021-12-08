import pandas as pd


def first():
    inp = open('3.txt').read().split("\n")
    xa = [list(x) for x in inp]
    ya = zip(*xa)

    gamma = ''
    eps = ''
    for za in list(ya):
        gbit = max(set(za), key = za.count)
        ebit = min(set(za), key = za.count)
        gamma+=str(gbit)
        eps+=str(ebit)

    gamma = int(gamma, 2)
    eps = int(eps, 2)


    print(gamma, eps)
    return gamma*eps



def second():
    def o():
        inp = open('3.txt').read().split("\n")
        xa = [list(x) for x in inp]
        df = pd.DataFrame(xa)

        for i in df.columns[:20]:
            df_count = df.apply(lambda x:x.value_counts())
            def la(x):
                if x.iloc[0]>x.iloc[1]:
                    return x.index[0]
                elif x.iloc[0]<x.iloc[1]:
                    return x.index[1]
                else:
                    return '1'

            df_count = df_count.apply(la)
            df_count = df_count.T
            df_max = df_count
            mask = df[i]==df_max[i]
            df = df[mask]
            if df.shape[0]==1:
                break

        fin = ''.join(df.iloc[0])
        return int(fin, 2)

    def co():
        inp = open('3.txt').read().split("\n")
        xa = [list(x) for x in inp]
        df = pd.DataFrame(xa)

        for i in df.columns[:20]:
            df_count = df.apply(lambda x:x.value_counts())
            def la(x):
                if x.iloc[0]<x.iloc[1]:
                    return x.index[0]
                elif x.iloc[0]>x.iloc[1]:
                    return x.index[1]
                else:
                    return '0'

            df_count = df_count.apply(la)
            df_count = df_count.T
            df_max = df_count
            mask = df[i]==df_max[i]
            df = df[mask]
            if df.shape[0]==1:
                break

        fin = ''.join(df.iloc[0])
        return int(fin, 2)
    ox = o()
    co2 = co()
    print(ox, co2)
    return ox*co2

if __name__=="__main__":
    print(second())
