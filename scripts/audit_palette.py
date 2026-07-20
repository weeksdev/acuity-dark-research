#!/usr/bin/env python3
"""Audit Acuity Dark and representative dark-theme palette values.

Uses the WCAG relative-luminance contrast formula and severe color-vision-
deficiency simulation matrices published by Machado, Oliveira, and Fernandes
(2009). Pairwise color-distance reporting uses CIE76 after simulation as a
screening heuristic, not as a substitute for human testing.
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]

CVD_MATRICES = {
    "protanopia": (
        (0.152286, 1.052583, -0.204868),
        (0.114503, 0.786281, 0.099216),
        (-0.003882, -0.048116, 1.051998),
    ),
    "deuteranopia": (
        (0.367322, 0.860646, -0.227968),
        (0.280085, 0.672501, 0.047413),
        (-0.011820, 0.042940, 0.968881),
    ),
    "tritanopia": (
        (1.255528, -0.076749, -0.178779),
        (-0.078411, 0.930809, 0.147602),
        (0.004733, 0.691367, 0.303900),
    ),
}

REPRESENTATIVE_THEMES = {
    "One Dark Pro": {"background": "#282C34", "text": "#ABB2BF", "comment": "#5C6370"},
    "Dracula": {"background": "#282A36", "text": "#F8F8F2", "comment": "#6272A4"},
    "Catppuccin Mocha": {"background": "#1E1E2E", "text": "#CDD6F4", "comment": "#6C7086"},
    "Tokyo Night": {"background": "#1A1B26", "text": "#A9B1D6", "comment": "#565F89"},
    "Gruvbox Dark": {"background": "#282828", "text": "#EBDBB2", "comment": "#928374"},
    "Nord": {"background": "#2E3440", "text": "#D8DEE9", "comment": "#616E88"},
    "Solarized Dark": {"background": "#002B36", "text": "#839496", "comment": "#586E75"},
    "GitHub Dark": {"background": "#0D1117", "text": "#C9D1D9", "comment": "#8B949E"},
}

CORE_TOKENS = ("foreground", "comment", "amber", "teal", "green", "magenta", "sky", "coral")
SYNTAX_ACCENTS = ("amber", "teal", "green", "magenta", "sky")


def parse_hex(value: str) -> tuple[float, float, float]:
    value = value.removeprefix("#")[:6]
    if len(value) != 6:
        raise ValueError(f"Expected six-digit hex color, got {value!r}")
    return tuple(int(value[i:i + 2], 16) / 255.0 for i in (0, 2, 4))  # type: ignore[return-value]


def srgb_to_linear(channel: float) -> float:
    return channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4


def linear_to_srgb(channel: float) -> float:
    channel = min(1.0, max(0.0, channel))
    return 12.92 * channel if channel <= 0.0031308 else 1.055 * channel ** (1 / 2.4) - 0.055


def relative_luminance(value: str) -> float:
    r, g, b = (srgb_to_linear(c) for c in parse_hex(value))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(a: str, b: str) -> float:
    high, low = sorted((relative_luminance(a), relative_luminance(b)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def mat_vec(matrix: tuple[tuple[float, float, float], ...], vector: tuple[float, float, float]) -> tuple[float, float, float]:
    return tuple(sum(row[i] * vector[i] for i in range(3)) for row in matrix)  # type: ignore[return-value]


def simulate_cvd(value: str, matrix: tuple[tuple[float, float, float], ...]) -> tuple[float, float, float]:
    linear = tuple(srgb_to_linear(c) for c in parse_hex(value))
    simulated_linear = mat_vec(matrix, linear)  # type: ignore[arg-type]
    return tuple(linear_to_srgb(c) for c in simulated_linear)  # type: ignore[return-value]


def rgb_to_lab(rgb: tuple[float, float, float]) -> tuple[float, float, float]:
    r, g, b = (srgb_to_linear(c) for c in rgb)
    x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / 0.95047
    y = (0.2126729 * r + 0.7151522 * g + 0.0721750 * b) / 1.00000
    z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / 1.08883

    def f(t: float) -> float:
        delta = 6 / 29
        return t ** (1 / 3) if t > delta ** 3 else t / (3 * delta ** 2) + 4 / 29

    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def delta_e_76(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def pairwise_distances(palette: dict[str, str], keys: Iterable[str], mode: str | None = None):
    matrix = CVD_MATRICES.get(mode) if mode else None
    prepared = {}
    for key in keys:
        rgb = parse_hex(palette[key])
        if matrix:
            rgb = simulate_cvd(palette[key], matrix)
        prepared[key] = rgb_to_lab(rgb)
    rows = []
    for left, right in itertools.combinations(keys, 2):
        rows.append((delta_e_76(prepared[left], prepared[right]), left, right))
    return sorted(rows)


def main() -> None:
    palette = json.loads((ROOT / "palette.json").read_text())
    background = palette["background"]

    print("Acuity Dark contrast against editor background")
    print("token\thex\tcontrast")
    for key in CORE_TOKENS:
        print(f"{key}\t{palette[key]}\t{contrast_ratio(palette[key], background):.2f}:1")

    theme = json.loads((ROOT / "themes" / "acuity-dark-color-theme.json").read_text())
    workbench = theme["colors"]
    workbench_pairs = [
        ("activity bar", "activityBar.foreground", "activityBar.background"),
        ("side bar", "sideBar.foreground", "sideBar.background"),
        ("title bar", "titleBar.activeForeground", "titleBar.activeBackground"),
        ("status bar", "statusBar.foreground", "statusBar.background"),
        ("input", "input.foreground", "input.background"),
        ("active tab", "tab.activeForeground", "tab.activeBackground"),
        ("inactive tab", "tab.inactiveForeground", "tab.inactiveBackground"),
        ("primary button", "button.foreground", "button.background"),
        ("secondary button", "button.secondaryForeground", "button.secondaryBackground"),
        ("active list item", "list.activeSelectionForeground", "list.activeSelectionBackground"),
        ("badge", "badge.foreground", "badge.background"),
        ("activity badge", "activityBarBadge.foreground", "activityBarBadge.background"),
        ("remote status", "statusBarItem.remoteForeground", "statusBarItem.remoteBackground"),
        ("warning status", "statusBarItem.warningForeground", "statusBarItem.warningBackground"),
        ("error status", "statusBarItem.errorForeground", "statusBarItem.errorBackground"),
    ]
    print("\nSelected workbench text/background contrast")
    print("pair\tcontrast")
    for label, foreground_key, background_key in workbench_pairs:
        print(f"{label}\t{contrast_ratio(workbench[foreground_key], workbench[background_key]):.2f}:1")

    print("\nRepresentative theme canonical text/comment contrast")
    print("theme\ttext\tcomment")
    for name, values in REPRESENTATIVE_THEMES.items():
        print(
            f"{name}\t{contrast_ratio(values['text'], values['background']):.2f}:1"
            f"\t{contrast_ratio(values['comment'], values['background']):.2f}:1"
        )

    print("\nMinimum pairwise CIE76 distance among syntax accents")
    for mode in (None, "protanopia", "deuteranopia", "tritanopia"):
        rows = pairwise_distances(palette, SYNTAX_ACCENTS, mode)
        distance, left, right = rows[0]
        label = mode or "normal"
        print(f"{label}\t{distance:.2f}\t{left}/{right}")

    print("\nClosest five pairs under each simulated viewing condition")
    for mode in (None, "protanopia", "deuteranopia", "tritanopia"):
        label = mode or "normal"
        print(f"[{label}]")
        for distance, left, right in pairwise_distances(palette, SYNTAX_ACCENTS, mode)[:5]:
            print(f"  {left:10s} {right:10s} ΔE76={distance:.2f}")


if __name__ == "__main__":
    main()
