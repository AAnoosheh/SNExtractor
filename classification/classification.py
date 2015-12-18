from sklearn.svm import SVC
from sklearn.preprocessing import normalize
from sklearn.externals import joblib

from numpy import vstack


def train(data, labels, c=1.0, norm=False):
    data = vstack(data)
    if norm:
        data = normalize(data)

    model = SVC(C=c, class_weight='auto', probability=True)
    return model.fit(data, labels)

def predict(model, data):
    data = vstack(data)
    return model.fit_predict(data)


def save_model(model, filename):
    joblib.dump(model, filename+'.pkl')