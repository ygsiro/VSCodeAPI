# Position

Represents a line and character position, such as the position of the cursor.

Position objects are immutable. Use the with or translate methods to derive new positions from an existing position.

## Constructors

```typescript
new Position(line: number, character: number): Position
```

## Properties

### character

```typescript
character: number
```

### line

```typescript
line: number
```

## Methods

### compareTo

```typescript
compareTo(other: Position): number
```

### isAfter

```typescript
isAfter(other: Position): boolean
```

### isAfterOrEqual

```typescript
isAfterOrEqual(other: Position): boolean
```

### isBefore

```typescript
isBefore(other: Position): boolean
```

### isBeforeOrEqual

```typescript
isBeforeOrEqual(other: Position): boolean
```

### isEqual

```typescript
isEqual(other: Position): boolean
```

### translate

```typescript
//1)
translate(lineDelta?: number, characterDelta?: number): Position
//2)
translate(change: {characterDelta: number, lineDelta: number}): Position
```

### with

```typescript
//1)
with(line?: number, character?: number): Position
//2)
with(change: {character: number, line: number}): Position
```

