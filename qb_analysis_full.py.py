import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Excel file
df = pd.read_excel("qb_stats.xlsx")

# Normalize function
def normalize(series, invert=False):
    norm = (series - series.min()) / (series.max() - series.min())
    return 1 - norm if invert else norm

# Normalize stats
df['Norm_PassYds']      = normalize(df['PassYds'])
df['Norm_PassTD']       = normalize(df['PassTD'])
df['Norm_INT']          = normalize(df['INT'], invert=True)
df['Norm_Cmp']          = normalize(df['Cmp%'])
df['Norm_YA']           = normalize(df['Y/A'])
df['Norm_Rating']       = normalize(df['PasserRating'])
df['Norm_SackRate']     = normalize(df['SackRate%'], invert=True)
df['Norm_RushYds']      = normalize(df['RushYds'])
df['Norm_RushTD']       = normalize(df['RushTD'])
df['Norm_OLRank']       = normalize(df['OLRank'], invert=False)

# Context-adjusted QBScore with reduced rushing weight
df['QBScore'] = (
    df['Norm_YA']        * 0.25 +
    df['Norm_PassTD']    * 0.15 +
    df['Norm_INT']       * 0.20 +
    df['Norm_Rating']    * 0.12 +
    df['Norm_RushYds']   * 0.07 +
    df['Norm_RushTD']    * 0.07 +
    df['Norm_SackRate']  * 0.12 +
    df['Norm_OLRank']    * 0.12 +
    df['Norm_PassYds']   * 0.12
)

# Scale for readability
df['QBScoreScaled'] = df['QBScore'] * 100

# Rank QBs
df['PasserRatingRank'] = df['PasserRating'].rank(ascending=False, method='min').astype(int)
df['QBScoreRank'] = df['QBScoreScaled'].rank(ascending=False, method='min').astype(int)
df['RankDiff'] = df['PasserRatingRank'] - df['QBScoreRank']

# Top 5 improved/worsened
top_improved = df.sort_values('RankDiff', ascending=False).head(5)
top_worsened = df.sort_values('RankDiff').head(5)

# Trend line
z = np.polyfit(df['PasserRating'], df['QBScoreScaled'], 1)
p = np.poly1d(z)
df['TrendLine'] = p(df['PasserRating'])

# Scatter plot
plt.figure(figsize=(22,14))
plt.scatter(df['PasserRating'], df['QBScoreScaled'], color='gray', s=150, alpha=0.7, edgecolor='k')

# Annotate all QBs with slight offsets
for i, row in df.iterrows():
    plt.text(row['PasserRating'] + 0.15, row['QBScoreScaled'] + 0.5, row['Player'],
             fontsize=9, weight='bold', rotation=30)

# Highlight top improved/worsened with arrows
for i, row in top_improved.iterrows():
    plt.annotate(f"+{int(row['RankDiff'])}", 
                 xy=(row['PasserRating'], row['QBScoreScaled']),
                 xytext=(row['PasserRating'] + 0.5, row['QBScoreScaled'] + 3),
                 arrowprops=dict(facecolor='blue', shrink=0.05),
                 fontsize=12, color='blue', fontweight='bold')

for i, row in top_worsened.iterrows():
    plt.annotate(f"{int(row['RankDiff'])}", 
                 xy=(row['PasserRating'], row['QBScoreScaled']),
                 xytext=(row['PasserRating'] + 0.5, row['QBScoreScaled'] - 5),
                 arrowprops=dict(facecolor='orange', shrink=0.05),
                 fontsize=12, color='orange', fontweight='bold')

# Trend line
plt.plot(df['PasserRating'], df['TrendLine'], "b--", linewidth=2)

plt.xlabel("Passer Rating", fontsize=14)
plt.ylabel("Context-Adjusted QBScore (Scaled 0-100)", fontsize=14)
plt.title("QB Performance: Passer Rating vs Context-Adjusted QBScore", fontsize=16)
plt.grid(True)

# Add table for top improved QBs (top left) with ranks
improved_table = top_improved[['Player', 'PasserRatingRank', 'QBScoreRank', 'RankDiff']].copy()
improved_table.rename(columns={'PasserRatingRank':'PasserPos',
                               'QBScoreRank':'QBScorePos',
                               'RankDiff':'Improvement'}, inplace=True)
plt.table(cellText=improved_table.values,
          colLabels=improved_table.columns,
          cellLoc='center',
          colLoc='center',
          loc='upper left',
          bbox=[0.01, 0.65, 0.35, 0.3],
          edges='closed')

# Add table for top worsened QBs (bottom right) with ranks
worsened_table = top_worsened[['Player', 'PasserRatingRank', 'QBScoreRank', 'RankDiff']].copy()
worsened_table.rename(columns={'PasserRatingRank':'PasserPos',
                               'QBScoreRank':'QBScorePos',
                               'RankDiff':'Decline'}, inplace=True)
plt.table(cellText=worsened_table.values,
          colLabels=worsened_table.columns,
          cellLoc='center',
          colLoc='center',
          loc='lower right',
          bbox=[0.65, 0.05, 0.35, 0.3],
          edges='closed')

plt.tight_layout()
plt.show()