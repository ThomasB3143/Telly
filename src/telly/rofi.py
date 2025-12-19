import subprocess

def show_menu(options, selected, theme=None, prompt=None):
    command = [
        "rofi",
        "-dmenu",
        "-selected-row", str(selected),
    ]

    if theme:
        command += ["-theme", theme]

    if prompt:
        command += ["-p", prompt]

    subprocess.run(
        command,
        input="\n".join(options),
        text=True,
    )
