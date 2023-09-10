# Range

A range represents an ordered pair of two positions. It is guaranteed that start.isBeforeOrEqual(end)

Range objects are immutable. Use the with, intersection, or union methods to derive new ranges from an existing range.

## Constructors

```typescript
new Range(start: Position, end: Position): Range
```

```typescript
new Range(startLine: number, startCharacter: number, endLine: number, endCharacter: number): Range
```

## Properties

### end

```typescript
end: Position
```

### isEmpty

```typescript
isEmpty: boolean
```

### isSingleLine

```typescript
isSingleLine: boolean
```

### start

```typescript
start: Position
```

## Methods

### contains

```typescript
contains(positionOrRange: Range | Position): boolean
```

### intersection

```typescript
intersection(range: Range): Range
```

### isEqual

```typescript
isEqual(other: Range): boolean
```

### union

```typescript
union(other: Range): Range
```

### with

```typescript
with(start?: Position, end?: Position): Range
```

### with

```typescript
with(change: {end: Position, start: Position}): Range
```

[Position]: Position.md
