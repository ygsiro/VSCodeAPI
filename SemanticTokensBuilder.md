# SemanticTokensBuilder

A semantic tokens builder can help with creating a SemanticTokens instance which contains delta encoded semantic tokens.

## Constructors

```typescript
new SemanticTokensBuilder(legend?: SemanticTokensLegend): SemanticTokensBuilder
```

## Methods

### build

```typescript
build(resultId?: string): SemanticTokens
```

### push

```typescript
push(line: number, char: number, length: number, tokenType: number, tokenModifiers?: number): void
```

### push

```typescript
push(range: Range, tokenType: string, tokenModifiers?: readonly string[]): void
```

