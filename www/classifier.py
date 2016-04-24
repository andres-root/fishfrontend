
from sklearn import svm
from .models import Fish


class Classifier(object):

    def __init__(self):
        # data = Fish.objects.values('size', 'color', 'name')
        # self.X = []
        # self.y = []
        # for e in data:
        #     self.X.append([e['size'], e['color']])
        #     self.y.append(e['name'])
        self.X = [[10, 1], [11, 1], [2, 0], [9, 1], [6, 0], [9, 1], [6, 0], [5, 0], [2, 0], [12, 0], [10, 1], [14, 1]]
        self.y = ['mojarra', 'mojarra', 'bagre', 'mojarra', 'bagre', 'mojarra', 'bagre', 'bagre', 'bagre', 'bagre', 'mojarra', 'mojarra']
        self.clf = svm.SVC()

    def train(self):
        self.clf.fit(self.X, self.y)

    def classify(self, targets):
        if len(targets) == 0:
            return False
        else:
            self.train()
            return self.clf.predict([targets])[0]
