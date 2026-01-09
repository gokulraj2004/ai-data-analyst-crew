import os
import pandas as pd
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class DataCleanerAgent:
    def __init__(self):
        # Report dictionary to track data quality actions
        self.report = {
            "missing_values": {},
            "duplicates_removed": 0,
            "column_types": {}
        }

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
            missing_count = int(df[col].isna().sum())
            if missing_count > 0:
                self.report["missing_values"][col] = missing_count

            if df[col].dtype == "object":
                df[col] = df[col].fillna("unknown")
            else:
                df[col] = df[col].fillna(df[col].median())

        return df

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        before = len(df)
        df = df.drop_duplicates()
        after = len(df)

        self.report["duplicates_removed"] = before - after
        return df

    def capture_schema(self, df: pd.DataFrame):
        for col in df.columns:
            self.report["column_types"][col] = str(df[col].dtype)

    def clean_data(self, file_path: str) -> pd.DataFrame:
        df = self.load_data(file_path)
        df = self.clean_column_names(df)
        df = self.handle_missing_values(df)
        df = self.remove_duplicates(df)
        self.capture_schema(df)
        return df

    def save_cleaned_data(self, df: pd.DataFrame, output_path: str):
        df.to_csv(output_path, index=False)

    def generate_ai_summary(self) -> str:
        prompt = f"""You are a senior data analyst.
            Explain the data cleaning actions taken in simple,
            business-friendly language.

            Cleaning details:
            - Missing values handled: {self.report["missing_values"]}
            - Duplicates removed: {self.report["duplicates_removed"]}
            - Final column data types: {self.report["column_types"]}

            Keep it concise and professional.
            """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    def save_data_quality_report(self, summary: str, path: str):
        with open(path, "w", encoding="utf-8") as f:
            f.write(summary)
