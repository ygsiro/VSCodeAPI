# ProcessExecution

The execution of a task happens as an external process without shell interaction.

## Constructors

```typescript
//1)
new ProcessExecution(process: string, options?: ProcessExecutionOptions): ProcessExecution
//2)
new ProcessExecution(process: string, args: string[], options?: ProcessExecutionOptions): ProcessExecution
```

## Properties

### args

```typescript
args: string[]
```

### options

```typescript
options?: ProcessExecutionOptions
```

### process

```typescript
process: string
```

