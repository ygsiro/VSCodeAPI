# DefinitionProvider

The definition provider interface defines the contract between extensions and the go to definition and peek definition features.

## Methods

### provideDefinition

```typescript
provideDefinition(document: TextDocument, position: Position, token: CancellationToken): ProviderResult<Definition | LocationLink[]>
```

