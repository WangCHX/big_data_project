import pandas as pd
data = pd.read_csv('check_in_num_friend.tsv',sep='\t', names=['user_check_in_count','userid','statuscount','followerscount','friendscount'])
data.corr()