# DocumentSymbol

Represents programming constructs like variables, classes, interfaces etc. that appear in a document. Document symbols can be hierarchical and they have two ranges: one that encloses its definition and one that points to its most interesting range, e.g. the range of an identifier.

## Constructors

```typescript
new DocumentSymbol(name: string, detail: string, kind: SymbolKind, range: Range, selectionRange: Range): DocumentSymbol
```

## Properties

### children

```typescript
children: DocumentSymbol[]
```

### detail

```typescript
detail: string
```

### kind

```typescript
kind: SymbolKind
```

### name

```typescript
name: string
```

### range

```typescript
range: Range
```

### selectionRange

```typescript
selectionRange: Range
```

### tags

```typescript
tags?: readonly Deprecated[]
```

[Range]: Range.md
[SymbolKind]: SymbolKind.md
