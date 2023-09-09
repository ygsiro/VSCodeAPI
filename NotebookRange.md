# NotebookRange

A notebook range represents an ordered pair of two cell indices. It is guaranteed that start is less than or equal to end.

## Constructors

```typescript
new NotebookRange(start: number, end: number): NotebookRange
```

## Properties

### end

```typescript
end: number
```

### isEmpty

```typescript
isEmpty: boolean
```

### start

```typescript
start: number
```

## Methods

### with

```typescript
with(change: {end: number, start: number}): NotebookRange
```

