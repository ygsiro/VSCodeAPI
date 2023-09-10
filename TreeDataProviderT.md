## TreeDataProvider&lt;T&gt;

A data provider that provides tree data

## Events

### onDidChangeTreeData

```typescript
onDidChangeTreeData?: Event<void | T | T[]>
```

## Methods

### getChildren

```typescript
getChildren(element?: T): ProviderResult<T[]>
```

### getParent

```typescript
getParent(element: T): ProviderResult<T>
```

### getTreeItem

```typescript
getTreeItem(element: T): TreeItem | Thenable<TreeItem>
```

### resolveTreeItem

```typescript
resolveTreeItem(item: TreeItem, element: T, token: CancellationToken): ProviderResult<TreeItem>
```

[Event]: EventT.md
[ProviderResult]: ProviderResultT.md
[TreeItem]: TreeItem.md
[CancellationToken]: CancellationToken.md
