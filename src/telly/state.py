import time
from pathlib import Path

STATE_DIR = Path("/tmp") / "telly"
STATE_DIR.mkdir(exist_ok=True)

def load_state(name):
    """Return (index, timestamp) or (0, 0) if no state exists."""
    path = STATE_DIR / f"{name}.state"

    if not path.exists():
        return 0, 0
        
    index, timestamp = path.read_text().split()
    return int(index), float(timestamp)

def save_state(name, index):
    """Save the current index and current time."""
    path = STATE_DIR / f"{name}.state"
    path.write_text(f"{index} {time.time()}")

def clear_state(name):
    """Remove state file."""
    path = STATE_DIR / f"{name}.state"
    path.unlink(missing_ok=True)
