# SignatureHelpProvider

The signature help provider interface defines the contract between extensions and the parameter hints-feature.

## Methods

### provideSignatureHelp

```typescript
provideSignatureHelp(document: TextDocument, position: Position, token: CancellationToken, context: SignatureHelpContext): ProviderResult<SignatureHelp>
```

