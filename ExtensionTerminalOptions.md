# ExtensionTerminalOptions

Value-object describing what options a virtual process terminal should use.

## Properties

### color

```typescript
color?: ThemeColor
```

### iconPath

```typescript
iconPath?: Uri | ThemeIcon | {dark: Uri, light: Uri}
```

### isTransient

```typescript
isTransient?: boolean
```

### location

```typescript
location?: TerminalEditorLocationOptions | TerminalSplitLocationOptions | TerminalLocation
```

### name

```typescript
name: string
```

### pty

```typescript
pty: Pseudoterminal
```

[ThemeIcon]: ThemeIcon.md
[TerminalEditorLocationOptions]: TerminalEditorLocationOptions.md
[ThemeColor]: ThemeColor.md
[Uri]: Uri.md
[TerminalLocation]: TerminalLocation.md
[Pseudoterminal]: Pseudoterminal.md
[TerminalSplitLocationOptions]: TerminalSplitLocationOptions.md
