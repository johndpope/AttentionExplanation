def isTrue(obj, attr) :
    return hasattr(obj, attr) and getattr(obj, attr)

import torch

def masked_softmax(tensor, mask, dim=-1) :
    # tensor : (x1, x2, x3, ..., xn) Tensor
    # mask : (x1, x2, x3, ..., xn) LongTensor containing 1/0 
    #        where 1 if element to be masked else 0
    # dim : dimension over which to do softmax
    tensor.masked_fill_(mask.long(), -float('inf'))
    return torch.nn.Softmax(dim=dim)(tensor)

import numpy as np
def get_sorting_index_with_noise_from_lengths(lengths, noise_frac) :
    if noise_frac > 0 :
        noisy_lengths = [x + np.random.randint(np.floor(-x*noise_frac), np.ceil(x*noise_frac)) for x in lengths]
    else :
        noisy_lengths = lengths
    return np.argsort(noisy_lengths)