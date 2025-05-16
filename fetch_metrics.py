import requests
from datetime import datetime, timedelta

OWNER = "abhinavkumar2119"
REPO = "smartdeploy"
TOKEN = "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"  # Replace this with your token

HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs"

def fetch_workflow_runs(per_page=100):
    params = {"per_page": per_page}
    response = requests.get(API_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()["workflow_runs"]

def analyze_runs(runs):
    total_runs = len(runs)
    failed_runs = 0
    total_duration = 0
    now = datetime.utcnow()
    deployments_last_7_days = 0

    for run in runs:
        created_at = datetime.strptime(run["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        completed_at = datetime.strptime(run["updated_at"], "%Y-%m-%dT%H:%M:%SZ")
        duration = (completed_at - created_at).total_seconds()
        total_duration += duration

        if run["conclusion"] != "success":
            failed_runs += 1

        if now - created_at < timedelta(days=7):
            deployments_last_7_days += 1

    avg_build_time = total_duration / total_runs if total_runs else 0
    failure_rate = (failed_runs / total_runs) * 100 if total_runs else 0
    deployment_frequency_per_day = deployments_last_7_days / 7

    return {
        "total_runs": total_runs,
        "failed_runs": failed_runs,
        "avg_build_time_seconds": avg_build_time,
        "failure_rate_percent": failure_rate,
        "deployment_frequency_per_day": deployment_frequency_per_day
    }

def main():
    runs = fetch_workflow_runs()
    metrics = analyze_runs(runs)
    print("📊 Metrics from last 100 workflow runs:")
    print(f"✅ Total runs: {metrics['total_runs']}")
    print(f"❌ Failed runs: {metrics['failed_runs']}")
    print(f"📉 Failure rate: {metrics['failure_rate_percent']:.2f}%")
    print(f"⏱ Average build time: {metrics['avg_build_time_seconds'] / 60:.2f} minutes")
    print(f"🚀 Deployment frequency: {metrics['deployment_frequency_per_day']:.2f} per day")

if __name__ == "__main__":
    main()
