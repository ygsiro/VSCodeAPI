# TypeDefinitionProvider

The type definition provider defines the contract between extensions and the go to type definition feature.

## Methods

### provideTypeDefinition

```typescript
provideTypeDefinition(document: TextDocument, position: Position, token: CancellationToken): ProviderResult<Definition | LocationLink[]>
```

