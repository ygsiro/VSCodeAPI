# DocumentFormattingEditProvider

The document formatting provider interface defines the contract between extensions and the formatting-feature.

## Methods

### provideDocumentFormattingEdits

```typescript
provideDocumentFormattingEdits(document: TextDocument, options: FormattingOptions, token: CancellationToken): ProviderResult<TextEdit[]>
```

