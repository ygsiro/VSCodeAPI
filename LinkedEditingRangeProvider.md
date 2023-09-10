# LinkedEditingRangeProvider

The linked editing range provider interface defines the contract between extensions and the linked editing feature.

## Methods

### provideLinkedEditingRanges

```typescript
provideLinkedEditingRanges(document: TextDocument, position: Position, token: CancellationToken): ProviderResult<LinkedEditingRanges>
```

[LinkedEditingRanges]: LinkedEditingRanges.md
[ProviderResult]: ProviderResultT.md
[Position]: Position.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
