# NotebookController

A notebook controller represents an entity that can execute notebook cells. This is often referred to as a kernel.

There can be multiple controllers and the editor will let users choose which controller to use for a certain notebook. The notebookType-property defines for what kind of notebooks a controller is for and the updateNotebookAffinity-function allows controllers to set a preference for specific notebook documents. When a controller has been selected its onDidChangeSelectedNotebooks-event fires.

When a cell is being run the editor will invoke the executeHandler and a controller is expected to create and finalize a notebook cell execution. However, controllers are also free to create executions by themselves.

## Events

### onDidChangeSelectedNotebooks

```typescript
onDidChangeSelectedNotebooks: Event<{notebook: NotebookDocument, selected: boolean}>
```

## Properties

### description

```typescript
description?: string
```

### detail

```typescript
detail?: string
```

### executeHandler

```typescript
executeHandler: (cells: NotebookCell[], notebook: NotebookDocument, controller: NotebookController) => void | Thenable<void>
```

### id

```typescript
id: string
```

### interruptHandler

```typescript
interruptHandler?: (notebook: NotebookDocument) => void | Thenable<void>
```

### label

```typescript
label: string
```

### notebookType

```typescript
notebookType: string
```

### supportedLanguages

```typescript
supportedLanguages?: string[]
```

### supportsExecutionOrder

```typescript
supportsExecutionOrder?: boolean
```

## Methods

### createNotebookCellExecution

```typescript
createNotebookCellExecution(cell: NotebookCell): NotebookCellExecution
```

### dispose

```typescript
dispose(): void
```

### updateNotebookAffinity

```typescript
updateNotebookAffinity(notebook: NotebookDocument, affinity: NotebookControllerAffinity): void
```

[NotebookControllerAffinity]: NotebookControllerAffinity.md
[NotebookCellExecution]: NotebookCellExecution.md
[NotebookCell]: NotebookCell.md
[Event]: EventT.md
[NotebookDocument]: NotebookDocument.md
