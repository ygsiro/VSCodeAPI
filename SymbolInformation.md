# SymbolInformation

Represents information about programming constructs like variables, classes, interfaces etc.

## Constructors

```typescript
new SymbolInformation(name: string, kind: SymbolKind, containerName: string, location: Location): SymbolInformation
```

```typescript
new SymbolInformation(name: string, kind: SymbolKind, range: Range, uri?: Uri, containerName?: string): SymbolInformation
```

## Properties

### containerName

```typescript
containerName: string
```

### kind

```typescript
kind: SymbolKind
```

### location

```typescript
location: Location
```

### name

```typescript
name: string
```

### tags

```typescript
tags?: readonly Deprecated[]
```

[Range]: Range.md
[Uri]: Uri.md
[SymbolKind]: SymbolKind.md
[Locaation]: Location.md
