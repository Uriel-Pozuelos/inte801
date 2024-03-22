from dataclasses import dataclass
import json

@dataclass
class D:
    debug: bool = False

    def log(self, msg, color=None):
        if self.debug:
            if color:
                colored_msg = f"{color}{msg}\033[0m"
                print(colored_msg)
            else:
                print(msg)

    def error(self, msg):
        red = '\033[91m'
        self.log(f"ERROR: {msg}", color=red)

    def info(self, msg):
        blue = '\033[94m'
        self.log(f"INFO: {msg}", color=blue)

    def success(self, msg):
        green = '\033[92m'
        self.log(f"SUCCESS: {msg}", color=green)

    def warning(self, msg):
        yellow = '\033[93m'
        self.log(f"WARNING: {msg}", color=yellow)

    def json(self, data):
        formatted_json = None

        try:
          formatted_json = json.dumps(data, indent=4)
        except Exception as e:
          self.error(f"Error al formatear JSON: {e}")
          return
        pink = '\033[95m'
        self.log(f"JSON: {formatted_json}", color=pink)
        return formatted_json
