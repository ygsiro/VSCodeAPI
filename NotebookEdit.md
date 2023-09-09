# NotebookEdit

A notebook edit represents edits that should be applied to the contents of a notebook.

## Static

### deleteCells

```typescript
deleteCells(range: NotebookRange): NotebookEdit
```

### insertCells

```typescript
insertCells(index: number, newCells: NotebookCellData[]): NotebookEdit
```

### replaceCells

```typescript
replaceCells(range: NotebookRange, newCells: NotebookCellData[]): NotebookEdit
```

### updateCellMetadata

```typescript
updateCellMetadata(index: number, newCellMetadata: ): NotebookEdit
```

### updateNotebookMetadata

```typescript
updateNotebookMetadata(newNotebookMetadata: ): NotebookEdit
```

## Constructors

```typescript
new NotebookEdit(range: NotebookRange, newCells: NotebookCellData[]): NotebookEdit
```

## Properties

### newCellMetadata

```typescript
newCellMetadata?:
```

### newCells

```typescript
newCells: NotebookCellData[]
```

### newNotebookMetadata

```typescript
newNotebookMetadata?:
```

### range

```typescript
range: NotebookRange
```

