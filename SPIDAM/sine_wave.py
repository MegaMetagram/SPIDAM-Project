import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave(frequency, amplitude, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    
    plt.figure(figsize=(10, 4))
    plt.plot(t, y)
    plt.title(f'Sine Wave: {frequency}Hz')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# Example usage:
# plot_sine_wave(frequency=440, amplitude=1.0, duration=2.0)