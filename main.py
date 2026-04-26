import time
from analyzer.log_analyzer import LogAnalyzer
from analyzer.utils import summarize_results, save_report
from colorama import Fore, Style

def main():
    file_path = "logs/large.log"

    print(Fore.CYAN + "[+] Starting Log Analysis..." + Style.RESET_ALL)

    analyzer = LogAnalyzer(file_path)

    start = time.time()
    results = analyzer.run()
    end = time.time()
    print(f"\n[+] Time taken: {end - start:.2f} seconds")

    summary = summarize_results(results)

    print(Fore.GREEN + "\n[+] Summary:" + Style.RESET_ALL)
    for k, v in summary.items():
        print(f"{k}: {v}")

    save_report(results)

    print(Fore.YELLOW + "\n[+] Report saved to output/report.txt" + Style.RESET_ALL)

if __name__ == "__main__":
    main()