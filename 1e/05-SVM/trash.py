"""
## Try labeling `A` and `B`
Another good way is to label `A` and `B` and see what will happen.

By labeling `A` and `B`, we mean
- Label them
  - either `A, B` as `0, 1`
  - or `A, B` as `1, 0`
- Train SVM on the entire dataset including `A` and `B`



In this case we have few data, and we don't have the labels for the points `A` and `B`, even though it does
seem to make sense to scale the feature in this case.

Let's take a real, larger example and compare the results of SVM w/ and w/o feature scaling.


> _SVMs are particularly well suited for classification of complex but **small- or medium**-sized
datasets._

**(?1)** Why small- and medium-sized datasets only? Why is it better to use DL for large-sized
dataset and how large does Mr. Geron mean by large?


**(?2)** Mr. Geron emphasized the importance of feature scaling before doing linear SVM.
In Figure 5-1, we do see that the lines seem to have different slopes,
but are they **_only so visually_** or **_numerically they are indeed of quite different slope values_**?

There is difference in the magnitude of the slopes before and after scaling.

Let's try to find a point
- which is classified safely as square magenta point on the left
- and which causes trouble by crossing the decision boundary towards the blue circular point territory on the right.

"""
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt



Xs = np.array([[1, 50], [5, 20], [3, 80], [5, 60]]).astype(np.float64)
ys = np.array([0, 0, 1, 1])
svm_clf = SVC(kernel="linear", C=100)
svm_clf.fit(Xs, ys)

plt.figure(figsize=(12,3.2))
plt.subplot(121)
plt.plot(Xs[:, 0][ys==1], Xs[:, 1][ys==1], "bo")
plt.plot(Xs[:, 0][ys==0], Xs[:, 1][ys==0], "ms")
plot_svc_decision_boundary(svm_clf, 0, 6)
plt.xlabel("$x_0$", fontsize=20)
plt.ylabel("$x_1$  ", fontsize=20, rotation=0)
w0, w1 = svm_clf.coef_
slope = - w0/w1
plt.title(f"decision boundary slope = {slope}", fontsize=16)
plt.axis([0, 6, 0, 90])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(Xs)
svm_clf.fit(X_scaled, ys)

plt.subplot(122)
plt.plot(X_scaled[:, 0][ys==1], X_scaled[:, 1][ys==1], "bo")
plt.plot(X_scaled[:, 0][ys==0], X_scaled[:, 1][ys==0], "ms")
plot_svc_decision_boundary(svm_clf, -2, 2)
plt.xlabel("$x_0$", fontsize=20)
w0, w1 = svm_clf.coef_
slope = - w0/w1
plt.title(f"decision boundary slope = {slope}", fontsize=16)
#plt.title("Scaled", fontsize=16)
plt.axis([-2, 2, -2, 2])



def plot_svc_decision_boundary(svm_clf, xmin, xmax):
    w = svm_clf.coef_[0]
    b = svm_clf.intercept_[0]

    # At the decision boundary, w0*x0 + w1*x1 + b = 0
    # => x1 = -w0/w1 * x0 - b/w1
    x0 = np.linspace(xmin, xmax, 200)
    decision_boundary = -w[0]/w[1] * x0 - b/w[1]

    margin = 1/w[1]
    gutter_up = decision_boundary + margin
    gutter_down = decision_boundary - margin

    svs = svm_clf.support_vectors_
    plt.scatter(svs[:, 0], svs[:, 1], s=180, facecolors='#FFAAAA')
    plt.plot(x0, decision_boundary, "k-", linewidth=2)
    plt.plot(x0, gutter_up, "k--", linewidth=2)
    plt.plot(x0, gutter_down, "k--", linewidth=2)

xA = 5.7
yA = Xs[0][1] + slope*(xA - Xs[0][0])
A = [xA, yA]
xB = 0.2
yB = Xs[-1][1] + slope*(xB - Xs[-1][0])
B = [xB, yB]
extra_data = np.array([A, B]).astype(np.float64)


another_svm_clf = SVC(kernel="linear", C=100)
X_aug_scaled = scaler.fit_transform(X_aug)
X_aug_scaled

another_svm_clf = SVC(kernel="linear", C=100)
another_svm_clf.fit(X_aug, y_aug)



