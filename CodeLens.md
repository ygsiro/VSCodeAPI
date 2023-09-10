# CodeLens

A code lens represents a Command that should be shown along with source text, like the number of references, a way to run tests, etc.

A code lens is unresolved when no command is associated to it. For performance reasons the creation of a code lens and resolving should be done to two stages.

See also

provideCodeLenses
resolveCodeLens

## Constructors

```typescript
new CodeLens(range: Range, command?: Command): CodeLens
```

## Properties

### command

```typescript
command?: Command
```

### isResolved

```typescript
isResolved: boolean
```

### range

```typescript
range: Range
```

[Range]: Range.md
[Command]: Command.md
