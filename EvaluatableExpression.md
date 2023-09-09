# EvaluatableExpression

An EvaluatableExpression represents an expression in a document that can be evaluated by an active debugger or runtime. The result of this evaluation is shown in a tooltip-like widget. If only a range is specified, the expression will be extracted from the underlying document. An optional expression can be used to override the extracted expression. In this case the range is still used to highlight the range in the document.

## Constructors

```typescript
new EvaluatableExpression(range: Range, expression?: string): EvaluatableExpression
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

