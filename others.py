import torch
import numpy as np
from sklearn import metrics

@torch.no_grad()
def get_grad_norm(parameters, norm_type=2):
    parameters = list(filter(lambda p: p.grad is not None, parameters))
    total_norm = 0
    
    try:
        for p in parameters:
            total_norm += (p.grad.data**norm_type).sum()
        total_norm = total_norm ** (1. / norm_type)
    except Exception as e:
        print(e)
    
    return total_norm

@torch.no_grad()
def get_parameter_norm(parameters, norm_type=2):
    total_norm = 0

    try:
        for p in parameters:
            total_norm += (p.data**norm_type).sum()
        total_norm = total_norm ** (1. / norm_type)
    except Exception as e:
        print(e)

    return total_norm

def get_accuracy(y_pred, y_true):
    y_pred = torch.sigmoid(y_pred).to("cpu").detach().numpy().tolist()
    y_pred = np.array(y_pred) >= .5
    y_true = y_true.to("cpu").detach().numpy().tolist()
    
    # accuracy = metrics.accuracy_score(y_true, y_pred)        
    # f1_score_micro = metrics.f1_score(y_true, y_pred, average='micro')
    f1_score_macro = metrics.f1_score(y_true, y_pred, average='macro')
    # hamming_score = metrics.hamming_loss(y_true, y_pred)
    
    return {
        # "accuracy": accuracy,
        # "f1_score_micro": f1_score_micro,
        "f1_score_macro": f1_score_macro,
        # "hamming_score": hamming_score
    }