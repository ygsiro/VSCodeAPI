# CustomTextEditorProvider

Provider for text based custom editors.

Text based custom editors use a TextDocument as their data model. This considerably simplifies implementing a custom editor as it allows the editor to handle many common operations such as undo and backup. The provider is responsible for synchronizing text changes between the webview and the TextDocument.

## Methods

### resolveCustomTextEditor

```typescript
resolveCustomTextEditor(document: TextDocument, webviewPanel: WebviewPanel, token: CancellationToken): void | Thenable<void>
```

