# NotebookCellData

NotebookCellData is the raw representation of notebook cells. Its is part of NotebookData.

## Constructors

```typescript
new NotebookCellData(kind: NotebookCellKind, value: string, languageId: string): NotebookCellData
```

## Properties

### executionSummary

```typescript
executionSummary?: NotebookCellExecutionSummary
```

### kind

```typescript
kind: NotebookCellKind
```

### languageId

```typescript
languageId: string
```

### metadata

```typescript
metadata?:
```

### outputs

```typescript
outputs?: NotebookCellOutput[]
```

### value

```typescript
value: string
```

[NotebookCellOutput]: NotebookCellOutput.md
[NotebookCellExecutionSummary]: NotebookCellExecutionSummary.md
[NotebookCellKind]: NotebookCellKind.md
