# SignatureInformation

Represents the signature of something callable. A signature can have a label, like a function-name, a doc-comment, and a set of parameters.

## Constructors

```typescript
new SignatureInformation(label: string, documentation?: string | MarkdownString): SignatureInformation
```

## Properties

### activeParameter

```typescript
activeParameter?: number
```

### documentation

```typescript
documentation?: string | MarkdownString
```

### label

```typescript
label: string
```

### parameters

```typescript
parameters: ParameterInformation[]
```

