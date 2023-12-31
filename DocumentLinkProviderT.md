## DocumentLinkProvider&lt;T&gt;

The document link provider defines the contract between extensions and feature of showing links in the editor.

## Methods

### provideDocumentLinks

```typescript
provideDocumentLinks(document: TextDocument, token: CancellationToken): ProviderResult<T[]>
```

### resolveDocumentLink

```typescript
resolveDocumentLink(link: T, token: CancellationToken): ProviderResult<T>
```

[ProviderResult]: ProviderResultT.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
