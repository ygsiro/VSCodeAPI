# CallHierarchyItem

Represents programming constructs like functions or constructors in the context of call hierarchy.

## Constructors

```typescript
new CallHierarchyItem(kind: SymbolKind, name: string, detail: string, uri: Uri, range: Range, selectionRange: Range): CallHierarchyItem
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

