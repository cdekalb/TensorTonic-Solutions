import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
        return np.array([0, 0], dtype=int)
    
    if max_len == None:
        max_len = max(len(seq) for seq in seqs)

    output = np.full((len(seqs), max_len), pad_value)
    
    for i, seq in enumerate(seqs):
        length = min(len(seq), max_len)
        output[i, :length] = seq[:length]

    return output
