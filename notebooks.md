# notebooks

Namespace for notebooks.

The notebooks functionality is composed of three loosely coupled components:

NotebookSerializer enable the editor to open, show, and save notebooks
NotebookController own the execution of notebooks, e.g they create output from code cells.
NotebookRenderer present notebook output in the editor. They run in a separate context.

## Functions

### createNotebookController

```typescript
createNotebookController(id: string, notebookType: string, label: string, handler?: (cells: NotebookCell[], notebook: NotebookDocument, controller: NotebookController) => void | Thenable<void>): NotebookController
```

### createRendererMessaging

```typescript
createRendererMessaging(rendererId: string): NotebookRendererMessaging
```

### registerNotebookCellStatusBarItemProvider

```typescript
registerNotebookCellStatusBarItemProvider(notebookType: string, provider: NotebookCellStatusBarItemProvider): Disposable
```

