from sklearn import metrics

def model(model,X_tr,y_tr,X_te,y_te):
    model.fit(X_tr,y_tr)
    print('The accuracy is:',model.score(X_te,y_te))
    metrics.plot_confusion_matrix(model,X_te,y_te,cmap = 'Blues' )
    metrics.plot_roc_curve(model, X_te,y_te)
