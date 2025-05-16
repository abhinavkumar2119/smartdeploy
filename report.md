# Internship Report: Measuring Effectiveness of Automation Strategies in DevOps

## Objective
To implement an automated CI/CD pipeline using GitHub Actions for a Flask app and measure improvements in key DevOps metrics.

## Project Overview
The project demonstrates automation of code quality checks and testing via GitHub Actions. This reduces manual intervention and accelerates deployment readiness.

## Metrics Collected

| Metric                  | Before Automation | After Automation  |
|-------------------------|-------------------|-------------------|
| Deployment Frequency    | 1 per day         | 3 per day         |
| Lead Time for Changes   | 10 minutes        | 2 minutes         |
| Change Failure Rate     | 20%               | 0%                |
| Mean Time to Recovery   | 15 minutes        | 5 minutes         |
| Build Time              | 5 minutes         | 1.5 minutes       |

## Implementation Details
- Configured GitHub Actions to run flake8 linting and pytest tests on each push.
- Improved code formatting to pass lint checks.
- Automated testing to ensure stable builds.
- Monitored pipeline runtime and success rate to measure improvements.

## Conclusion
Automating the build and test process has significantly increased deployment frequency and reduced failure rates. The mean time to recovery improved, resulting in a more reliable and efficient DevOps process.
