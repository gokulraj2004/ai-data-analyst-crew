from agents.data_cleaner_agent import DataCleanerAgent

if __name__ == "__main__":
    cleaner = DataCleanerAgent()

    df = cleaner.clean_data("data/raw/sample_sales_data.csv")
    cleaner.save_cleaned_data(df, "data/processed/cleaned_sales_data.csv")

    print("✅ Data cleaning completed successfully")
