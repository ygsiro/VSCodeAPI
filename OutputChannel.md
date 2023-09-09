# OutputChannel

An output channel is a container for readonly textual information.

To get an instance of an OutputChannel use createOutputChannel.

## Properties

### name

```typescript
name: string
```

## Methods

### append

```typescript
append(value: string): void
```

### appendLine

```typescript
appendLine(value: string): void
```

### clear

```typescript
clear(): void
```

### dispose

```typescript
dispose(): void
```

### hide

```typescript
hide(): void
```

### replace

```typescript
replace(value: string): void
```

### show

```typescript
show(preserveFocus?: boolean): void
```

### show

```typescript
show(column?: ViewColumn, preserveFocus?: boolean): void
```

