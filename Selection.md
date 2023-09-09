# Selection

Represents a text selection in an editor.

## Constructors

```typescript
new Selection(anchor: Position, active: Position): Selection
```

```typescript
new Selection(anchorLine: number, anchorCharacter: number, activeLine: number, activeCharacter: number): Selection
```

## Properties

### active

```typescript
active: Position
```

### anchor

```typescript
anchor: Position
```

### end

```typescript
end: Position
```

### isEmpty

```typescript
isEmpty: boolean
```

### isReversed

```typescript
isReversed: boolean
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

