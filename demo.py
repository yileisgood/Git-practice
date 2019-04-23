from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
clf = tree.DecisionTreeClassifier()
from sklearn.metrics import accuracy_score
# CHALLENGE - create 3 more classifiers...
# 1
randf = RandomForestClassifier()
# 2
neural = MLPClassifier(hidden_layer_sizes= 200,alpha= 1)
# 3
svm = SVC(kernel='linear',C = 0.025, gamma= 2 )
# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)
randf = randf.fit(X,Y)
svm = svm .fit(X,Y)
neural = neural.fit(X,Y)

prediction = clf.predict([[190, 70, 43]])
print('Random:',randf.predict([[190, 70, 43]]),accuracy_score(Y,randf.predict(X)),'\n',
      'Neural:',neural.predict([[190, 70, 43]]),accuracy_score(Y,neural.predict(X)),'\n',
      'SVM:',svm.predict([[190, 70, 43]]),accuracy_score(Y,svm.predict(X),'\n'))
# CHALLENGE compare their reusults and print the best onek!

print(prediction)
print()