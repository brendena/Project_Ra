import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve, auc
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from io import StringIO
import re


def createRocCurve(train_X,train_Y,test_X,test_Y,  titleCurve, fileTitle, justCount=False):
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(train_X, train_Y)

    print("size of validation set " + str(len(test_X) ) + "\n")
    status = rf.predict_proba(test_X)
    if(justCount == True):
        count = 0
        for i in range(0, len(status)):
            if(status[i][0] < status[i][1]):
                count = count + 1
        print(str(count) + " got right")
        print(str(len(test_X)) + " total size")
        print(str(count/len(test_X)) + " % correct")
    
    else:
        fpr, tpr, _ = roc_curve(test_Y, status[:,1])
        roc_auc = auc(fpr, tpr)
        print(roc_auc)

        plt.figure()
        lw = 2
        plt.plot(fpr, tpr, color='darkorange',
                lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
        plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(titleCurve)
        plt.legend(loc="lower right")
        plt.savefig("./images/" +fileTitle + '.png')
        plt.clf()
        
    return rf

