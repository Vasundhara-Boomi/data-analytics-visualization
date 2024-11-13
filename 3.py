import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(0)
num_samples = 1000

# Generate transaction amounts
transaction_amounts = np.random.normal(loc=100, scale=20, size=num_samples)

# Generate labels (0 for normal, 1 for fraudulent)
labels = np.random.choice([0, 1], size=num_samples, p=[0.9, 0.1])

# Create a DataFrame
data = pd.DataFrame({'TransactionAmount': transaction_amounts, 'Label': labels})

# Create a box plot to visualize the data
plt.figure(figsize=(8, 6))
data.boxplot(column='TransactionAmount', by='Label', grid=False)
plt.title('Distribution of Transaction Amounts by Type')
plt.suptitle('')  # This line is used to remove the default title set by pandas
plt.xlabel('Type (0: Normal, 1: Fraudulent)')
plt.ylabel('Transaction Amount')

# Save the box plot as an image (e.g., PNG)
plt.savefig('boxplot.png', dpi=300, bbox_inches='tight')

# Save the DataFrame to a CSV file
data.to_csv('3.csv', index=False)

# Display the box plot (optional)
plt.show()