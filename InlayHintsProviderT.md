## InlayHintsProvider&lt;T&gt;

The inlay hints provider interface defines the contract between extensions and the inlay hints feature.

## Events

### onDidChangeInlayHints

```typescript
onDidChangeInlayHints?: Event<void>
```

## Methods

### provideInlayHints

```typescript
provideInlayHints(document: TextDocument, range: Range, token: CancellationToken): ProviderResult<T[]>
```

### resolveInlayHint

```typescript
resolveInlayHint(hint: T, token: CancellationToken): ProviderResult<T>
```

