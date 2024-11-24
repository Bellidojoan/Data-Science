import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
file_path = '../results/quality_of_moves.csv'
data = pd.read_csv(file_path)

# Create the img directory if it doesn't exist
output_dir = "../img"
os.makedirs(output_dir, exist_ok=True)

# Define Elo categories
def classify_elo_category(elo):
    if elo <= 1200:
        return "Low"
    elif 1200 < elo <= 1600:
        return "Intermediate"
    elif 1600 < elo <= 2000:
        return "Advanced"
    else:
        return "Expert"

# Classify Elo categories
data['AvgElo'] = (data['WhiteElo'] + data['BlackElo']) / 2
data['EloCategory'] = data['AvgElo'].apply(classify_elo_category)

# Ensure EloCategory has the correct order
category_order = ['Expert', 'Advanced', 'Intermediate', 'Low']
data['EloCategory'] = pd.Categorical(data['EloCategory'], categories=category_order, ordered=True)

# Analyze proportions by GameMode and EloCategory
# Group data by GameMode and EloCategory
grouped_data = data.groupby(['GameMode', 'EloCategory'])[['good', 'inaccuracy', 'mistake', 'blunder']].sum()

# Calculate proportions for each category within each GameMode and EloCategory
proportions_by_mode = grouped_data.div(grouped_data.sum(axis=1), axis=0).reset_index()

# Visualize heatmaps by GameMode
for mode in ['Bullet', 'Blitz', 'Rapid']:
    mode_data = proportions_by_mode[proportions_by_mode['GameMode'] == mode].set_index('EloCategory')
    plt.figure(figsize=(10, 6))
    sns.heatmap(
        mode_data[['good', 'inaccuracy', 'mistake', 'blunder']],
        annot=False,
        fmt=".2f",
        cmap="YlGnBu",
        cbar_kws={'label': 'Proportion of Moves'}
    )
    plt.title(f'Move Quality Proportions ({mode})')
    plt.xlabel('Move Quality')
    plt.ylabel('Elo Category')
    plt.tight_layout()
    output_path = os.path.join(output_dir, f'heatmap-{mode.lower()}-moves.png')
    plt.savefig(output_path, dpi=300)
    print(f"Saved heatmap for {mode} to {output_path}")