import pickle
favorites = [
    'aaa', 'bbb', 'ccc','ddd', 'eee', 'fff', 'eee'
]
save_file = open('favorites.dat', 'wb')
aa = pickle.dump(favorites,save_file)
save_file.close
print(aa)
