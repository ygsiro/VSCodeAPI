# HoverProvider

The hover provider interface defines the contract between extensions and the hover-feature.

## Methods

### provideHover

```typescript
provideHover(document: TextDocument, position: Position, token: CancellationToken): ProviderResult<Hover>
```

[Hover]: Hover.md
[ProviderResult]: ProviderResultT.md
[Position]: Position.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
