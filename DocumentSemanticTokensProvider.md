# DocumentSemanticTokensProvider

The document semantic tokens provider interface defines the contract between extensions and semantic tokens.

## Events

### onDidChangeSemanticTokens

```typescript
onDidChangeSemanticTokens?: Event<void>
```

## Methods

### provideDocumentSemanticTokens

```typescript
provideDocumentSemanticTokens(document: TextDocument, token: CancellationToken): ProviderResult<SemanticTokens>
```

### provideDocumentSemanticTokensEdits

```typescript
provideDocumentSemanticTokensEdits(document: TextDocument, previousResultId: string, token: CancellationToken): ProviderResult<SemanticTokens | SemanticTokensEdits>
```

[SemanticTokensEdits]: SemanticTokensEdits.md
[Event]: EventT.md
[ProviderResult]: ProviderResultT.md
[TextDocument]: TextDocument.md
[SemanticTokens]: SemanticTokens.md
[CancellationToken]: CancellationToken.md
