# trendpulse-RamaKrishnaKiranAnnadevara

# TrendPulse — YourName

Four small Python scripts that implement a simple trending-data pipeline:

- `task1_data_collection.py` — fetches Google Trends via `pytrends` and saves `data/trendpulse.csv`
- `task2_data_processing.py` — cleans and smooths data, outputs `data/trendpulse_processed.csv`
- `task3_analysis.py` — computes top movers and correlations, saves CSV summaries
- `task4_visualization.py` — produces plots in `output/`

How to run locally

1. Create and activate a virtualenv, then install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the pipeline in order:

```bash
python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py
```

How to submit on GitHub

1. Create a public repo named `trendpulse-yourname` on GitHub.
2. Commit and push these files to the repo root.
3. Open each file in GitHub and copy the browser link; submit one link per task, e.g.:

```
https://github.com/<username>/trendpulse-yourname/blob/main/task1_data_collection.py
```

4. Confirm each link is public by opening it in an incognito window.
