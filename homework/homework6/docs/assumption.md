## Preprocessing Assumptions

When we clean and preprocess data, every choice encodes assumptions about the dataset. It's important to document these for reproducibility and stakeholder understanding.

### 1. Missing Data Handling
- Filling missing numeric values with median assumes the missingness is **MCAR or MAR** (not systematically biased).  
- Forward/backward fill assumes **temporal continuity** in time series data.  
- Dropping rows assumes the missing rows are **not critical** to analysis.  
- Imputation affects averages, distributions, and model training.

### 2. Understanding Missingness
- MCAR: safe to drop or fill, assumes randomness.  
- MAR: imputation using related features is valid.  
- MNAR: missing depends on unobserved values; may require domain knowledge.  
- Misidentifying missingness can bias results.

### 3. Filtering / Data Cleaning
- Removing negative or out-of-range values assumes they are **errors or invalid entries**.  
- Dropping columns or rows with excessive missingness assumes those data are **non-essential**.  
- Rare but valid events might be lost if thresholds are too strict.

### 4. Scaling / Normalization
- StandardScaler assumes features are roughly **normally distributed**.  
- MinMaxScaler assumes min and max values are **representative**, not extreme outliers.  
- Scaling changes interpretation of magnitudes; coefficients or distances may be affected.

### 5. Column Type Corrections
- Converting strings to numeric assumes there are **no hidden characters or formatting issues**.  
- Parsing dates assumes a **consistent date format**.  
- Categoricals assume a **finite, discrete set of values**.  
- Wrong types can break computations or modeling.

### 6. Reproducibility & Modularity
- Using modular functions assumes **future datasets follow similar structure and patterns**.  
- Documenting assumptions ensures that preprocessing is **transparent** and results are interpretable.

> **Tip:** Always communicate these assumptions to stakeholders, so they understand the limitations and decisions made during preprocessing.
