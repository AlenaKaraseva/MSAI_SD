from sklearn.utils import shuffle
from sklearn import datasets
from sklearn.model_selection import train_test_split  
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

class Builder:
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
        
    def get_subsample(self, df_share):       
        data = self.X_train.copy()
        target = self.y_train.copy()
        
        data, target = shuffle(data, target, random_state=0)
        
        subsample = len(target) * df_share // 100
        return data[ : subsample, :], target[ : subsample]
                
        """
        1. Copy train dataset
        2. Shuffle data (don't miss the connection between X_train and y_train)
        3. Return df_share %-subsample of X_train and y_train
        """

if __name__ == "__main__":
    
    dataset = datasets.load_iris()        
    X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2, random_state=0, shuffle=True)
        
    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    """

    pattern_item = Builder(X_train, y_train)
    for df_share in range(10, 101, 10):
        curr_X_train, curr_y_train = pattern_item.get_subsample(df_share)
        
        pipe = make_pipeline(
            StandardScaler(),
            LinearRegression()
        )
        
        pipe.fit(curr_X_train, curr_y_train)
        print(f'For df_share = {df_share}, score is {pipe.score(X_test, y_test)}')
       
        """
        1. Preprocess curr_X_train, curr_y_train in the way you want
        2. Train Linear Regression on the subsample
        3. Save or print the score to check how df_share affects the quality
        """
