"""
Dataset Preprocessing Pipeline
"""

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler


class PreprocessingPipeline:
    def __init__(self):

        self.imputer = None
        self.scaler = None

    def impute_mean(self, dataframe):

        self.imputer = SimpleImputer(strategy="mean")

        dataframe[:] = self.imputer.fit_transform(dataframe)

        return dataframe

    def impute_median(self, dataframe):

        self.imputer = SimpleImputer(strategy="median")

        dataframe[:] = self.imputer.fit_transform(dataframe)

        return dataframe

    def standardize(self, dataframe):

        self.scaler = StandardScaler()

        dataframe[:] = self.scaler.fit_transform(dataframe)

        return dataframe

    def normalize(self, dataframe):

        self.scaler = MinMaxScaler()

        dataframe[:] = self.scaler.fit_transform(dataframe)

        return dataframe

    def remove_duplicates(self, dataframe):

        return dataframe.drop_duplicates()

    def remove_missing(self, dataframe):

        return dataframe.dropna()

    def pipeline(self, dataframe, impute=True, scale=True):

        df = dataframe.copy()

        if impute:
            df = self.impute_mean(df)

        if scale:
            df = self.standardize(df)

        return df
