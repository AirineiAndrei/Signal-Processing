P_signal_db = 90
SNR_db = 80

# SNR_db = 10 * log10(P_signal / P_noise)
# SNR_db = 10 * log10(P_signal) - 10 * log10(P_noise)
# P_noise_db = P_signal_db - SNR_db
P_noise_db = P_signal_db - SNR_db

print(f"The power of the noise is {P_noise_db} dB")
