# FileDecorationProvider

The decoration provider interfaces defines the contract between extensions and file decorations.

## Events

### onDidChangeFileDecorations

```typescript
onDidChangeFileDecorations?: Event<Uri | Uri[]>
```

## Methods

### provideFileDecoration

```typescript
provideFileDecoration(uri: Uri, token: CancellationToken): ProviderResult<FileDecoration>
```

