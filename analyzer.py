import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# generate sample scientific data
data = np.random.uniform(0, 100, 100).astype(np.uint8)  # convert to uint8 for byte-level XOR

# simple XOR encryption key
key = np.array([42] * len(data), dtype=np.uint8)

encrypted = np.bitwise_xor(data, key)

# Simulate transmission errors: randomly flip bits in 5% of the data
error_rate = 0.05
num_errors = int(len(encrypted) * error_rate)
error_indices = np.random.choice(len(encrypted), num_errors, replace=False)
for idx in error_indices:
    flip_mask = np.random.randint(1, 256, dtype=np.uint8)
    encrypted[idx] = np.bitwise_xor(encrypted[idx], flip_mask)

decrypted = np.bitwise_xor(encrypted, key)

differences = np.abs(data.astype(float) - decrypted.astype(float))

# analyze errors with SciPy
mean_diff = np.mean(differences)
std_diff = np.std(differences)
t_stat, p_value = stats.ttest_1samp(differences, 0)

print("Sample Original Data (first 10):", data[:10])
print("Sample Decrypted Data (first 10):", decrypted[:10])
print(f"Mean difference: {mean_diff:.2f}")
print(f"Standard deviation of differences: {std_diff:.2f}")
print(f"T-statistic: {t_stat:.2f}, P-value: {p_value:.4f}")
if p_value < 0.05:
    print("Significant errors detected (p < 0.05). Data integrity compromised.")
else:
    print("No significant errors detected.")

errors_detected = np.any(differences > 0)
print(f"Errors detected (any difference): {errors_detected}")

# Matplotlib Visualizations

# plot 1: line comparison of original vs decrypted data
plt.figure(figsize=(10, 6))
plt.plot(data, label='Original Data', alpha=0.8)
plt.plot(decrypted, label='Decrypted (with simulated errors)', alpha=0.8, linestyle='--')
plt.title('Original vs Decrypted Data Comparison')
plt.xlabel('Data Point Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('data_comparison.png')
plt.show()

# plot 2: bar chart of absolute differences
plt.figure(figsize=(10, 6))
plt.bar(range(len(differences)), differences, color='salmon', alpha=0.7)
plt.title('Absolute Differences Between Original and Decrypted Data')
plt.xlabel('Data Point Index')
plt.ylabel('Difference')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('differences_bar.png')
plt.show()
