# InlineCompletionItemProvider

The inline completion item provider interface defines the contract between extensions and the inline completion feature.

Providers are asked for completions either explicitly by a user gesture or implicitly when typing.

## Methods

### provideInlineCompletionItems

```typescript
provideInlineCompletionItems(document: TextDocument, position: Position, context: InlineCompletionContext, token: CancellationToken): ProviderResult<InlineCompletionList | InlineCompletionItem[]>
```

[InlineCompletionList]: InlineCompletionList.md
[ProviderResult]: ProviderResultT.md
[InlineCompletionContext]: InlineCompletionContext.md
[InlineCompletionItem]: InlineCompletionItem.md
[Position]: Position.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
