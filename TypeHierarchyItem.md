# TypeHierarchyItem

Represents an item of a type hierarchy, like a class or an interface.

## Constructors

```typescript
new TypeHierarchyItem(kind: SymbolKind, name: string, detail: string, uri: Uri, range: Range, selectionRange: Range): TypeHierarchyItem
```

## Properties

### detail

```typescript
detail?: string
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

### uri

```typescript
uri: Uri
```

[Range]: Range.md
[Uri]: Uri.md
[SymbolKind]: SymbolKind.md
