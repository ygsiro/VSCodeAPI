# ImplementationProvider

The implementation provider interface defines the contract between extensions and the go to implementation feature.

## Methods

### provideImplementation

```typescript
provideImplementation(document: TextDocument, position: Position, token: CancellationToken): ProviderResult<Definition | LocationLink[]>
```

[LocationLink]: LocationLink.md
[ProviderResult]: ProviderResultT.md
[Definition]: Definition.md
[Position]: Position.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
