# Global watcher: when a window gains focus in a fat-layout tab, move it to
# the top so the active window is always the enlarged (full-width) one.
from typing import Any

from kitty.boss import Boss
from kitty.window import Window


def on_focus_change(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    if not data.get('focused'):
        return
    tab = window.tabref()
    if tab is None or tab.current_layout.name != 'fat':
        return
    wl = tab.windows
    # tab.active_window is not updated yet when this hook fires, so activate
    # the focused window's group explicitly, then move it to the top slot
    wl.set_active_window_group_for(window)
    if wl.move_window_group(by=-wl.active_group_idx):
        tab.relayout()
