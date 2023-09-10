# TextEdit

A text edit represents edits that should be applied to a document.

## Static

### delete

```typescript
delete(range: Range): TextEdit
```

### insert

```typescript
insert(position: Position, newText: string): TextEdit
```

### replace

```typescript
replace(range: Range, newText: string): TextEdit
```

### setEndOfLine

```typescript
setEndOfLine(eol: EndOfLine): TextEdit
```

## Constructors

```typescript
new TextEdit(range: Range, newText: string): TextEdit
```

## Properties

### newEol

```typescript
newEol?: EndOfLine
```

### newText

```typescript
newText: string
```

### range

```typescript
range: Range
```

[Range]: Range.md
[Position]: Position.md
[EndOfLine]: EndOfLine.md
