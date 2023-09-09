# NotebookCellStatusBarItemProvider

A provider that can contribute items to the status bar that appears below a cell's editor.

## Events

### onDidChangeCellStatusBarItems

```typescript
onDidChangeCellStatusBarItems?: Event<void>
```

## Methods

### provideCellStatusBarItems

```typescript
provideCellStatusBarItems(cell: NotebookCell, token: CancellationToken): ProviderResult<NotebookCellStatusBarItem | NotebookCellStatusBarItem[]>
```

