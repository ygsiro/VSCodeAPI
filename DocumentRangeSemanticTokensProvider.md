# DocumentRangeSemanticTokensProvider

The document range semantic tokens provider interface defines the contract between extensions and semantic tokens.

## Methods

### provideDocumentRangeSemanticTokens

```typescript
provideDocumentRangeSemanticTokens(document: TextDocument, range: Range, token: CancellationToken): ProviderResult<SemanticTokens>
```

