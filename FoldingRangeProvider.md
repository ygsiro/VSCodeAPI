# FoldingRangeProvider

The folding range provider interface defines the contract between extensions and Folding in the editor.

## Events

### onDidChangeFoldingRanges

```typescript
onDidChangeFoldingRanges?: Event<void>
```

## Methods

### provideFoldingRanges

```typescript
provideFoldingRanges(document: TextDocument, context: FoldingContext, token: CancellationToken): ProviderResult<FoldingRange[]>
```

[FoldingRange]: FoldingRange.md
[Event]: EventT.md
[ProviderResult]: ProviderResultT.md
[FoldingContext]: FoldingContext.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
