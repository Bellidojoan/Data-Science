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

# Analyze proportions by GameMode and EloRange
data['AvgElo'] = (data['WhiteElo'] + data['BlackElo']) / 2
data['EloRange'] = pd.cut(data['AvgElo'], bins=[1000, 1200, 1400, 1600, 1800, 2000, 2200],
                          labels=['1000-1200', '1200-1400', '1400-1600', '1600-1800', '1800-2000', '2000-2200'])
proportions_by_mode = data.groupby(['GameMode', 'EloRange'])[['good', 'inaccuracy', 'mistake', 'blunder']].sum()
proportions_by_mode = proportions_by_mode.div(proportions_by_mode.sum(axis=1), axis=0)

# Visualize heatmaps by GameMode
for mode in ['Bullet', 'Blitz', 'Rapid']:
    mode_data = proportions_by_mode.loc[mode]
    plt.figure(figsize=(10, 6))
    sns.heatmap(
        mode_data,
        annot=False,
        fmt=".2f",
        cmap="YlGnBu",
        cbar_kws={'label': 'Proportion of Moves'}
    )
    plt.title(f'Move Quality Proportions ({mode})')
    plt.xlabel('Move Quality')
    plt.ylabel('Elo Range')
    plt.tight_layout()
    output_path = os.path.join(output_dir, f'heatmap-{mode.lower()}-moves.png')
    plt.savefig(output_path, dpi=300)
    print(f"Saved heatmap for {mode} to {output_path}")