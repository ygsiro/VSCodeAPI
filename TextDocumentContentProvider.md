# TextDocumentContentProvider

A text document content provider allows to add readonly documents to the editor, such as source from a dll or generated html from md.

Content providers are registered for a uri-scheme. When a uri with that scheme is to be loaded the content provider is asked.

## Events

### onDidChange

```typescript
onDidChange?: Event<Uri>
```

## Methods

### provideTextDocumentContent

```typescript
provideTextDocumentContent(uri: Uri, token: CancellationToken): ProviderResult<string>
```

