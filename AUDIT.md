# Palette audit

Generated from `palette.json` by `scripts/audit_palette.py`.

## Acuity Dark contrast against the editor background

| Token | Hex | WCAG contrast |
|---|---:|---:|
| Main foreground | `#CBD3D8` | 11.61:1 |
| Comment | `#8696A0` | 5.77:1 |
| Amber | `#D5A351` | 7.70:1 |
| Teal | `#4ACFB5` | 9.12:1 |
| Green | `#AECC8C` | 9.90:1 |
| Magenta | `#E3B8EC` | 10.34:1 |
| Sky | `#70AFE8` | 7.53:1 |
| Coral/error | `#F0A29A` | 8.67:1 |

Background: `#17191D`.

## Selected workbench text/background pairs

| Pair | Contrast |
|---|---:|
| Activity bar | 12.25:1 |
| Side bar | 12.05:1 |
| Title bar | 12.25:1 |
| Status bar | 10.34:1 |
| Input | 10.38:1 |
| Active tab | 14.79:1 |
| Inactive tab | 5.92:1 |
| Primary button | 4.67:1 |
| Secondary button | 7.57:1 |
| Active list item | 8.51:1 |
| Badge | 7.13:1 |
| Activity badge | 9.63:1 |
| Remote status | 7.05:1 |
| Warning status | 6.47:1 |
| Error status | 7.97:1 |

These are explicit opaque foreground/background pairs. Transparent overlays and extension-contributed UI can produce different effective colors and require inspection in the running editor.

## Representative canonical theme values

| Theme | Main text | Comment |
|---|---:|---:|
| One Dark Pro | 6.57:1 | 2.32:1 |
| Dracula | 13.36:1 | 3.03:1 |
| Catppuccin Mocha | 11.34:1 | 3.36:1 |
| Tokyo Night | 8.10:1 | 2.76:1 |
| Gruvbox Dark | 10.75:1 | 4.02:1 |
| Nord | 9.25:1 | 2.43:1 |
| Solarized Dark | 4.75:1 | 2.79:1 |
| GitHub Dark | 12.26:1 | 6.15:1 |

These values are canonical-palette checks, not exhaustive audits of every token and extension version.

## Simulated color-vision separation

Minimum pairwise CIE76 distance among the five routine accent colors:

| Simulation | Minimum ΔE76 | Closest pair |
|---|---:|---|
| Normal | 33.83 | Teal / green |
| Protanopia | 11.42 | Magenta / sky |
| Deuteranopia | 18.67 | Teal / magenta |
| Tritanopia | 14.15 | Teal / sky |

The simulation uses the severe-deficiency matrices from Machado, Oliveira, and Fernandes (2009). CIE76 is a screening metric and should not be interpreted as a clinical accessibility guarantee.
