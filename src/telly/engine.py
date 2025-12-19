import time
import subprocess
from pathlib import Path
import tomllib

from mytool.state import load_state, save_state, clear_state
from mytool.rofi import show_menu

CONFIG_DIR = Path.home() / ".config" / "mytool" / "launchers"
DEFAULT_TIMEOUT = 2.0

def run_launcher(name):
    launcher_dir = CONFIG_DIR / name
    config_path = launcher_dir / "config.toml"

    if not config_path.exists():
        print(f"No launcher config found: {name}")
        return

    with config_path.open("rb") as f:
        config = tomllib.load(f)

    options = config["options"]
    labels = [opt["label"] for opt in options]
    timeout = config.get("timeout", DEFAULT_TIMEOUT)

    index, last_time = load_state(name)

    now = time.time()

    if now - last_time < timeout:
        index = (index + 1) % len(labels)
    else:
        index = 0

    save_state(name, index)

    show_menu(
        labels,
        selected=index,
        theme=str(launcher_dir / "style.css"),
        prompt=config.get("name"),
    )

    time.sleep(timeout)

    current_index, _ = load_state(name)
    if current_index == index:
        clear_state(name)
        script = options[index]["script"]

        subprocess.Popen(
            ["bash", script],
            cwd=launcher_dir,
        )
