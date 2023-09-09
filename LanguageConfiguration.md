# LanguageConfiguration

The language configuration interfaces defines the contract between extensions and various editor features, like automatic bracket insertion, automatic indentation etc.

## Properties

### __characterPairSupport

```typescript
__characterPairSupport?: {autoClosingPairs: {close: string, notIn: string[], open: string}[]}
```

### __electricCharacterSupport

```typescript
__electricCharacterSupport?: {brackets: any, docComment: {close: string, lineStart: string, open: string, scope: string}}
```

### brackets

```typescript
brackets?: CharacterPair[]
```

### comments

```typescript
comments?: CommentRule
```

### indentationRules

```typescript
indentationRules?: IndentationRule
```

### onEnterRules

```typescript
onEnterRules?: OnEnterRule[]
```

### wordPattern

```typescript
wordPattern?: RegExp
```

