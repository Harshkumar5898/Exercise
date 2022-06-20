import pickle
import requests


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response = requests.get(url)
file = url.split('/')[-1]
with open(file, 'wb') as f:
    f.write(response.content)

with open('iris.data') as f:
    l = f.read()


l1 = l.split('\n')

l2 = []

for item in l1:
    h = item.split(',')
    l2.append(h)


# l2 = [item.split(',') for item in l1]

with open('iris.pkl', 'wb') as f:
    pickle.dump(l2, f)


with open('iris.pkl', 'rb') as f:
    file = pickle.load(f)
    print(file)
