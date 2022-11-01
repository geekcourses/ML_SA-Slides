def plot_classification(self):
    h = .02
    n_neighbors = 9
    self.X = self.X.values[:10, [1,4]] #trim values to 10 entries and only columns 2 and 5 (indices 1, 4)
    self.y = self.y[:10, ] #trim outcome column, too

    clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
    clf.fit(self.X, self.y)

    x_min, x_max = self.X[:, 0].min() - 1, self.X[:, 0].max() + 1
    y_min, y_max = self.X[:, 1].min() - 1, self.X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]) #no errors here, but it's  not moving on until computer crashes

    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA','#00AAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00','#00AAFF'])
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    plt.scatter(self.X[:, 0], self.X[:, 1], c=self.y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("Classification (k = %i)" % (n_neighbors))