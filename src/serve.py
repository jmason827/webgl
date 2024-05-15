import subprocess
import time

# Command 1: Flask application
flask_command = ["flask", "--app", "backend.py", "run"]
# Command 2: HTTP server
http_server_command = ["python", "-m", "http.server", "8000"]

while True:
	# Option 2: Run commands in parallel (consider using Popen for more control)
	flask_process = subprocess.Popen(flask_command)
	http_server_process = subprocess.Popen(http_server_command)

	# wait
	input()

	# Terminate processes if needed
	flask_process.terminate()
	http_server_process.terminate()
