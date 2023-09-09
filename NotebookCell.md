# NotebookCell

Represents a cell of a notebook, either a code-cell or markup-cell.

NotebookCell instances are immutable and are kept in sync for as long as they are part of their notebook.

## Properties

### document

```typescript
document: TextDocument
```

### executionSummary

```typescript
executionSummary: NotebookCellExecutionSummary
```

### index

```typescript
index: number
```

### kind

```typescript
kind: NotebookCellKind
```

### metadata

```typescript
metadata:
```

### notebook

```typescript
notebook: NotebookDocument
```

### outputs

```typescript
outputs: readonly NotebookCellOutput[]
```

