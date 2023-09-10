# NotebookEditor

Represents a notebook editor that is attached to a notebook. Additional properties of the NotebookEditor are available in the proposed API, which will be finalized later.

## Properties

### notebook

```typescript
notebook: NotebookDocument
```

### selection

```typescript
selection: NotebookRange
```

### selections

```typescript
selections: readonly NotebookRange[]
```

### viewColumn

```typescript
viewColumn?: ViewColumn
```

### visibleRanges

```typescript
visibleRanges: readonly NotebookRange[]
```

## Methods

### revealRange

```typescript
revealRange(range: NotebookRange, revealType?: NotebookEditorRevealType): void
```

[NotebookRange]: NotebookRange.md
[NotebookDocument]: NotebookDocument.md
[ViewColumn]: ViewColumn.md
[NotebookEditorRevealType]: NotebookEditorRevealType.md
