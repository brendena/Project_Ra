import numpy as np

def getId(idPresent=False ,subset=-1, addSunRoof=False):
    allId = np.asarray(['ethnicity', 'marital_status', 'owner_type', 
                        'gender', 'use', 'age', 'bld_val', 'credit_rating', 
                        'year_built', 'roof_age','computers', 
                        'consumer_electronics', 'frequent_remodeler'])

    if(subset > 0):
        
        listCatiorgories = np.random.choice(len(allId), subset, replace=False)
        
        allId = allId[listCatiorgories] 
    elif(subset == 0 ):
        allId = []

    if(addSunRoof == True):
        allId = np.append(allId,["sqFtRoof","hoursSun"] )

    if(idPresent == True):
        allId = np.append(allId, ["id"])
        
    return allId

