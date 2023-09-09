# FoldingRange

A line based folding range. To be valid, start and end line must be bigger than zero and smaller than the number of lines in the document. Invalid ranges will be ignored.

## Constructors

```typescript
new FoldingRange(start: number, end: number, kind?: FoldingRangeKind): FoldingRange
```

## Properties

### end

```typescript
end: number
```

### kind

```typescript
kind?: FoldingRangeKind
```

### start

```typescript
start: number
```

