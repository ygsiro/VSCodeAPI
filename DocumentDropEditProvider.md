# DocumentDropEditProvider

Provider which handles dropping of resources into a text editor.

This allows users to drag and drop resources (including resources from external apps) into the editor. While dragging and dropping files, users can hold down shift to drop the file into the editor instead of opening it. Requires editor.dropIntoEditor.enabled to be on.

## Methods

### provideDocumentDropEdits

```typescript
provideDocumentDropEdits(document: TextDocument, position: Position, dataTransfer: DataTransfer, token: CancellationToken): ProviderResult<DocumentDropEdit>
```

[DataTransfer]: DataTransfer.md
[ProviderResult]: ProviderResultT.md
[Position]: Position.md
[DocumentDropEdit]: DocumentDropEdit.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
