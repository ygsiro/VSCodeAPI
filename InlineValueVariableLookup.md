# InlineValueVariableLookup

Provide inline value through a variable lookup. If only a range is specified, the variable name will be extracted from the underlying document. An optional variable name can be used to override the extracted name.

## Constructors

```typescript
new InlineValueVariableLookup(range: Range, variableName?: string, caseSensitiveLookup?: boolean): InlineValueVariableLookup
```

## Properties

### caseSensitiveLookup

```typescript
caseSensitiveLookup: boolean
```

### range

```typescript
range: Range
```

### variableName

```typescript
variableName?: string
```

