import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Generate data for the sine wave
x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)

# Create a plot
plt.figure()
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Save the plot to a PDF file
with PdfPages('/workspaces/pythonplay_codesp/browserploting/sine_wave.pdf') as pdf:
    pdf.savefig()
    plt.close()

print("Sine wave plot saved to sine_wave.pdf")