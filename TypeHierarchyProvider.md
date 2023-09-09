# TypeHierarchyProvider

The type hierarchy provider interface describes the contract between extensions and the type hierarchy feature.

## Methods

### prepareTypeHierarchy

```typescript
prepareTypeHierarchy(document: TextDocument, position: Position, token: CancellationToken): ProviderResult<TypeHierarchyItem | TypeHierarchyItem[]>
```

### provideTypeHierarchySubtypes

```typescript
provideTypeHierarchySubtypes(item: TypeHierarchyItem, token: CancellationToken): ProviderResult<TypeHierarchyItem[]>
```

### provideTypeHierarchySupertypes

```typescript
provideTypeHierarchySupertypes(item: TypeHierarchyItem, token: CancellationToken): ProviderResult<TypeHierarchyItem[]>
```

