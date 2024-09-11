# BigQuery benchmark repo

This repo is intended to run benchmark queries against BigQuery.

## Setup (to run locally)

### 1. Clone the repo
```shell
git clone https://github.com/voltrondata/benchmark-bigquery

```

### 2. Setup Python
Create a new Python 3.8+ virtual environment and install the requirements with:
```shell
cd benchmark-bigquery

# Create the virtual environment
python3 -m venv ./venv

# Activate the virtual environment
. ./venv/bin/activate

# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install the benchmark-bigquery package (in editable mode)
pip install --editable .

```

### 3. Create .env file in root of repo folder
Create a .env file in the root folder of the repo - it will be git-ignored for security reasons.   

Sample contents:
```text
export GOOGLE_PROJECT_ID="voltron-data-developers"
export DATASET_ID="voltron-data-developers.tpch_10"
```

### 4. Authenticate with Google Cloud
```shell
gcloud auth application-default login
```

## Running the benchmarks (with default settings)

```shell
benchmark-bigquery
```

Note: this will create a file in the [data](data) directory called: "benchmark_results.json" with the query run details.   

To see more options:
```shell
benchmark-bigquery --help
```

## Converting the benchmark JSON output data to Excel format
```shell
benchmark-bigquery-convert-output-to-excel
```

Note: this will create an Excel file in the [data](data) directory called: "benchmark_results.xlsx" with the query run details.
