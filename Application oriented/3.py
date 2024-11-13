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

# Create a scatter plot to visualize the data
plt.figure(figsize=(8, 6))
plt.scatter(data[data['Label'] == 0]['TransactionAmount'], data[data['Label'] == 0].index, color='blue', label='Normal')
plt.scatter(data[data['Label'] == 1]['TransactionAmount'], data[data['Label'] == 1].index, color='red', label='Fraudulent')
plt.xlabel('Transaction Amount')
plt.ylabel('Sample Index')
plt.legend()
plt.title('Synthetic Credit Card Transactions')

# Save the scatterplot as an image (e.g., PNG)
plt.savefig('scatterplot.png', dpi=300, bbox_inches='tight')

# Save the DataFrame to a CSV file
data.to_csv('3.csv', index=False)

# Display the scatterplot (optional)
plt.show()
