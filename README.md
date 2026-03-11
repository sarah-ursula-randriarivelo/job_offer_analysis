# Job Analyser

## Description

This project is a comprehensive job offer analysis pipeline that processes job posting data through multiple stages: data loading, cleaning, skill extraction, analysis, and visualization. It uses Python and Jupyter notebooks to transform raw job offer data into insights about job market trends, required skills, and more.

## Project Structure

- `step_01_data_loader.ipynb`: Loads job offer data from CSV files in the datasets folder.
- `step_02_cleaning.ipynb`: Cleans the data by removing duplicates, handling missing values, and preprocessing text.
- `step_03_skill_extraction.ipynb`: Extracts relevant skills from job descriptions using natural language processing techniques.
- `step_04_skill_analysis.ipynb`: Performs analysis on the processed data, especially for the skills like the the most common skills in job offers, an aggregated view of skills per category  .
- `step_05_job_offer_visualization.ipynb`: Performs data visualization to analyze insigths in the datasets. 

- `datasets/`: Directory containing CSV files with job offer data at various processing stages:
  - `job_offer.csv`: Raw job offer data
  - `job_offer_no_duplicate.csv`: Data after duplicate removal
  - `job_offer_cleaned.csv`: Cleaned data
  - `job_offer_with_skills.csv`: Data with extracted skills
- `modules/`: Custom Python modules:
  - `stopword.py`: Contains custom stopwords for text processing
- `requirements.txt`: List of Python dependencies required for the project.

## Installation

1. Ensure you have Python installed (version 3.8 or higher recommended).
2. Clone or download this repository to your local machine.
3. Navigate to the project directory.
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Launch Jupyter Notebook or JupyterLab:
   ```
   jupyter notebook
   ```

## Usage

1. Open the Jupyter notebooks in the following order:
   - Start with `step_01_data_loader.ipynb`
   - Follow with `step_02_cleaning.ipynb`
   - Follow with`step_03_skill_extraction.ipynb`
   - Then `step_04_job_offer_analysis.ipynb`
   - Finally `step_05_job_offer_visualization.ipynb`

2. Execute the cells in each notebook sequentially. Each step builds upon the previous one.

3. The processed data will be saved as CSV files in the `datasets/` folder for use in subsequent steps.

## Dependencies

The project requires the following Python packages:

- pandas==3.0.0 (Data manipulation and analysis)
- numpy==2.4.2 (Numerical computing)
- matplotlib>=3.8.0 (Static plotting)
- jupyter>=1.0.0 (Jupyter notebook environment)
- ipykernel>=6.25.0 (Jupyter kernel)
- notebook>=7.0.0 (Jupyter notebook server)

## Features

- **Data Loading**: Efficiently loads large datasets of job offers
- **Analysis**: Provides insights through statistical analysis and visualizations

