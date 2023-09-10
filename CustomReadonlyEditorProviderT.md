## CustomReadonlyEditorProvider&lt;T&gt;

Provider for readonly custom editors that use a custom document model.

Custom editors use CustomDocument as their document model instead of a TextDocument.

You should use this type of custom editor when dealing with binary files or more complex scenarios. For simple text based documents, use CustomTextEditorProvider instead.

## Methods

### openCustomDocument

```typescript
openCustomDocument(uri: Uri, openContext: CustomDocumentOpenContext, token: CancellationToken): T | Thenable<T>
```

### resolveCustomEditor

```typescript
resolveCustomEditor(document: T, webviewPanel: WebviewPanel, token: CancellationToken): void | Thenable<void>
```

[Uri]: Uri.md
[CustomDocumentOpenContext]: CustomDocumentOpenContext.md
[WebviewPanel]: WebviewPanel.md
[CancellationToken]: CancellationToken.md
