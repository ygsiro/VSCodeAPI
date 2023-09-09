# CodeActionKind

Kind of a code action.

Kinds are a hierarchical list of identifiers separated by ., e.g. "refactor.extract.function".

Code action kinds are used by the editor for UI elements such as the refactoring context menu. Users can also trigger code actions with a specific kind with the editor.action.codeAction command.

## Static

### Empty

```typescript
Empty: CodeActionKind
```

### QuickFix

```typescript
QuickFix: CodeActionKind
```

### Refactor

```typescript
Refactor: CodeActionKind
```

### RefactorExtract

```typescript
RefactorExtract: CodeActionKind
```

### RefactorInline

```typescript
RefactorInline: CodeActionKind
```

### RefactorMove

```typescript
RefactorMove: CodeActionKind
```

### RefactorRewrite

```typescript
RefactorRewrite: CodeActionKind
```

### Source

```typescript
Source: CodeActionKind
```

### SourceFixAll

```typescript
SourceFixAll: CodeActionKind
```

### SourceOrganizeImports

```typescript
SourceOrganizeImports: CodeActionKind
```

## Constructors

```typescript
new CodeActionKind(value: string): CodeActionKind
```

## Properties

### value

```typescript
value: string
```

## Methods

### append

```typescript
append(parts: string): CodeActionKind
```

### contains

```typescript
contains(other: CodeActionKind): boolean
```

### intersects

```typescript
intersects(other: CodeActionKind): boolean
```

