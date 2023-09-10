# NotebookCellExecution

A NotebookCellExecution is how notebook controller modify a notebook cell as it is executing.

When a cell execution object is created, the cell enters the [NotebookCellExecutionState.Pending Pending](#NotebookCellExecutionState.Pending Pending) state. When start(...) is called on the execution task, it enters the [NotebookCellExecutionState.Executing Executing](#NotebookCellExecutionState.Executing Executing) state. When end(...) is called, it enters the [NotebookCellExecutionState.Idle Idle](#NotebookCellExecutionState.Idle Idle) state.

## Properties

### cell

```typescript
cell: NotebookCell
```

### executionOrder

```typescript
executionOrder: number
```

### token

```typescript
token: CancellationToken
```

## Methods

### appendOutput

```typescript
appendOutput(out: NotebookCellOutput | readonly NotebookCellOutput[], cell?: NotebookCell): Thenable<void>
```

### appendOutputItems

```typescript
appendOutputItems(items: NotebookCellOutputItem | readonly NotebookCellOutputItem[], output: NotebookCellOutput): Thenable<void>
```

### clearOutput

```typescript
clearOutput(cell?: NotebookCell): Thenable<void>
```

### end

```typescript
end(success: boolean, endTime?: number): void
```

### replaceOutput

```typescript
replaceOutput(out: NotebookCellOutput | readonly NotebookCellOutput[], cell?: NotebookCell): Thenable<void>
```

### replaceOutputItems

```typescript
replaceOutputItems(items: NotebookCellOutputItem | readonly NotebookCellOutputItem[], output: NotebookCellOutput): Thenable<void>
```

### start

```typescript
start(startTime?: number): void
```

[NotebookCellOutputItem]: NotebookCellOutputItem.md
[CancellationToken]: CancellationToken.md
[NotebookCell]: NotebookCell.md
[NotebookCellOutput]: NotebookCellOutput.md
