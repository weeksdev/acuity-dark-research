# Acuity Dark Research: evidence, derivation, and limitations

## Executive conclusion

There is no defensible scientific basis for declaring any existing dark coding theme universally “best.” The direct programming evidence is sparse, participant counts are generally small, and most display studies use prose, symbols, or search tasks rather than source code. Moreover, controlled proofreading studies repeatedly find a performance advantage for positive polarity—dark text on a light background—so a dark theme begins with a known trade-off.

A more supportable target is: **construct a dark theme that satisfies stronger measurable readability constraints than most popular alternatives, minimizes avoidable color-related failure modes, and exposes its assumptions for testing.** Acuity Dark Research is that candidate.

Its design requirements are:

1. Routine syntax colors must reach at least 7:1 contrast against the editor background.
2. Comments must reach at least 4.5:1 rather than becoming decorative low-contrast text.
3. Hue must not be the only carrier of meaning.
4. Routine syntax colors must remain distinguishable under severe simulated protanopia, deuteranopia, and tritanopia.
5. High-salience red must be reserved for exceptional states.
6. The number of routine hues must remain limited; punctuation and ordinary variables stay neutral.
7. VS Code semantic tokens must be used, particularly for C#.

These are evidence-backed constraints. The exact hexadecimal values are engineering outputs derived under those constraints; no journal article can legitimately prescribe a specific hex code for every programming token.

## 1. What was reviewed

### Representative VS Code theme families

The survey covered eight influential design families rather than attempting to enumerate thousands of Marketplace variants:

