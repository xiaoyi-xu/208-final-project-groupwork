from sklearn.model_selection import cross_val_score

def kfold(model,X,y):
    
    accuracy= cross_val_score(model,X,y,scoring = 'accuracy',cv = 5)

    return accuracy.mean()
    
