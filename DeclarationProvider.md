# DeclarationProvider

The declaration provider interface defines the contract between extensions and the go to declaration feature.

## Methods

### provideDeclaration

```typescript
provideDeclaration(document: TextDocument, position: Position, token: CancellationToken): ProviderResult<Declaration>
```

[Declaration]: Declaration.md
[ProviderResult]: ProviderResultT.md
[Position]: Position.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
