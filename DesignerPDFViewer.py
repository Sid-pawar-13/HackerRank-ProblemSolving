import numpy as np
import random
import string
def designerPdfViewer(h, word):
    print(h,word)
    size = [int(i) for i in h]
    words = [size[ord(c)-ord('a')] for c in word]
    return max(words)*len(words)

print(designerPdfViewer(np.random.randint(7,size=26),
      ''.join(random.choice(string.ascii_lowercase) for i in range(10))))
