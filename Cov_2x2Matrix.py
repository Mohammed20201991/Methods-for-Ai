import numpy as np
X= [9, 2, 5, 6, 2, 1, 5]
Y= [1, 5, 3, 6, 7, 1, 8]
Cov_matrix = np.stack((X,Y),axis= 0)
print(np.cov(Cov_matrix))
