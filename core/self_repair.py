import datetime
import platform
import psutil
import logging

class DiagnosticEngine:
    @staticmethod
    def run_check():
        report = {
            "timestamp": datetime.datetime.now().isoformat(),
            "system": platform.system(),
            "release": platform.release(),
            "cpu_usage": psutil.cpu_percent(interval=1),
            "memory": psutil.virtual_memory()._asdict(),
            "disk": psutil.disk_usage('/')._asdict(),
            "status": "OK",
            "notes": ""
        }

        # Basic heuristics
        if report["cpu_usage"] > 90:
            report["status"] = "Warning"
            report["notes"] = "High CPU usage detected."

        if report["memory"]["percent"] > 90:
            report["status"] = "Warning"
            report["notes"] += " High memory usage."

        if report["disk"]["percent"] > 95:
            report["status"] = "Critical"
            report["notes"] += " Disk almost full."

        logging.info("Diagnostic Report: %s", report)
        return report
