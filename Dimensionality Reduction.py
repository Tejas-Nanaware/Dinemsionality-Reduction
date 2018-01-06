from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

# import file
data = np.loadtxt("Book11.txt", delimiter='\t', skiprows=1)
# 0 Coding Skills
# 1 Aptitude Skills
# 2 Technical Skills
# 3 Communication Skills
# 4 Core Knowledge
# 5 Presentation Skills
# 6 Academic Performance
# 7 Puzzle Solving skills
# 8 English Proficiency
# 9 Programming Skills
# 10 Management Skills
# 11 Projects
# 12 Internships
# 13 Training
# 14 Backlog
# 15 Placed

# X Axis 0,2,7,9,11,12,13,14
# Y Axis 1,3,4,5,6,8,10,14

# Splitting data for averaging skills to represent in 3D
w1 = data[:,0]
w2 = data[:,1]
w3 = data[:,2]
w4 = data[:,3]
w5 = data[:,4]
w6 = data[:,5]
w7 = data[:,6]
w8 = data[:,7]
w9 = data[:,8]
w10 = data[:,9]
w11 = data[:,10]
w12 = data[:,11]
w13 = data[:,12]
w14 = data[:,13]
w15 = -10*data[:,14]
w16 = data[:,15]

# X Axis 0,2,7,9,11,12,13,14
# Y Axis 1,3,4,5,6,8,10,14
x = (w1 + w3 + w8 + w10 + w12 + w13 + w14 + w15)/8
y = (w2 + w4 + w5 + w6 + w7 + w9 + w11 + w15)/8
z = w16

# Show plot obtained by averaging
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
three_d = ax.scatter(x,y,z, marker='o', c=z, cmap='jet')
plt.colorbar(three_d)

ax.set_xlabel('Qualitative Skills in %')
ax.set_ylabel('Quantitative Skills in %')
ax.set_zlabel('Probability Of Placement in %')
ax.set_title('Average of Qualitative & Quantitative vs Probability of Placement')
plt.show()

# Implementing TSNE for plotting 16D data into 2D
X_embedded = TSNE(n_components=2).fit_transform(data[:,:])

plt.figure()
two_d_tsne = plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=z)
plt.colorbar(two_d_tsne)
plt.xlabel('Skills')
plt.ylabel('Probability of being placed')
plt.title('Represented Higher Dimensions to 2D using TSNE')
plt.show()

# Implementing PCA to reduce dimensions
pca = PCA(n_components=2)
pca_result = pca.fit_transform(data)

plt.figure()
two_d_pca = plt.scatter(pca_result[:, 0], pca_result[:, 1], c=z)
plt.colorbar(two_d_pca)
plt.xlabel('Skills')
plt.ylabel('Probability of being placed')
plt.title('Represented Higher Dimensions to 2D using PCA')
plt.show()