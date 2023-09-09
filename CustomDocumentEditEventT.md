## CustomDocumentEditEvent&lt;T&gt;

Event triggered by extensions to signal to the editor that an edit has occurred on an CustomDocument.

See also onDidChangeCustomDocument.

## Properties

### document

```typescript
document: T
```

### label

```typescript
label?: string
```

## Methods

### redo

```typescript
redo(): void | Thenable<void>
```

### undo

```typescript
undo(): void | Thenable<void>
```

