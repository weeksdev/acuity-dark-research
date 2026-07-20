# Acuity Dark Research

A dark Visual Studio Code color theme designed from explicit legibility and accessibility constraints rather than aesthetic preference alone.

## What is different

- Core syntax colors have WCAG contrast ratios from **7.53:1 to 10.34:1** against the editor background.
- Ordinary foreground text is **11.61:1**.
- Comments are deliberately subordinate but remain **5.77:1**, above the WCAG 4.5:1 normal-text threshold.
- The five routine syntax accents were optimized for separation under simulated protanopia, deuteranopia, and tritanopia.
- Red/coral is reserved for errors, invalid tokens, and deletions rather than routine code.
- Control-flow keywords use bold and comments use italics, so important distinctions do not rely on hue alone.
- Semantic highlighting is enabled and includes mappings for C# namespaces, types, methods, properties, constants, parameters, and attributes.

The accompanying `RESEARCH.md` report explains the evidence, assumptions, calculations, theme comparison, and limitations. `AUDIT.md` contains the numerical checks.

## Install the VSIX

From a terminal:

```bash
code --install-extension acuity-dark-research-0.1.0.vsix
```

Or in VS Code:

1. Open **Extensions**.
2. Select the `...` menu.
3. Select **Install from VSIX...**.
4. Choose `acuity-dark-research-0.1.0.vsix`.
5. Open **Preferences: Color Theme** with `Ctrl/Cmd+K`, then `Ctrl/Cmd+T`.
6. Select **Acuity Dark Research**.

Open `samples/ThemePreview.cs` to exercise the C# mappings.

## Recommended test settings

```json
{
  "editor.semanticHighlighting.enabled": "configuredByTheme",
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active"
}
```

## Run the audit

The script uses only the Python standard library:

```bash
python scripts/audit_palette.py
```

## Interpreting the claim

This is an evidence-informed candidate, not proof of universal superiority. No published study compares every VS Code theme in a controlled programming trial. The theme is intended to outperform common dark themes on measurable prerequisites—contrast, restrained salience, readable comments, semantic redundancy, and simulated color-vision robustness—then be tested in actual development work.
