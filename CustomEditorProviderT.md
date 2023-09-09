# CustomEditorProvider<T>

Provider for editable custom editors that use a custom document model.

Custom editors use CustomDocument as their document model instead of a TextDocument. This gives extensions full control over actions such as edit, save, and backup.

You should use this type of custom editor when dealing with binary files or more complex scenarios. For simple text based documents, use CustomTextEditorProvider instead.

## Events

### onDidChangeCustomDocument

```typescript
onDidChangeCustomDocument: Event<CustomDocumentEditEvent<T>> | Event<CustomDocumentContentChangeEvent<T>>
```

## Methods

### backupCustomDocument

```typescript
backupCustomDocument(document: T, context: CustomDocumentBackupContext, cancellation: CancellationToken): Thenable<CustomDocumentBackup>
```

### openCustomDocument

```typescript
openCustomDocument(uri: Uri, openContext: CustomDocumentOpenContext, token: CancellationToken): T | Thenable<T>
```

### resolveCustomEditor

```typescript
resolveCustomEditor(document: T, webviewPanel: WebviewPanel, token: CancellationToken): void | Thenable<void>
```

### revertCustomDocument

```typescript
revertCustomDocument(document: T, cancellation: CancellationToken): Thenable<void>
```

### saveCustomDocument

```typescript
saveCustomDocument(document: T, cancellation: CancellationToken): Thenable<void>
```

### saveCustomDocumentAs

```typescript
saveCustomDocumentAs(document: T, destination: Uri, cancellation: CancellationToken): Thenable<void>
```

