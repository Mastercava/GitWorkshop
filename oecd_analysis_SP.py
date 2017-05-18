import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

oecd_df = pd.read_csv('./Data/oecd-countries.csv')


# Select variables that would be plotted on the X and Y axis as well as the size of the points
X = 'WorkingLongHours'
Y = 'LifeExpectancy'
S = 'TimeDevotedToLeisure'

fig1, ax1 = plt.subplots()
ax1.scatter(oecd_df[X], oecd_df[Y], s=oecd_df[S] * 10)

# Add annotation (country name) to each point in the scatter plot
for i, txt in enumerate(oecd_df.Country):
    ax1.annotate(txt, (oecd_df[X][i], oecd_df[Y][i]))

ax1.set_xlabel(X)
ax1.set_ylabel(Y)
ax1.set_title('Scatter Plot')

# Perform PCA on the feature space and plot the first to principal components
feature_original = np.array(oecd_df.ix[:,1:])
labels = oecd_df.Country

pca = PCA(n_components=2)
pca.fit(feature_original)
features_pca = pca.transform(feature_original)

fig2, ax2 = plt.subplots()

ax2.scatter(features_pca[:,0], features_pca[:,1])

# Add annotation (country name) to each point in the scatter plot
for i, txt in enumerate(oecd_df.Country):
    ax2.annotate(txt, (features_pca[i,0], features_pca[i,1]))

ax2.set_xlabel('1st Principal Component')
ax2.set_ylabel('2nd Principal Component')
ax2.set_title('PCA Plot')

plt.show()