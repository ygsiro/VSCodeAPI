## CodeLensProvider&lt;T&gt;

A code lens provider adds commands to source text. The commands will be shown as dedicated horizontal lines in between the source text.

## Events

### onDidChangeCodeLenses

```typescript
onDidChangeCodeLenses?: Event<void>
```

## Methods

### provideCodeLenses

```typescript
provideCodeLenses(document: TextDocument, token: CancellationToken): ProviderResult<T[]>
```

### resolveCodeLens

```typescript
resolveCodeLens(codeLens: T, token: CancellationToken): ProviderResult<T>
```

[Event]: EventT.md
[ProviderResult]: ProviderResultT.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
