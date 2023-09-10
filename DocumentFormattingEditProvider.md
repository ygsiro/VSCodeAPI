# DocumentFormattingEditProvider

The document formatting provider interface defines the contract between extensions and the formatting-feature.

## Methods

### provideDocumentFormattingEdits

```typescript
provideDocumentFormattingEdits(document: TextDocument, options: FormattingOptions, token: CancellationToken): ProviderResult<TextEdit[]>
```

[FormattingOptions]: FormattingOptions.md
[ProviderResult]: ProviderResultT.md
[TextEdit]: TextEdit.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
