# Global watcher: in vertical-layout tabs, the focused window gets ~2x the
# height of the inactive windows; losing focus restores equal sizes.
from typing import Any

from kitty.boss import Boss
from kitty.window import Window


def on_focus_change(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    tab = window.tabref()
    if tab is None:
        return
    layout = tab.current_layout
    if layout.name != 'vertical':
        return
    if not data.get('focused'):
        if layout.biased_map:
            layout.biased_map = {}
            tab.relayout()
        return
    n = tab.windows.num_groups
    if n < 2:
        return
    idx = tab.windows.group_idx_for_window(window.id)
    if idx is None:
        return
    # biased_map values are increments over the equal split; to give this
    # window twice each other window's share, add (n-1)/(n*(n+1)) to its slot.
    layout.biased_map = {idx: (n - 1) / (n * (n + 1))}
    tab.relayout()