another_svm_clf = SVC(kernel="linear", C=100)
another_svm_clf.fit(X_aug, y_aug)
plt.figure(figsize=(12,3.2))
plt.subplot(121)
plt.plot(X_aug[:, 0][y_aug==1], X_aug[:, 1][y_aug==1], "bo")
plt.plot(X_aug[:, 0][y_aug==0], X_aug[:, 1][y_aug==0], "ms")
plot_svc_decision_boundary(another_svm_clf, 0, 6)
plt.xlabel("$x_0$", fontsize=20)
plt.ylabel("$x_1$  ", fontsize=20, rotation=0)
w0, w1 = another_svm_clf.coef_[0]
slope = - w0/w1
plt.title(f"slope = {slope:.4f}", fontsize=16)
plt.axis([0, 6, 0, 90]);

another_svm_clf.fit(X_aug_scaled, y_aug)
plt.subplot(122)
plt.plot(X_aug_scaled[:, 0][y_aug==1], X_aug_scaled[:, 1][y_aug==1], "bo")
plt.plot(X_aug_scaled[:, 0][y_aug==0], X_aug_scaled[:, 1][y_aug==0], "ms")
plot_svc_decision_boundary(another_svm_clf, -2, 2)
plt.xlabel("$x_0$", fontsize=20)
w0, w1 = another_svm_clf.coef_[0]
scaled_slope = - w0/w1
plt.title(f"slope = {scaled_slope:.4f}", fontsize=16)
plt.axis([-2, 2, -2, 2]);


from sklearn import datasets
iris = datasets.load_iris()
X = iris["data"][:, [2,3]]
y = iris["target"]
X.shape, y.shape

X[:,1] = petal_width*(1e+4)


svm_clf.fit(X, y)
plt.figure(figsize=(12,3.2))
plt.subplot(121)
plt.plot(X[:, 0][y==1], X[:, 1][y==1], "bs")
plt.plot(X[:, 0][y==0], X[:, 1][y==0], "yo")
plot_svc_decision_boundary(svm_clf, 0, 6)
plt.xlabel("petal length", fontsize=20)
plt.ylabel("petal width", fontsize=20, rotation=0)
w0, w1 = svm_clf.coef_[0]
slope = - w0/w1
plt.title(f"slope (right scale) = {slope:.4f}", fontsize=16)
plt.axis([0, 6, 0, 90])

svm_clf.fit(X_wrong_scale, y)

plt.subplot(122)
plt.plot(X_wrong_scale[:, 0][y==1], X_wrong_scale[:, 1][y==1], "bs")
plt.plot(X_wrong_scale[:, 0][y==0], X_wrong_scale[:, 1][y==0], "yo")
plot_svc_decision_boundary(svm_clf, -2, 2)
#plt.xlabel("$x_0$", fontsize=20)
plt.xlabel("petal length", fontsize=20)
plt.ylabel("petal width", fontsize=20, rotation=0)
w0, w1 = scaled_svm_clf.coef_[0]
scaled_slope = - w0/w1
plt.title(f"slope (wrong scale) = {scaled_slope:.4f}", fontsize=16)
plt.axis([-2, 2, -2, 2]);




svm_clf.fit(X, y)
plt.figure(figsize=(13.7,3.2))
plt.subplot(121)
plt.plot(X[:, 0][y==1], X[:, 1][y==1], "bs")
plt.plot(X[:, 0][y==0], X[:, 1][y==0], "yo")
plot_svc_decision_boundary(svm_clf, 0, 5.5)
plt.xlabel("petal length (cm)", fontsize=20)
plt.ylabel("petal width (cm)", fontsize=20)
w0, w1 = svm_clf.coef_[0]
slope = - w0/w1
plt.title(f"slope (same scale) = {slope:.4f}", fontsize=16)
plt.axis([0, 5.5, 0, 2])

svm_clf.fit(X_diff_scale, y)

plt.subplot(122)
plt.plot(X_diff_scale[:, 0][y==1], X_diff_scale[:, 1][y==1], "bs")
plt.plot(X_diff_scale[:, 0][y==0], X_diff_scale[:, 1][y==0], "yo")
plot_svc_decision_boundary(svm_clf, 0, 5.5)
#plt.xlabel("$x_0$", fontsize=20)
plt.xlabel("petal length (cm)", fontsize=20)
plt.ylabel("petal width (mm)", fontsize=20)
w0, w1 = svm_clf.coef_[0]
scaled_slope = - w0/w1
plt.title(f"slope (diff scale) = {scaled_slope:.4f}", fontsize=16)
plt.axis([0, 5.5, 0, 3e+4]);
