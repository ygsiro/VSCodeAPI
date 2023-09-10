# TextDocumentWillSaveEvent

An event that is fired when a document will be saved.

To make modifications to the document before it is being saved, call the waitUntil-function with a thenable that resolves to an array of text edits.

## Properties

### document

```typescript
document: TextDocument
```

### reason

```typescript
reason: TextDocumentSaveReason
```

## Methods

### waitUntil

```typescript
waitUntil(thenable: Thenable<readonly TextEdit[]>): void
```

### waitUntil

```typescript
waitUntil(thenable: Thenable<any>): void
```

[TextDocumentSaveReason]: TextDocumentSaveReason.md
[TextEdit]: TextEdit.md
[TextDocument]: TextDocument.md
