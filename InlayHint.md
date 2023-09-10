# InlayHint

Inlay hint information.

## Constructors

```typescript
new InlayHint(position: Position, label: string | InlayHintLabelPart[], kind?: InlayHintKind): InlayHint
```

## Properties

### kind

```typescript
kind?: InlayHintKind
```

### label

```typescript
label: string | InlayHintLabelPart[]
```

### paddingLeft

```typescript
paddingLeft?: boolean
```

### paddingRight

```typescript
paddingRight?: boolean
```

### position

```typescript
position: Position
```

### textEdits

```typescript
textEdits?: TextEdit[]
```

### tooltip

```typescript
tooltip?: string | MarkdownString
```

[Position]: Position.md
[InlayHintKind]: InlayHintKind.md
[InlayHintLabelPart]: InlayHintLabelPart.md
[MarkdownString]: MarkdownString.md
[TextEdit]: TextEdit.md
