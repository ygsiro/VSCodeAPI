## CompletionItemProvider&lt;T&gt;

The completion item provider interface defines the contract between extensions and IntelliSense.

Providers can delay the computation of the detail and documentation properties by implementing the resolveCompletionItem-function. However, properties that are needed for the initial sorting and filtering, like sortText, filterText, insertText, and range, must not be changed during resolve.

Providers are asked for completions either explicitly by a user gesture or -depending on the configuration- implicitly when typing words or trigger characters.

## Methods

### provideCompletionItems

```typescript
provideCompletionItems(document: TextDocument, position: Position, token: CancellationToken, context: CompletionContext): ProviderResult<CompletionList<T> | T[]>
```

### resolveCompletionItem

```typescript
resolveCompletionItem(item: T, token: CancellationToken): ProviderResult<T>
```

