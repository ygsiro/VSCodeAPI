# NotebookDocumentWillSaveEvent

An event that is fired when a notebook document will be saved.

To make modifications to the document before it is being saved, call the waitUntil-function with a thenable that resolves to a workspace edit.

## Properties

### notebook

```typescript
notebook: NotebookDocument
```

### reason

```typescript
reason: TextDocumentSaveReason
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

[NotebookDocument]: NotebookDocument.md
[TextDocumentSaveReason]: TextDocumentSaveReason.md
[WorkspaceEdit]: WorkspaceEdit.md
[CancellationToken]: CancellationToken.md
