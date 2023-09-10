# InlineValueEvaluatableExpression

Provide an inline value through an expression evaluation. If only a range is specified, the expression will be extracted from the underlying document. An optional expression can be used to override the extracted expression.

## Constructors

```typescript
new InlineValueEvaluatableExpression(range: Range, expression?: string): InlineValueEvaluatableExpression
```

## Properties

### expression

```typescript
expression?: string
```

### range

```typescript
range: Range
```

[Range]: Range.md
