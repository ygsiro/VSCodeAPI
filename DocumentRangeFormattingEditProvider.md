# DocumentRangeFormattingEditProvider

The document formatting provider interface defines the contract between extensions and the formatting-feature.

## Methods

### provideDocumentRangeFormattingEdits

```typescript
provideDocumentRangeFormattingEdits(document: TextDocument, range: Range, options: FormattingOptions, token: CancellationToken): ProviderResult<TextEdit[]>
```

### provideDocumentRangesFormattingEdits

```typescript
provideDocumentRangesFormattingEdits(document: TextDocument, ranges: Range[], options: FormattingOptions, token: CancellationToken): ProviderResult<TextEdit[]>
```

[FormattingOptions]: FormattingOptions.md
[ProviderResult]: ProviderResultT.md
[Range]: Range.md
[TextEdit]: TextEdit.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
