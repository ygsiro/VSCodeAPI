# FileWillDeleteEvent

An event that is fired when files are going to be deleted.

To make modifications to the workspace before the files are deleted, call the waitUntil-function with a thenable that resolves to a workspace edit.

## Properties

### files

```typescript
files: readonly Uri[]
```

### token

```typescript
token: CancellationToken
```

## Methods

### waitUntil

```typescript
waitUntil(thenable: Thenable<WorkspaceEdit>): void
```

### waitUntil

```typescript
waitUntil(thenable: Thenable<any>): void
```

[Uri]: Uri.md
[WorkspaceEdit]: WorkspaceEdit.md
[CancellationToken]: CancellationToken.md
