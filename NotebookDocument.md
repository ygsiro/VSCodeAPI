# NotebookDocument

Represents a notebook which itself is a sequence of code or markup cells. Notebook documents are created from notebook data.

## Properties

### cellCount

```typescript
cellCount: number
```

### isClosed

```typescript
isClosed: boolean
```

### isDirty

```typescript
isDirty: boolean
```

### isUntitled

```typescript
isUntitled: boolean
```

### metadata

```typescript
metadata:
```

### notebookType

```typescript
notebookType: string
```

### uri

```typescript
uri: Uri
```

### version

```typescript
version: number
```

## Methods

### cellAt

```typescript
cellAt(index: number): NotebookCell
```

### getCells

```typescript
getCells(range?: NotebookRange): NotebookCell[]
```

### save

```typescript
save(): Thenable<boolean>
```

[NotebookRange]: NotebookRange.md
[NotebookCell]: NotebookCell.md
[Uri]: Uri.md
