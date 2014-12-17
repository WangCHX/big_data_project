import pandas as pd


data = pd.read_csv("interval.tsv", header=None,names=['hour', 'cnt'], sep=r'\s+')
data = pd.read_csv("interval_min.tsv", header=None,names=['hour','min', 'cnt'], sep=r'\s+').dropna()
data['t'] = data.apply(lambda x: x['hour'] * 60 + x['min'], axis = 1)
data['t'] = data.t / 60
data.sort(columns='t').plot(x='t', y = 'cnt', xticks = range(0, 24,3))

data_usa = pd.read_csv("interval_usa.tsv", header=None, names=['hour','min', 'usa'], sep=r'\s+').dropna()
data_usa['t'] = data_usa.apply(lambda x: (x['hour'] * 60 + x['min'] - 300 + 1440) % 1440, axis = 1)
data_usa['t'] = data_usa.t / 60
data_usa.usa /= sum(data_usa.usa)

data_chn = pd.read_csv("interval_chn.tsv", header=None, names=['hour','min', 'chn'], sep=r'\s+').dropna()
data_chn['t'] = data_chn.apply(lambda x: (x['hour'] * 60 + x['min'] + 420) % 1440, axis = 1)
data_chn['t'] = data_chn.t / 60
data_chn.chn /= sum(data_chn.chn)

usa_chn = pd.merge(data_chn.sort(columns='t'), data_usa.sort(columns='t'), how="outer", on='t')
x1 = pd.DataFrame(usa_chn[['usa', 'chn']].as_matrix(),columns=['USA', 'CHN'])
x1.index = usa_chn.t
x1.plot(xticks = range(0, 24,3), style='-')

data_nyc = pd.read_csv("interval_nyc.tsv", header=None, names=['hour','min', 'nyc'], sep=r'\s+').dropna()
data_nyc.nyc /= sum(data_nyc.nyc)
data_nyc['t'] = data_nyc.apply(lambda x: (x['hour'] * 60 + x['min'] - 300 + 1440) % 1440, axis = 1)
data_nyc['t'] = data_nyc.t / 60

data_la = pd.read_csv("interval_la.tsv", header=None, names=['hour','min', 'la'], sep=r'\s+').dropna()
data_la['t'] = data_la.apply(lambda x: (x['hour'] * 60 + x['min'] - 480 + 1440 ) % 1440, axis = 1)
data_la['t'] = data_la.t / 60
data_la.la /= sum(data_la.la)

data_chi = pd.read_csv("interval_chi.tsv", header=None, names=['hour','min', 'chi'], sep=r'\s+').dropna()
data_chi['t'] = data_chi.apply(lambda x: (x['hour'] * 60 + x['min'] - 360 + 1440) % 1440, axis = 1)
data_chi['t'] = data_chi.t / 60
data_chi.chi /= sum(data_chi.chi)

nyc_la = pd.merge(data_nyc.sort(columns='t'), data_la.sort(columns='t'), how="outer", on='t')
nyc_la_chi = pd.merge(nyc_la, data_chi.sort(columns='t'), how="outer", on='t')

x2 = pd.DataFrame(nyc_la_chi[['la','chi','nyc']].as_matrix(),columns=['Los Angeles','Chicago','NYC'])
x2.index = nyc_la_chi.t
x2.plot(xticks = range(0, 24,3), style="-")

