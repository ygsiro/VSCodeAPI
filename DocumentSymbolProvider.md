# DocumentSymbolProvider

The document symbol provider interface defines the contract between extensions and the go to symbol-feature.

## Methods

### provideDocumentSymbols

```typescript
provideDocumentSymbols(document: TextDocument, token: CancellationToken): ProviderResult<DocumentSymbol[] | SymbolInformation[]>
```

