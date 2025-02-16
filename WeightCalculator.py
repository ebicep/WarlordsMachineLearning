import pandas as pd
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from tabulate import tabulate


class WeightCalculator:
    def __init__(self, df_functions, min_plays=10, polynomial_degree=1):
        self.df_functions = df_functions
        self.min_plays = min_plays
        self.polynomial_degree = polynomial_degree

    def train(self, df: DataFrame, print_table: bool = False):
        name = ""
        for consumer in self.df_functions:
            df = consumer(df)
            name += consumer.__name__ + " + "

        df = df[df["plays"] >= self.min_plays].copy()
        df.loc[:, "winrate"] = df["wins"] / df["plays"]
        df.drop(columns=["name", "wins", "plays"], inplace=True)

        X = df.drop(columns=["winrate"])
        y = df.loc[:, "winrate"]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        if self.polynomial_degree > 1:
            model = make_pipeline(
                PolynomialFeatures(degree=self.polynomial_degree),
                LinearRegression()
            )
        else:
            model = LinearRegression()

        # 5-fold cross-validation
        kf = KFold(n_splits=5, shuffle=True, random_state=42)
        mse_scores = -cross_val_score(model, X_scaled, y, cv=kf, scoring='neg_mean_squared_error')
        r2_scores = cross_val_score(model, X_scaled, y, cv=kf, scoring='r2')

        results = ""
        results += f"\n{name[:-3]}:" + "\n"
        results += f"- 5-Fold Cross-Validation Mean Squared Error (MSE): {mse_scores.mean():.4f} (±{mse_scores.std():.4f})" + "\n"
        results += f"- 5-Fold Cross-Validation R-squared (R2): {r2_scores.mean():.4f} (±{r2_scores.std():.4f})" + "\n"

        # Train the model on the full training set
        model.fit(X_train, y_train)

        # Evaluate on the test set
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        results += f"\nTest Set Performance:" + "\n"
        results += f"- Mean Squared Error (MSE): {mse:.4f}" + "\n"
        results += f"- R-squared (R2): {r2:.4f}" + "\n"

        if self.polynomial_degree > 1:
            # Get the names of the polynomial features
            poly_feature_names = model.named_steps['polynomialfeatures'].get_feature_names_out(X.columns)
            coef_pairs = list(zip(poly_feature_names, model.named_steps['linearregression'].coef_))
            intercept = model.named_steps['linearregression'].intercept_
        else:
            # For linear regression (no polynomial features)
            coef_pairs = list(zip(X.columns, model.coef_))
            intercept = model.intercept_

        # Weights
        sorted_coef_pairs = sorted(coef_pairs, key=lambda x: abs(x[1]), reverse=True)

        results += "\n- Coefficients (sorted by absolute value):" + "\n"
        for feature, coef in sorted_coef_pairs:
            results += f"  - {feature}: {coef:.4f}" + "\n"

        results += f"- Intercept: {intercept:.4f}" + "\n"

        if print_table:
            results += tabulate(X, headers='keys', tablefmt='psql') + "\n"

        return mse, r2, model, results

    def train_best(self, df: DataFrame, print_table: bool = False):
        r = []
        for _ in range(5):
            mse, r2, trained_model, results = self.train(df, print_table=print_table)
            r.append({"mse": mse, "r2": r2, "model": trained_model, "results": results})

        # Pick the best model based on MSE
        best_run = min(r, key=lambda x: x["mse"])
        print(best_run["results"])