| Theme family | Characteristic design approach | Main issue relevant to this project |
|---|---|---|
| [One Dark Pro](https://github.com/Binaryify/OneDark-Pro) | Cool charcoal background with pastel semantic accents | Canonical comment tone is very low contrast. |
| [Dracula](https://draculatheme.com/visual-studio-code) | Deep violet-gray background with bright cyan, green, pink, purple, and yellow | Excellent default-text contrast; canonical comments are much weaker. |
| [Catppuccin Mocha](https://github.com/catppuccin/vscode) | Warm pastel palette intended to balance low and high contrast | Strong default text; canonical comments remain below 4.5:1. |
| [Tokyo Night](https://github.com/enkia/tokyo-night-vscode-theme) | Blue-black surface with cool neon/pastel accents and intentionally restrained UI contrast | Canonical comments are low contrast; some UI elements intentionally trade visibility for atmosphere. |
| [Gruvbox Dark](https://github.com/jdinhify/vscode-theme-gruvbox) | Warm retro brown-gray base with muted yellow, orange, green, and aqua | Better comment contrast than many themes, but still below 4.5:1 in the canonical palette. |
| [Nord](https://www.nordtheme.com/docs/colors-and-palettes) | Restrained blue-gray base with cool “frost” accents | Cohesive and calm; canonical comments are low contrast. |
| [Solarized Dark](https://ethanschoonover.com/solarized/) | Deliberately constructed low-contrast CIELAB-oriented 16-color system | Base text only narrowly clears 4.5:1 and comments are substantially lower. |
| [GitHub Dark](https://github.com/primer/github-vscode-theme) | Neutral near-black base, conservative token colors, strong general text hierarchy | The strongest canonical comment contrast in this comparison; less aggressive categorical separation. |

The numerical comparison in `AUDIT.md` uses representative canonical background, foreground, and comment colors. It is not a full audit of every current token in every extension version.

### VS Code implementation model

VS Code separates workbench colors, TextMate `tokenColors`, and semantic `semanticTokenColors`. Semantic highlighting supplies language-aware token types such as class, method, property, namespace, parameter, and readonly modifiers. Acuity uses all three layers and enables semantic highlighting by default.

Sources: [VS Code theming](https://code.visualstudio.com/api/extension-capabilities/theming), [syntax highlighting](https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide), and [semantic highlighting](https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide).

## 2. What the research actually supports

### 2.1 Syntax highlighting is useful, but “more colors” is not established

Sarkar’s controlled, randomized, within-subject eye-tracking study involved ten participants and found significantly faster task completion with syntax highlighting, with a weaker effect among more experienced programmers. A later novice-focused study by Hannebauer, Hesenius, and Gruhn did not establish a general comprehension benefit for novices. The evidence therefore supports retaining meaningful highlighting, but does not show that assigning a distinct hue to every lexical class improves comprehension.

Design consequence: Acuity uses five routine accent families and leaves ordinary variables, properties, operators, and punctuation neutral. This is a conservative inference from mixed evidence, not a claim that five is a biologically optimal number.

Sources:

- Advait Sarkar, [“The impact of syntax colouring on program comprehension”](https://ppig.org/files/2015-PPIG-26th-Sarkar1.pdf), PPIG 2015.
- Christoph Hannebauer, Marc Hesenius, and Volker Gruhn, [“Does syntax highlighting help programming novices?”](https://doi.org/10.1007/s10664-017-9579-0), *Empirical Software Engineering* 23, 2018.

### 2.2 Dark mode is a preference constraint, not a universal readability advantage

Buchner and Baumgartner found proofreading performance consistently better with positive polarity, independent of ambient lighting and chromaticity. Piepenbrock, Mayr, and Buchner later found a positive-polarity advantage for both younger and older adults in visual acuity and proofreading. Other work reports possible subjective-fatigue or comfort advantages for negative polarity in some conditions, so performance and comfort should not be conflated.

Design consequence: Acuity does not claim to beat a well-designed light theme for every reader. It aims to be a stronger dark theme for users who choose dark mode.

Sources:

- Axel Buchner and Nina Baumgartner, [“Text-background polarity affects performance irrespective of ambient illumination and colour contrast”](https://pubmed.ncbi.nlm.nih.gov/17510822/), *Ergonomics* 50(7), 2007.
- Cornelia Piepenbrock, Susanne Mayr, and Axel Buchner, [“Positive display polarity is advantageous for both younger and older adults”](https://pubmed.ncbi.nlm.nih.gov/23654206/), *Ergonomics* 56(7), 2013.

### 2.3 Luminance/lightness contrast is more reliable than hue preference

Li et al. tested 230 colored-text/neutral-background images with 20 participants. Comfort decreased as text approached the background; text hue was not significant, while a model incorporating lightness and chroma best predicted comfort. Humar et al. tested 56 combinations with 308 participants and found that color combinations materially affected legibility. WCAG is not a source-code standard, but its 4.5:1 and 7:1 text thresholds provide transparent, repeatable accessibility proxies.

Design consequence:

- Routine syntax accents target at least 7:1.
- Comments target at least 4.5:1.
- Main text is high contrast but not pure white on pure black.
- Exact hues are selected primarily for categorical separation, not because a study says “functions should be green.”

Sources:

- Zhenzhen Li et al., [“Visual comfort models based on coloured text and neutral background combinations”](https://doi.org/10.1016/j.visres.2024.108524), *Vision Research* 227, 2025.
- Iztok Humar et al., [“The impact of color combinations on the legibility of text presented on LCDs”](https://pubmed.ncbi.nlm.nih.gov/24874503/), *Applied Ergonomics* 45(6), 2014.
- W3C, [WCAG 2.2 contrast criteria](https://www.w3.org/TR/WCAG22/#contrast-minimum) and [7:1 technique G17](https://www.w3.org/WAI/WCAG22/Techniques/general/G17).

### 2.4 Excessive or poorly placed salience can be harmful

Crameri, Shephard, and Heron show why nonuniform “rainbow” schemes can create artificial perceptual emphasis and why perceptual uniformity and color-vision accessibility matter. Their work concerns scientific visualization rather than code, so it does not prove that coding accents must have identical lightness. It does establish the broader design principle that arbitrary color salience can distort attention.

Design consequence: routine accents occupy a controlled contrast band of 7.53:1–10.34:1, punctuation is neutral, and the brightest alarm-like color is not used for ordinary syntax.

Source: Fabio Crameri, Grace E. Shephard, and Philip J. Heron, [“The misuse of colour in science communication”](https://doi.org/10.1038/s41467-020-19160-7), *Nature Communications* 11, 2020.

### 2.5 Red is exceptional; dark blue must be lightened

Fan et al. found the greatest visual fatigue with red text under negative polarity in their tested nighttime conditions. Zhu et al. found blue font on black had the longest response time among their tested red/green/blue combinations. These are task- and stimulus-specific findings, so they should not be overgeneralized into absolute bans.

Design consequence:

- Coral is reserved for invalid tokens, errors, and deletions.
- The blue family is a light sky blue at 7.53:1, not a dark saturated blue on black.
- Amber is assigned to sparse structural keywords and warnings rather than large bodies of text.

Sources:

- Qiangqiang Fan et al., [“The Effect of Ambient Illumination and Text Color on Visual Fatigue under Negative Polarity”](https://doi.org/10.3390/s24113516), *Sensors* 24(11), 2024.
- W. Zhu et al., [“Font and background color combinations influence recognition efficiency: A novel method via primary color Euclidean distance and response surface analysis”](https://doi.org/10.1016/j.displa.2024.102873), *Displays* 85, 2024. The article reports the blue-on-black result for its tested conditions.

### 2.6 Color must not be the sole semantic channel

WCAG’s “Use of Color” principle requires additional visual means when color communicates information. Machado, Oliveira, and Fernandes provide a physiologically based model for simulating color-vision deficiency.

Design consequence:

- Control-flow keywords are amber **and bold**.
- Comments are gray **and italic**.
- Attributes/decorators are magenta **and italic**.
- Invalid tokens are coral **and underlined**.
- Readonly declarations receive semantic-token styling.
- The palette is audited using severe Machado simulation matrices.

Sources:

- W3C, [WCAG 2.2: Use of Color](https://www.w3.org/TR/WCAG22/#use-of-color).
- Gustavo M. Machado, Manuel M. Oliveira, and Leandro A. F. Fernandes, [“A physiologically-based model for simulation of color vision deficiency”](https://doi.org/10.1109/TVCG.2009.113), *IEEE Transactions on Visualization and Computer Graphics* 15(6), 2009.

## 3. Deriving the exact palette

### 3.1 Fixed constraints

The palette was generated and then adjusted under the following constraints:

- Background: very dark, low-chroma neutral surface.
- Foreground: low-chroma text with contrast materially above 7:1, but not pure white.
- Comments: minimum 4.5:1 and visually subordinate to code.
- Five routine accents: each at least 7:1; no routine red.
- Accent contrast spread: constrained to avoid one routine lexical category becoming an alarm signal solely because it is much brighter.
- Color-vision robustness: maximize the worst pairwise CIE Lab distance after severe protanopia, deuteranopia, and tritanopia simulations.
- Redundant font styles for categories that may converge under color-vision deficiency.

CIE76 distance is used only as a screening metric. It is not a guarantee of equal perceptual difference and is not a substitute for human evaluation.

### 3.2 Final palette and semantic assignments

| Role | Hex | Contrast on `#17191D` | Assignment | Evidence-to-choice chain |
|---|---:|---:|---|---|
| Editor background | `#17191D` | — | Main editor surface | Low-chroma near-black permits strong contrast without pure-black/pure-white maximum contrast; background lightness and chroma affect comfort. |
| Main foreground | `#CBD3D8` | 11.61:1 | Variables, properties, normal code | Strong text/background separation; low chroma prevents ordinary text from competing with syntax categories. |
| Comment | `#8696A0` | 5.77:1 | Comments and documentation | Above 4.5:1 while lower than routine code; italic adds a non-color cue. |
| Amber | `#D5A351` | 7.70:1 | Keywords, control flow, warnings, escape sequences | High contrast and sparse use; yellow/amber performs well in Fan et al.’s tested negative-polarity conditions. Bold is added to control flow. |
| Teal | `#4ACFB5` | 9.12:1 | Strings and links | High contrast, separated from other optimized categories, and avoids dark blue-on-black. |
| Green | `#AECC8C` | 9.90:1 | Functions, methods, regular expressions | High contrast and optimized categorical separation. No claim is made that green has an intrinsic “function” meaning. |
| Magenta | `#E3B8EC` | 10.34:1 | Numbers, constants, attributes, decorators | High contrast and strong simulated CVD separation from teal/green; attributes add italics. It is a pale magenta rather than high-saturation red. |
| Sky | `#70AFE8` | 7.53:1 | Types, classes, interfaces, namespaces | Lightened blue avoids the low-luminance blue-on-black condition associated with poor response time in Zhu et al. |
| Coral | `#F0A29A` | 8.67:1 | Errors, invalid tokens, deletions only | Red-family color is reserved for exceptional states because routine red text produced the greatest fatigue in Fan et al.’s tested conditions. Underline or editor diagnostics provide additional cues. |
| Neutral operator text | `#AEB7BD` | 8.49:1 | Operators and punctuation | Keeps the reading skeleton visible without assigning another categorical hue. |

### 3.3 Color-vision simulation result

For the five routine accents, the smallest pairwise CIE76 distance was:

| Viewing model | Minimum pairwise distance | Closest pair |
|---|---:|---|
| Normal color vision | 33.83 | Teal / green |
| Severe protanopia simulation | 11.42 | Magenta / sky |
| Severe deuteranopia simulation | 18.67 | Teal / magenta |
| Severe tritanopia simulation | 14.15 | Teal / sky |

The first draft had a deuteranopia minimum of only 2.57 between lavender and sky. The final palette deliberately varies both hue and lightness to remove that collapse. This is why the routine accents are not perfectly equal in lightness: simulated CVD separation was treated as a stronger constraint than aesthetic uniformity.

## 4. Canonical comparison

The exact output is in `audit-output.txt` and reproducible with `scripts/audit_palette.py`.

| Theme | Main text contrast | Comment contrast |
|---|---:|---:|
| One Dark Pro | 6.57:1 | 2.32:1 |
| Dracula | 13.36:1 | 3.03:1 |
| Catppuccin Mocha | 11.34:1 | 3.36:1 |
| Tokyo Night | 8.10:1 | 2.76:1 |
| Gruvbox Dark | 10.75:1 | 4.02:1 |
| Nord | 9.25:1 | 2.43:1 |
| Solarized Dark | 4.75:1 | 2.79:1 |
| GitHub Dark | 12.26:1 | 6.15:1 |
| **Acuity Dark** | **11.61:1** | **5.77:1** |

Acuity does not have the highest main-text or comment contrast in every row. Its intended advantage is the combination of high routine-token contrast, readable comments, controlled salience, semantic redundancy, and optimized simulated CVD separation.

## 5. C#-specific implementation

VS Code can resolve C# source through TextMate scopes and semantic tokens. Acuity maps:

- namespaces, classes, structs, interfaces, enums, and type parameters → sky;
- functions and methods → green;
- strings → teal;
- numbers, enum members, readonly variables, and constants → magenta;
- keywords/modifiers → amber;
- parameters, variables, fields, and properties → neutral foreground;
- attributes/decorators → magenta italic;
- comments → gray italic;
- invalid tokens and diagnostics → coral plus non-color diagnostic styling.

This mapping limits “rainbow code.” The aim is fast structural parsing: control, literal data, callable behavior, and type structure are distinct; local names and punctuation remain visually stable.

## 6. What is not proven

- No controlled study has compared Acuity against all popular VS Code themes.
- WCAG contrast ratios are an accessibility proxy developed for web content, not a complete source-code readability model.
- CIE76 and CVD simulations are screening tools, not direct measurements of programmer comprehension.
- Individual vision, age, display calibration, font, anti-aliasing, brightness, ambient illumination, language grammar, and familiarity can change outcomes.
- Positive-polarity research means a dark theme should not be presented as universally superior to light mode.
- Semantic color meaning is partly conventional. The exact role-to-hue mapping should be evaluated through use, not treated as a biological fact.

## 7. Recommended evaluation protocol

Use the theme for at least several normal work sessions, then compare it with the current theme under matched font, brightness, and room lighting. Record:

1. time to locate method declarations, return paths, exceptions, and string literals;
2. frequency of rereading comments;
3. visual discomfort after 30–60 minutes;
4. missed diagnostics or diff markers;
5. whether any two semantic categories are repeatedly confused;
6. screenshots under a CVD simulator and on the actual primary monitor.

A stronger follow-up would randomize equivalent code-comprehension tasks across themes and measure accuracy, completion time, and subjective fatigue.
