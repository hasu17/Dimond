import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


sns.set_theme(style="whitegrid", palette="muted", font_scale=1.2)

# 1. Load the dataset
# The dataset is at c:\Users\Hp\Desktop\Dimond\diamonds.csv\diamonds.csv
dataset_path = r'c:\Users\Hp\Desktop\Dimond\diamonds.csv\diamonds.csv'
df = pd.read_csv(dataset_path)

# 2. Data Cleaning
# Remove the first column as it's an index
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# Check for null values
print("Missing values in each column:")
print(df.isnull().sum())

# 3. Exploratory Data Analysis (EDA)
print("\nSummary Statistics:")
print(df.describe())

# 4. Visualizations
output_dir = 'plots'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# A. Price Distribution
plt.figure(figsize=(12, 7))
sns.histplot(df['price'], bins=50, kde=True)
plt.title('Distribution of Diamond Prices')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'price_distribution.png'))
plt.close()

# B. Carat vs Price
plt.figure(figsize=(12, 7))
sns.scatterplot(data=df, x='carat', y='price', alpha=0.5, hue='cut')
plt.title('Carat Weight vs. Price')
plt.xlabel('Carat')
plt.ylabel('Price ($)')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'carat_vs_price.png'))
plt.close()

# C. Impact of Cut on Price
plt.figure(figsize=(12, 7))
sns.boxplot(data=df, x='cut', y='price', order=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
plt.title('Impact of Cut Quality on Price')
plt.xlabel('Cut Quality')
plt.ylabel('Price ($)')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'cut_vs_price.png'))
plt.close()

# D. Impact of Color on Price
plt.figure(figsize=(12, 7))
sns.boxplot(data=df, x='color', y='price', order=['D', 'E', 'F', 'G', 'H', 'I', 'J'])
plt.title('Impact of Diamond Color on Price')
plt.xlabel('Color (D is best, J is worst)')
plt.ylabel('Price ($)')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'color_vs_price.png'))
plt.close()

# E. Impact of Clarity on Price
plt.figure(figsize=(12, 7))
sns.boxplot(data=df, x='clarity', y='price', order=['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
plt.title('Impact of Diamond Clarity on Price')
plt.xlabel('Clarity (IF is best, I1 is worst)')
plt.ylabel('Price ($)')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'clarity_vs_price.png'))
plt.close()

# F. Correlation Heatmap

plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=['number'])
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Diamond Attributes')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
plt.close()

# G. Clarity vs Carat
plt.figure(figsize=(12, 7))
sns.boxplot(data=df, x='clarity', y='carat', order=['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
plt.title('Distribution of Carat Weight across Clarity Grades')
plt.xlabel('Clarity (IF is best, I1 is worst)')
plt.ylabel('Carat Weight')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'clarity_vs_carat.png'))
plt.close()

# H. Cut vs Clarity Heatmap
plt.figure(figsize=(12, 8))
cut_clarity_counts = pd.crosstab(df['cut'], df['clarity'])

cut_order = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
clarity_order = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
cut_clarity_counts = cut_clarity_counts.reindex(index=cut_order, columns=clarity_order)

sns.heatmap(cut_clarity_counts, annot=True, fmt="d", cmap="YlGnBu")
plt.title('Frequency of Diamonds by Cut and Clarity')
plt.xlabel('Clarity (IF is best)')
plt.ylabel('Cut Quality (Ideal is best)')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'cut_vs_clarity_heatmap.png'))
plt.close()

print("\nAnalysis complete. Plots saved in the 'plots' directory.")
print("Updated to include Clarity vs Carat and Cut vs Clarity.")
