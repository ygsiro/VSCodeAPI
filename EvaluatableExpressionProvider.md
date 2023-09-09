# EvaluatableExpressionProvider

The evaluatable expression provider interface defines the contract between extensions and the debug hover. In this contract the provider returns an evaluatable expression for a given position in a document and the editor evaluates this expression in the active debug session and shows the result in a debug hover.

## Methods

### provideEvaluatableExpression

```typescript
provideEvaluatableExpression(document: TextDocument, position: Position, token: CancellationToken): ProviderResult<EvaluatableExpression>
```

