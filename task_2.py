from scipy.stats import mode
from sklearn import datasets
from sklearn.model_selection import train_test_split  
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


class Facade:
    def __init__(self, classificators) -> None:
        self.classificators = classificators      
        
        """
        Initialize a class item with a list of classificators
        """

    def fit(self, data, target):
        for i in self.classificators:
            i.fit(data, target)
        
        """
        Fit classifiers from the initialization stage
        """

    def predict(self, data):       
        target_preds = []
        for i in self.classificators:
            target_preds.append(i.predict(data))
            
        # finding the mode
        mode_array = mode(target_preds)
        return mode_array[0][0]
        
        """
        Get predicts from all the classifiers and return
        the most popular answers
        """


if __name__ == "__main__":

    dataset = datasets.load_iris()  
    X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2, random_state=0, shuffle=True)
  
    classificators = [
        make_pipeline(
            StandardScaler(),
            SGDClassifier()),
        make_pipeline(
            StandardScaler(),
            KNeighborsClassifier(n_neighbors=3)),
        make_pipeline(
            StandardScaler(),
            SVC(kernel='linear')),
        make_pipeline(
            StandardScaler(),
            SVC(kernel='rbf')),
        make_pipeline(
            StandardScaler(),
            MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=0))
    ]
      
    ensemble = Facade(classificators)
    ensemble.fit(X_train, y_train)
    target_pred = ensemble.predict(X_test)
    print(f'Accuracy score: {accuracy_score(y_test, target_pred)}')
#     print(target_pred)
#     print(y_test)
       
    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    3. Prepare classifiers to initialize <StructuralPatternName> class.
    4. Train the ensemble
    """
