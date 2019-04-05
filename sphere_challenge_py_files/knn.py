from sklearn.neighbors import NearestNeighbors

import numpy as np

"""
Define a simple class that inherits from sklearn.neighbors.NearestNeighbors. 
We will adjust the fit/predict as necessary
"""
class ProbabilisticKNN(NearestNeighbors): 
    def __init__(self, n_neighbors): 
        super(ProbabilisticKNN, self).__init__(n_neighbors)
        
        self.train_y = None
        
    def fit(self, train_x, train_y): 
        """
        The fit function requires both train_x and train_y. 
        See 'The selected model' section above for explanation
        """
        self.train_y = np.copy(train_y)
        
        super(ProbabilisticKNN, self).fit(train_x)
        
    def predict_proba(self, test_x): 
        """
        This function finds the k closest instances to the unseen test data, and 
        averages the train_labels of the closest instances. 
        """
        
        # Find the nearest neighbours for the test set
        test_neighbours = self.kneighbors(test_x, return_distance=False)
        
        # Average the labels of these for prediction
        return np.asarray(
            [self.train_y[inds].mean(0) for inds in test_neighbours]
        )

# # Learn the KNN model 
# nn = ProbabilisticKNN(n_neighbors=11)
# nn.fit(train_x, train_y)

# # Predict on the test instances
# test_predicted = nn.predict_proba(test_x)
# test_predicted