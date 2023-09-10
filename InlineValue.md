# InlineValue

Inline value information can be provided by different means:

directly as a text value (class InlineValueText).
as a name to use for a variable lookup (class InlineValueVariableLookup)
as an evaluatable expression (class InlineValueEvaluatableExpression) The InlineValue types combines all inline value types into one type.

```typescript
InlineValue: InlineValueText | InlineValueVariableLookup | InlineValueEvaluatableExpression
```

[InlineValueEvaluatableExpression]: InlineValueEvaluatableExpression.md
[InlineValueText]: InlineValueText.md
[InlineValueVariableLookup]: InlineValueVariableLookup.md
