#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

import random
from sklearn import preprocessing
from sklearn import ensemble
from sklearn import svm
from sklearn import linear_model
from sklearn import neural_network
import pandas as pd
import numpy as np
import warnings
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.grid_search import GridSearchCV
warnings.filterwarnings('ignore')

# データセットおよび予実表出力先ディレクトリ
path = 'C:\\Users\\1500570\\Documents\\R\\WS\\ws_ais\\180713\\'
data =pd.read_csv(path+"txt2tpkiin_utf879.csv")
data =pd.get_dummies(data)

train, test = train_test_split(data, test_size=0.3)

y_train =train["y3"]
#del train["y"]
x_train =train.ix[:,4:]

y_test =test["y3"]
#del test["y"]
x_test =test.ix[:,4:]
print(x_test)

param_grid = [
    {'kernel': ['linear']},
    {'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
]


n_ml = 0
# メインループ（試す学習アルゴリズム数分）
while n_ml < 1:
    # ファイル出力用の実測値/予測値格納用リスト
    aarray = []
    parray = []
    # n_mlの値によって学習アルゴリズムを選択
    if n_ml == 0:
        namae = "rfr"
        #rf =GridSearchCV(svm.SVC(), param_grid, cv =5, scoring ="accuracy")
        rf = ensemble.RandomForestClassifier(n_estimators=100)
    elif n_ml == 1:
        namae = "svr"
        rf = svm.SVC()
    elif n_ml == 2:
        namae = "nnr"
        rf = neural_network.MLPClassifier(hidden_layer_sizes=(10,2))
    """
    elif n_ml == 3:
        namae = "lmr"
        rf = linear_model.LinearRegression()
    """
    # iは予測対象ではなく学習期間データの開始インデクス
    rf.fit(x_train,y_train)
    """
    for params, mean_score, all_scores in rf.grid_scores_:
        print ("{:.3f} (+/- {:.3f}) for {}".format(mean_score, all_scores.std() / 2, params))
    """
    py = rf.predict(x_test)
    aarray.append(y_test)
    parray.append(py)
    eva =metrics.confusion_matrix(y_test,py)
    evavalue =metrics.accuracy_score(y_test,py)
    p = np.vstack((aarray,parray)).swapaxes(0,1)
    np.savetxt(path+"result_"+namae+".csv",p,delimiter=",")
    print(eva)
    print(evavalue)
    print(len(eva))
    n_ml += 1
print("end!!")
