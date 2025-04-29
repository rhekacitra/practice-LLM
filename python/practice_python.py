import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('articles.csv')

# Remove rows with missing 'category')
df_clean = df.dropna(subset=['category'])

# Count articles per category
category_counts = df_clean['category'].value_counts()

# Plot a bar graph to a png
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar')
plt.title('Number of Articles per Category')
plt.xlabel('Category')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('python/practice_python_plot.png')
plt.show()