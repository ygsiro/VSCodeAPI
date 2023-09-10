# Pseudoterminal

Defines the interface of a terminal pty, enabling extensions to control a terminal.

## Events

### onDidChangeName

```typescript
onDidChangeName?: Event<string>
```

### onDidClose

```typescript
onDidClose?: Event<number | void>
```

### onDidOverrideDimensions

```typescript
onDidOverrideDimensions?: Event<TerminalDimensions>
```

### onDidWrite

```typescript
onDidWrite: Event<string>
```

## Methods

### close

```typescript
close(): void
```

### handleInput

```typescript
handleInput(data: string): void
```

### open

```typescript
open(initialDimensions: TerminalDimensions): void
```

### setDimensions

```typescript
setDimensions(dimensions: TerminalDimensions): void
```

[Event]: EventT.md
[TerminalDimensions]: TerminalDimensions.md
