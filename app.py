from agents.data_cleaner_agent import DataCleanerAgent

if __name__ == "__main__":
    cleaner = DataCleanerAgent()

    df = cleaner.clean_data("data/raw/sample_sales_data.csv")
    cleaner.save_cleaned_data(df, "data/processed/cleaned_sales_data.csv")

    summary = cleaner.generate_ai_summary()
    cleaner.save_data_quality_report(
        summary,
        "data/processed/data_quality_report.txt"
    )

    print("✅ Gemini-powered data cleaning completed")
