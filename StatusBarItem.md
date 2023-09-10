# StatusBarItem

A status bar item is a status bar contribution that can show text and icons and run a command on click.

## Properties

### accessibilityInformation

```typescript
accessibilityInformation: AccessibilityInformation
```

### alignment

```typescript
alignment: StatusBarAlignment
```

### backgroundColor

```typescript
backgroundColor: ThemeColor
```

### color

```typescript
color: string | ThemeColor
```

### command

```typescript
command: string | Command
```

### id

```typescript
id: string
```

### name

```typescript
name: string
```

### priority

```typescript
priority: number
```

### text

```typescript
text: string
```

### tooltip

```typescript
tooltip: string | MarkdownString
```

## Methods

### dispose

```typescript
dispose(): void
```

### hide

```typescript
hide(): void
```

### show

```typescript
show(): void
```

[MarkdownString]: MarkdownString.md
[StatusBarAlignment]: StatusBarAlignment.md
[AccessibilityInformation]: AccessibilityInformation.md
[ThemeColor]: ThemeColor.md
[Command]: Command.md
