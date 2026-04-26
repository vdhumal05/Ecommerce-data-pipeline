import sys
import os

# scripts folder add to path
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))

from load import load

def run_pipeline():
    print("Starting ETL Pipeline...")
    load()
    print("Pipeline Completed ✅")

if __name__ == "__main__":
    run_pipeline()