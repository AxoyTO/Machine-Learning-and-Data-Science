import numpy as np


class MinMaxScaler:
    def __init__(self):
        self.maxes = []
        self.mins = []

    def fit(self, data):
        """Store calculated statistics
        Parameters:
        data (np.array): train set, size (num_obj, num_features)
        """

        # print(data.shape)
        self.maxes = data.max(axis=0)
        self.mins = data.min(axis=0)

        pass

    def transform(self, data):
        """
        Parameters:
        data (np.array): train set, size (num_obj, num_features)
        Return:
        np.array: scaled data, size (num_obj, num_features)
        """
        print(data)
        cols = data.shape[1]
        for i in range(cols):
            v = data[:, i]
            data[:, i] = (v - self.mins[i]) / (self.maxes[i] - self.mins[i])
        return data
        pass


class StandardScaler:
    def __init__(self):
        self.deviation = []
        self.expected_val = []

    def fit(self, data):
        """Store calculated statistics
        Parameters:
        data (np.array): train set, size (num_obj, num_features)
        """

        prob = 1 / data.shape[0]
        for i in range(data.shape[1]):
            sum = 0
            for j in data[:, i]:
                sum += j * prob
            self.expected_val.append(sum)

        self.deviation = data.std(axis=0)
        # print("E: ", self.expected_val)
        # print("D: ", self.deviation)
        pass

    def transform(self, data):
        """
        Parameters:
        data (np.array): train set, size (num_obj, num_features)

        Return:
        np.array: scaled data, size (num_obj, num_features)
        """
        transformed = np.zeros(shape=data.shape)
        # print("---------------------------------")
        for i in range(data.shape[1]):
            for j in range(data.shape[0]):
                transformed[j][i] = (data[j][i] - self.expected_val[i]) / self.deviation[i]
        #       print(data[j][i])
        #   print("---------------------------------")
        # print(transformed)
        return transformed
        pass
