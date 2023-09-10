# ReferenceProvider

The reference provider interface defines the contract between extensions and the find references-feature.

## Methods

### provideReferences

```typescript
provideReferences(document: TextDocument, position: Position, context: ReferenceContext, token: CancellationToken): ProviderResult<Location[]>
```

[ReferenceContext]: ReferenceContext.md
[ProviderResult]: ProviderResultT.md
[Position]: Position.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
