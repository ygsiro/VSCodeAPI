# ReferenceProvider

The reference provider interface defines the contract between extensions and the find references-feature.

## Methods

### provideReferences

```typescript
provideReferences(document: TextDocument, position: Position, context: ReferenceContext, token: CancellationToken): ProviderResult<Location[]>
```

