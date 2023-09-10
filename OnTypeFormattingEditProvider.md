# OnTypeFormattingEditProvider

The document formatting provider interface defines the contract between extensions and the formatting-feature.

## Methods

### provideOnTypeFormattingEdits

```typescript
provideOnTypeFormattingEdits(document: TextDocument, position: Position, ch: string, options: FormattingOptions, token: CancellationToken): ProviderResult<TextEdit[]>
```

[FormattingOptions]: FormattingOptions.md
[ProviderResult]: ProviderResultT.md
[Position]: Position.md
[TextEdit]: TextEdit.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
