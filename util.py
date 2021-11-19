from sklearn.metrics import accuracy_score, precision_score, recall_score, log_loss, confusion_matrix, plot_confusion_matrix, f1_score, roc_auc_score
import matplotlib.pyplot as plt
import numpy as np

def evaluate_model(model, X, y, plot_cf):
    '''
    Compute summary metrics for classifier models.
    Returns accuracy, precision, recall, and F1 score.
    Prints each of those metrics plus ROC score.

    Parameters
    ----------
    model: classifer model that has been train on X and y already
    X: Independent variable dataframe
    y: Target variable array
    plot_cf: boolean. If true, plots confusion matrix.

    Returns
    -------
    Prints Accuracy, Precision, Recall, F1, and ROC scores
    Returns Accuracy, Precision, Recall, and F1
    '''

    y_preds = model.predict(X)

    acc_score = accuracy_score(y, y_preds)
    precision = precision_score(y, y_preds)
    recall = recall_score(y, y_preds)
    f1 = f1_score(y, y_preds)
    try:
        roc = roc_auc_score(y, model.decision_function(X))
    except AttributeError:
        roc = np.nan

    print(f"Accuracy: {acc_score:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"ROC: {roc:.4f}")

    if plot_cf == True:
        fig, ax = plt.subplots()
        ax.grid(False)
        
        plot_confusion_matrix(model, X, y, ax=ax)


    return acc_score, precision, recall, f1