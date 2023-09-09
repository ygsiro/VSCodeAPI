# TreeDragAndDropController<T>

Provides support for drag and drop in TreeView.

## Properties

### dragMimeTypes

```typescript
dragMimeTypes: readonly string[]
```

### dropMimeTypes

```typescript
dropMimeTypes: readonly string[]
```

## Methods

### handleDrag

```typescript
handleDrag(source: readonly T[], dataTransfer: DataTransfer, token: CancellationToken): void | Thenable<void>
```

### handleDrop

```typescript
handleDrop(target: T, dataTransfer: DataTransfer, token: CancellationToken): void | Thenable<void>
```

