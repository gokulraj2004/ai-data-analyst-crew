import pandas as pd

class DataCleanerAgent:
    def __init__(self):
        pass

    def load_data(self, file_path: str) -> pd.DataFrame:
        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            return pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")

    def clean_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )
        return df

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].fillna("unknown")
            else:
                df[col] = df[col].fillna(df[col].median())
        return df

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.drop_duplicates()

    def clean_data(self, file_path: str) -> pd.DataFrame:
        df = self.load_data(file_path)
        df = self.clean_column_names(df)
        df = self.handle_missing_values(df)
        df = self.remove_duplicates(df)
        return df

    def save_cleaned_data(self, df: pd.DataFrame, output_path: str):
        df.to_csv(output_path, index=False)
