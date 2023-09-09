# CodeAction

A code action represents a change that can be performed in code, e.g. to fix a problem or to refactor code.

A CodeAction must set either edit and/or a command. If both are supplied, the edit is applied first, then the command is executed.

## Constructors

```typescript
new CodeAction(title: string, kind?: CodeActionKind): CodeAction
```

## Properties

### command

```typescript
command?: Command
```

### diagnostics

```typescript
diagnostics?: Diagnostic[]
```

### disabled

```typescript
disabled?: {reason: string}
```

### edit

```typescript
edit?: WorkspaceEdit
```

### isPreferred

```typescript
isPreferred?: boolean
```

### kind

```typescript
kind?: CodeActionKind
```

### title

```typescript
title: string
```

