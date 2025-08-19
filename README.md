# Bootcamp Repository

## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.

## Project Folder Rules
- Keep project files organized and clearly named.

# Data Storage
## Folder Structure

The project uses the following data folder structure:

- **data/raw/** → Contains the original, unprocessed data files saved directly after creation.

- **data/processed/** → Stores the cleaned or validated data, and data saved using utility functions.

## Formats Used and Why

Two formats are used in this project:

- **CSV (.csv)** → Simple text format that is easy to read and compatible with many tools. Used for basic data exchange and inspection.

- **Parquet (.parquet)** → A binary columnar format, more efficient for large datasets in terms of storage and speed. Used when performance matters.

## Reading/Writing with Environment Variables

The project uses .env variables to configure data storage paths. These are loaded using dotenv, and fallback defaults are provided:

RAW = pathlib.Path(os.getenv("DATA_DIR_RAW", "data/raw"))
PROC = pathlib.Path(os.getenv("DATA_DIR_PROCESSED", "data/processed"))

This allows flexibility when changing storage locations without modifying the core code.
All data read/write operations use these variables to construct paths dynamically.


## Data Cleaning Strategy

This project includes a data preprocessing pipeline implemented in `src/cleaning.py`.

The following steps were applied to clean the dataset:

1. **Missing Value Handling**:
   - Numerical columns with missing values were filled using the **median**.
   - Remaining rows with missing values were dropped.

2. **Normalization**:
   - Min-max normalization was applied to numerical columns to scale values to the [0, 1] range.

3. **Modular Functions**:
   - Cleaning was done using reusable functions:
     - `fill_missing_median()`
     - `drop_missing()`
     - `normalize_data()`

4. **Outputs**:
   - Original data: `data/raw/sample_data.csv`
   - Cleaned data: `data/processed/cleaned_data.csv`

Assumptions and full details are documented in [`docs/assumption.md`](docs/assumption.md).