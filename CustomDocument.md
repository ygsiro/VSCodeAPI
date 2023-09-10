# CustomDocument

Represents a custom document used by a CustomEditorProvider.

Custom documents are only used within a given CustomEditorProvider. The lifecycle of a CustomDocument is managed by the editor. When no more references remain to a CustomDocument, it is disposed of.

## Properties

### uri

```typescript
uri: Uri
```

## Methods

### dispose

```typescript
dispose(): void
```

[Uri]: Uri.md
