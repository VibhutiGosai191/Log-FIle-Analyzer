from collections import defaultdict

def summarize_results(results):
    summary = defaultdict(int)
    for event in results:
        summary[event['type']] += 1
    return summary

def save_report(results, filepath="output/report.txt"):
    with open(filepath, "w") as f:
        for event in results:
            f.write(f"{event}\n")