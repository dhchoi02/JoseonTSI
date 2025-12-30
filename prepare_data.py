import os
import pandas as pd
from glob import glob

script_dir = os.path.dirname(os.path.abspath(__file__))

# Merge annals_articles
annals_dir = os.path.join(script_dir, 'annals_articles')
annals_files = sorted(glob(os.path.join(annals_dir, '*.csv')))
if annals_files:
    dfs = [pd.read_csv(f) for f in annals_files]
    annals_df = pd.concat(dfs, ignore_index=True)
    annals_df.to_csv(os.path.join(script_dir, 'annals_articles.csv'), index=False)
    print(f'Created annals_articles.csv: {len(annals_df):,} rows')

# Merge career_records
career_dir = os.path.join(script_dir, 'career_records')
career_files = sorted(glob(os.path.join(career_dir, '*.csv')))
if career_files:
    dfs = [pd.read_csv(f) for f in career_files]
    career_df = pd.concat(dfs, ignore_index=True)
    career_df.to_csv(os.path.join(script_dir, 'career_records.csv'), index=False)
    print(f'Created career_records.csv: {len(career_df):,} rows')
