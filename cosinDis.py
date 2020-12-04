import pandas as pd 
import jieba
import jieba.analyse 
import pandas as pd
import numpy as np
import csv

from sklearn.metrics import pairwise_distances
stopWordFile = open('./rank/stopWords.txt')
stops = []
for x in stopWordFile:
    stops.append(x.strip())
R = []


with open('processed.csv', 'r') as original:
    csvreader = csv.reader(original)
    for row in csvreader:
        R.append(row[0])


class Recommendation:
    def __init__(self):
        self.k_nearest = []

    def buildMatrix(self, recipes):
        M = len(recipes)
        N = 1
        terms = {}
        dt = []
        id = 0
        for recipe in recipes:
            
            tags = jieba.analyse.extract_tags(recipe, topK=20, withWeight=True, allowPOS=())
            cleaned_dict = {}
            for word, tfidf in tags:
                word = word.strip().lower()
                cleaned_dict[word] = tfidf
                if word not in terms:
                    terms[word] = N
                    N += 1
            dt.append([id, cleaned_dict])
            id+=1 
        
        dt_matrix = [[0 for i in range(N)] for j in range(M)]
        i =0
        for docid, t_tfidf in dt:
            dt_matrix[i][0] = docid
            for term, tfidf in t_tfidf.items():
                dt_matrix[i][terms[term]] = tfidf
            i += 1
        #print(dt_matrix[:10])
        dt_matrix = pd.DataFrame(dt_matrix)
        dt_matrix.index = dt_matrix[0]
        return dt_matrix 
    
    def construct_k_nearest(self, dt_matrix, k):
        value_matrix = []
        tmp = np.array(1 - pairwise_distances(dt_matrix[dt_matrix.columns[1:]], metric = "cosine"))
        similarity_matrix = pd.DataFrame(tmp, index = dt_matrix.index.tolist(), columns = dt_matrix.index.tolist())
        for i in similarity_matrix.index:
            tmp = [int(i),[]]
            j = 0
            while j < k:
                if j == 0:
                    temp = list(similarity_matrix.loc[i])
                    value_matrix.append(list(temp))
                max_col = similarity_matrix.loc[i].idxmax(axis = 1)
                value = similarity_matrix.loc[i][max_col]
                similarity_matrix.loc[i][max_col] =  -1
                if max_col != i:
                    tmp[1].append(int(max_col)) 
                    j += 1
            self.k_nearest.append(tmp)
        return value_matrix
recommendation = Recommendation()
m = recommendation.buildMatrix(R)
value_matrix = recommendation.construct_k_nearest(m, 5)
result = recommendation.k_nearest
print(result[:10])  
print(value_matrix[1])         

    









         


