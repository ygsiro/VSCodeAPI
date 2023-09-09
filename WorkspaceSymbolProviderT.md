## WorkspaceSymbolProvider&lt;T&gt;

The workspace symbol provider interface defines the contract between extensions and the symbol search-feature.

## Methods

### provideWorkspaceSymbols

```typescript
provideWorkspaceSymbols(query: string, token: CancellationToken): ProviderResult<T[]>
```

### resolveWorkspaceSymbol

```typescript
resolveWorkspaceSymbol(symbol: T, token: CancellationToken): ProviderResult<T>
```

