# DiagnosticRelatedInformation

Represents a related message and source code location for a diagnostic. This should be used to point to code locations that cause or related to a diagnostics, e.g. when duplicating a symbol in a scope.

## Constructors

```typescript
new DiagnosticRelatedInformation(location: Location, message: string): DiagnosticRelatedInformation
```

## Properties

### location

```typescript
location: Location
```

### message

```typescript
message: string
```

