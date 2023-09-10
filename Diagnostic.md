# Diagnostic

Represents a diagnostic, such as a compiler error or warning. Diagnostic objects are only valid in the scope of a file.

## Constructors

```typescript
new Diagnostic(range: Range, message: string, severity?: DiagnosticSeverity): Diagnostic
```

## Properties

### code

```typescript
code?: string | number | {target: Uri, value: string | number}
```

### message

```typescript
message: string
```

### range

```typescript
range: Range
```

### relatedInformation

```typescript
relatedInformation?: DiagnosticRelatedInformation[]
```

### severity

```typescript
severity: DiagnosticSeverity
```

### source

```typescript
source?: string
```

### tags

```typescript
tags?: DiagnosticTag[]
```

[DiagnosticRelatedInformation]: DiagnosticRelatedInformation.md
[DiagnosticSeverity]: DiagnosticSeverity.md
[Range]: Range.md
[DiagnosticTag]: DiagnosticTag.md
[Uri]: Uri.md
