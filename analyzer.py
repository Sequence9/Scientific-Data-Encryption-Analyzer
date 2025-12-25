import numpy as np
import scipy.stats as stats

# generate sample scientific data: 100 random measurements (e.g., sensor readings) between 0 and 100
data = np.random.uniform(0, 100, 100).astype(np.uint8)  # convert to uint8 for byte-level XOR

# XOR encryption key
key = np.array([42] * len(data), dtype=np.uint8)

encrypted = np.bitwise_xor(data, key)

# simulate transmission errors
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

# error flag: check if any differences > 0
errors_detected = np.any(differences > 0)
print(f"Errors detected (any difference): {errors_detected}")