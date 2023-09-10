# FileWillRenameEvent

An event that is fired when files are going to be renamed.

To make modifications to the workspace before the files are renamed, call the waitUntil-function with a thenable that resolves to a workspace edit.

## Properties

### files

```typescript
files: readonly {newUri: Uri, oldUri: Uri}[]
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
