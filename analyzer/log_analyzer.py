import threading
from queue import Queue
from analyzer.patterns import PATTERNS

class LogAnalyzer:
    def __init__(self, file_path, thread_count=4):
        self.file_path = file_path
        self.thread_count = thread_count
        self.queue = Queue()
        self.results = []
        self.lock = threading.Lock()

    def load_logs(self):
        with open(self.file_path, "r") as f:
            for line in f:
                self.queue.put(line)

    def worker(self):
        while not self.queue.empty():
            line = self.queue.get()
            self.analyze_line(line)
            self.queue.task_done()

    def analyze_line(self, line):
        for key, pattern in PATTERNS.items():
            match = pattern.search(line)
            if match:
                event = {
                    "type": key,
                    "ip": match.group(1) if match.groups() else "N/A",
                    "log": line.strip()
                }
                with self.lock:
                    self.results.append(event)

    def run(self):
        self.load_logs()

        threads = []
        for _ in range(self.thread_count):
            t = threading.Thread(target=self.worker)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        return self.results