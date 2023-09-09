# DocumentHighlightProvider

The document highlight provider interface defines the contract between extensions and the word-highlight-feature.

## Methods

### provideDocumentHighlights

```typescript
provideDocumentHighlights(document: TextDocument, position: Position, token: CancellationToken): ProviderResult<DocumentHighlight[]>
```

