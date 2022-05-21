import pandas as pd
from sklearn import cluster, compose, metrics, preprocessing


class Clustering:
    def __init__(self, target: str) -> None:
        self.target = target
        self.contrato_id = None
        self.nr_documento = None
        self.preprop_df = self.set_data()

    def set_data(self):
        df = pd.read_csv("data/to_analysis.csv")

        # preprocessing
        # we need to drop columns with proportions, because
        # of those missings
        prop_columns = [column for column in df.columns if column.startswith("prop_")]

        df.drop(prop_columns, axis=1, inplace=True)

        if self.target == "dsp":
            dspp_columns = [column for column in df.columns if "dspp" in column]
            df.drop(dspp_columns, axis=1, inplace=True)
            df.dropna(subset=["score_dsp", "('qtd_transacoes', 'mean')"], inplace=True)
        elif self.target == "dspp":
            dsp_columns = [column for column in df.columns if "dsp" in column]
            df.drop(dsp_columns, axis=1, inplace=True)
            df.dropna(subset=["score_dspp", "('qtd_transacoes', 'mean')"], inplace=True)

        self.contrato_id = df["contrato_id"].to_list()
        self.nr_documento = df["nr_documento"].to_list()

        df.drop(["contrato_id", "nr_documento"], axis=1, inplace=True)

        return df

    def remove_unused_categories(self) -> None:
        categorical_variables = self.preprop_df.select_dtypes(include=object).columns

        new_categorical_variables = [
            feature + "_new" for feature in categorical_variables
        ]
        df = self.preprop_df.copy()

        for i, feature in enumerate(categorical_variables):
            df[new_categorical_variables[i]] = df[feature].apply(
                lambda x: None if len(x.split(",")) > 1 else x
            )

        df.drop(categorical_variables, axis=1, inplace=True)
        df.dropna(subset=new_categorical_variables, inplace=True)

        self.preprop_df = df.copy()

    def frequency_encoding(self, feature: str):
        df = self.preprop_df.copy()

        frq_encoder = (df.groupby([feature]).size()) / len(df)
        df[feature + "_enc"] = df[feature].apply(lambda x: frq_encoder[x])

        df.drop([feature], axis=1, inplace=True)

        self.preprop_df = df.copy()

    def create_pipeline(self):
        categorical_selector = compose.make_column_selector(dtype_include=object)
        categorical_columns = categorical_selector(self.preprop_df)

        numerical_selector = compose.make_column_selector(dtype_exclude=object)
        numerical_columns = numerical_selector(self.preprop_df)

        ohe_preprocessor = preprocessing.OneHotEncoder(sparse=False)
        std_preprocessor = preprocessing.StandardScaler()

        preprocessor = compose.ColumnTransformer(
            [
                ("ohe_preprocessor", ohe_preprocessor, categorical_columns),
                ("std_preprocessor", std_preprocessor, numerical_columns),
            ]
        )

        df_transformed = preprocessor.fit_transform(self.preprop_df)

        clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10]

        score_lst = []
        for n_cluster in clusters:
            cluster_kmeans = cluster.KMeans(n_clusters=n_cluster).fit(df_transformed)
            preds = cluster_kmeans.predict(df_transformed)
            # centers = cluster_kmeans.cluster_centers_
            score = metrics.silhouette_score(df_transformed, preds, metric="euclidean")
            score_lst.append(
                metrics.silhouette_score(df_transformed, preds, metric="euclidean")
            )
            print(
                "For n cluster: {}. The avg silhouette_score is {}".format(
                    n_cluster, score
                )
            )
