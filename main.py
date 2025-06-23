import sys
import os

# Add 'src/' directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

# Now import from the actual location
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

if __name__ == "__main__":
    obj = DataIngestionTrainingPipeline()
    obj.main()
