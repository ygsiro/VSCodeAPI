# InlineValuesProvider

The inline values provider interface defines the contract between extensions and the editor's debugger inline values feature. In this contract the provider returns inline value information for a given document range and the editor shows this information in the editor at the end of lines.

## Events

### onDidChangeInlineValues

```typescript
onDidChangeInlineValues?: Event<void>
```

## Methods

### provideInlineValues

```typescript
provideInlineValues(document: TextDocument, viewPort: Range, context: InlineValueContext, token: CancellationToken): ProviderResult<InlineValue[]>
```

[InlineValueContext]: InlineValueContext.md
[Event]: EventT.md
[Range]: Range.md
[ProviderResult]: ProviderResultT.md
[InlineValue]: InlineValue.md
[TextDocument]: TextDocument.md
[CancellationToken]: CancellationToken.md
