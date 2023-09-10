# RenameProvider

The rename provider interface defines the contract between extensions and the rename-feature.

## Methods

### prepareRename

```typescript
prepareRename(document: TextDocument, position: Position, token: CancellationToken): ProviderResult<Range | {placeholder: string, range: Range}>
```

### provideRenameEdits

```typescript
provideRenameEdits(document: TextDocument, position: Position, newName: string, token: CancellationToken): ProviderResult<WorkspaceEdit>
```

[ProviderResult]: ProviderResultT.md
[Range]: Range.md
[Position]: Position.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
[WorkspaceEdit]: WorkspaceEdit.md
