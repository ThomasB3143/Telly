# teevee

**teevee** is a single-button cyclic launcher for Linux desktops.

You bind a key to a launcher, press it to open a menu, press it again to cycle through options, then leave it to timeout to activate the currently selected option — similar to classic TV menus.

teevee is written in Bash and integrates with **dunst** for notifications.

---

## Features

- Single-button UI (perfect for keyboard-only or minimal setups)
- Cyclic selection with configurable timeout
- Per-launcher configuration (no global config required)
- Persistent last-selected option
- dunst notifications with:
  - Replacement (no spam)
  - Per-option icons
  - Per-option text
- No daemon, no polling, no background services
- XDG-compliant state handling

## Setting up your first launcher

1. Create a "teevee" config directory
2. Create a subdirectory named as your launcher title
3. Create a launcher.conf (see [this example](https://github.com/ThomasB3143/teevee/blob/main/examples/launchers/mylauncher/launcher.conf))
4. Create an "options/" subdirectory
5. Insert a script per option (note that scripts are read in alphabetical order)
6. Bind a key to "teevee run <launcher-title>

Now you can repeat steps 2-6 for as many launchers as you'd like!

## Launcher ideas

- A power-mode menu to choose between performance modes (power-saving, balanced, etc.)
- A menu to shift between wallpapers or themes