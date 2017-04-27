import pandas as pd
import numpy as np
import re
from convertGoogleScraped import convertGoogleScraped
from JoinMerge import joinFiles, mergeData, getTrainingDataTestingData, getCVSConvertToData
from myId import getId
from treeRocCurve import createRocCurve#
import random


random.seed(100)


#convertGoogleScraped("./SeattleUpdated")



#'''
print("\n--------Tampa-----------\n ")
data = getTrainingDataTestingData("Tampa", "./googleSunroof/FL_TampaUpdated.csv")

print("testing validation set\n")
createRocCurve(data["trainX"], data["trainY"],data["testX"],data["testY"], "ROC Florida Tampa", "florida")
print("testing remaining just true set\n")
decisionTree = createRocCurve(data["trainX"], data["trainY"],data["testAcceptedRestX"],data["testAcceptedRestY"], "this is a cool image", "image",justCount=True)

getCVSConvertToData("./clean_data/cleaned_Tampa.csv", "./googleSunroof/FL_TampaUpdated.csv", decisionTree, "tampa")

#'''

#'''
print("\n--------Seattle-----------\n ")
data = getTrainingDataTestingData("Seattle", "./googleSunroof/SeattleUpdated.csv")

print("testing validation set\n")
createRocCurve(data["trainX"], data["trainY"],data["testX"],data["testY"], "ROC Seattle", "validationSeattle")
print("testing remaining just true set\n")
decisionTree = createRocCurve(data["trainX"], data["trainY"],data["testAcceptedRestX"],data["testAcceptedRestY"], "this is a cool image", "image",justCount=True)
getCVSConvertToData("./clean_data/cleaned_Seattle.csv",  "./googleSunroof/SeattleUpdated.csv", decisionTree, "seattle")
#'''

#'''
print("\n--------New York-----------\n ")
data = getTrainingDataTestingData("NewYork", "./googleSunroof/New_YorkUpdated.csv")

print("testing validation set\n")
createRocCurve(data["trainX"], data["trainY"],data["testX"],data["testY"], "ROC New York City", "ValidationNY")
print("testing remaining just true set\n")
decisionTree = createRocCurve(data["trainX"], data["trainY"],data["testAcceptedRestX"],data["testAcceptedRestY"], "ROC New York City", "NYTraining",justCount=True)

getCVSConvertToData("./clean_data/cleaned_NewYork.csv",  "./googleSunroof/New_YorkUpdated.csv", decisionTree, "New York")
#'''

'''
print("\n--------Tampa-Test-----------\n ")
data = getTrainingDataTestingData("Tampa", "./googleSunroof/FL_TampaUpdated.csv")

secondaryCity = getTrainingDataTestingData("Seattle", "./googleSunroof/SeattleUpdated.csv")

print("testing validation set\n")
createRocCurve(data["trainX"], data["trainY"],secondaryCity["testX"],secondaryCity["testY"], "ROC Tampa validated on New York Data", "newFlorida")
print("testing remaining just true set\n")
createRocCurve(data["trainX"], data["trainY"],secondaryCity["testAcceptedRestX"],secondaryCity["testAcceptedRestY"], "this is a cool image", "image",justCount=True)
#'''





























'''
for itteration in range(0,5):
    for i in range(1,12):
        #subSet
        s = getId()
        createRocCurve(data["trainX"][s], data["trainY"],data["testx"][s],data["testx"], "this is a cool image", str(itteration) + "_" + str(i) +" image")

        #createRocCurve(data["trainX"][s], data["trainY"],data["testAcceptedRestX"][s],data["testAcceptedRestY"], "this is a cool image", str(itteration) + "_" + str(i) +" image")

        s = np.append(s,["sqFtRoof","hoursSun"] )
        createRocCurve(data["trainX"][s], data["trainY"],data["testx"][s],data["testx"], "this is a cool image", str(itteration) + "_" + str(i) +" image")
'''