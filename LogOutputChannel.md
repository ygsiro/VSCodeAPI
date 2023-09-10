# LogOutputChannel

A channel for containing log output.

To get an instance of a LogOutputChannel use createOutputChannel.

## Events

### onDidChangeLogLevel

```typescript
onDidChangeLogLevel: Event<LogLevel>
```

## Properties

### logLevel

```typescript
logLevel: LogLevel
```

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

### debug

```typescript
debug(message: string, ...args: any[]): void
```

### dispose

```typescript
dispose(): void
```

### error

```typescript
error(error: string | Error, ...args: any[]): void
```

### hide

```typescript
hide(): void
```

### info

```typescript
info(message: string, ...args: any[]): void
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

### trace

```typescript
trace(message: string, ...args: any[]): void
```

### warn

```typescript
warn(message: string, ...args: any[]): void
```

[ViewColumn]: ViewColumn.md
[debug]: debug.md
[Event]: EventT.md
[LogLevel]: LogLevel.md
