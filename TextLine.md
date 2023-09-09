# TextLine

Represents a line of text, such as a line of source code.

TextLine objects are immutable. When a document changes, previously retrieved lines will not represent the latest state.

## Properties

### firstNonWhitespaceCharacterIndex

```typescript
firstNonWhitespaceCharacterIndex: number
```

### isEmptyOrWhitespace

```typescript
isEmptyOrWhitespace: boolean
```

### lineNumber

```typescript
lineNumber: number
```

### range

```typescript
range: Range
```

### rangeIncludingLineBreak

```typescript
rangeIncludingLineBreak: Range
```

### text

```typescript
text: string
```

