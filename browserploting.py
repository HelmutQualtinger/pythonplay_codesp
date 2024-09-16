# %%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import webbrowser
import os
import socketserver

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

import http.server

PORT = 8000
DIRECTORY = "/workspaces/pythonplay_codesp/browserploting"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    webbrowser.open(f"http://localhost:{PORT}/sine_wave.pdf")
    httpd.serve_forever()
# %%
