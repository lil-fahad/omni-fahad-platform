
# main.py — Auto-Training + Prediction Loop
import schedule
import time
import subprocess

def job():
    print("Running scheduled pipeline...")
    subprocess.run(["python", "run_pipeline.py"])

# Run every 6 hours
schedule.every(6).hours.do(job)

print("Scheduler started. Will run every 6 hours.")
while True:
    schedule.run_pending()
    time.sleep(60)
