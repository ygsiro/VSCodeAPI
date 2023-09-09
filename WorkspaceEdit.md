# WorkspaceEdit

A workspace edit is a collection of textual and files changes for multiple resources and documents.

Use the applyEdit-function to apply a workspace edit.

## Constructors

```typescript
new WorkspaceEdit(): WorkspaceEdit
```

## Properties

### size

```typescript
size: number
```

## Methods

### createFile

```typescript
createFile(uri: Uri, options?: {contents: Uint8Array | DataTransferFile, ignoreIfExists: boolean, overwrite: boolean}, metadata?: WorkspaceEditEntryMetadata): void
```

### delete

```typescript
delete(uri: Uri, range: Range, metadata?: WorkspaceEditEntryMetadata): void
```

### deleteFile

```typescript
deleteFile(uri: Uri, options?: {ignoreIfNotExists: boolean, recursive: boolean}, metadata?: WorkspaceEditEntryMetadata): void
```

### entries

```typescript
entries(): [Uri, TextEdit[]][]
```

### get

```typescript
get(uri: Uri): TextEdit[]
```

### has

```typescript
has(uri: Uri): boolean
```

### insert

```typescript
insert(uri: Uri, position: Position, newText: string, metadata?: WorkspaceEditEntryMetadata): void
```

### renameFile

```typescript
renameFile(oldUri: Uri, newUri: Uri, options?: {ignoreIfExists: boolean, overwrite: boolean}, metadata?: WorkspaceEditEntryMetadata): void
```

### replace

```typescript
replace(uri: Uri, range: Range, newText: string, metadata?: WorkspaceEditEntryMetadata): void
```

### set

```typescript
set(uri: Uri, edits: readonly TextEdit | SnippetTextEdit[]): void
```

### set

```typescript
set(uri: Uri, edits: readonly [TextEdit | SnippetTextEdit, WorkspaceEditEntryMetadata][]): void
```

### set

```typescript
set(uri: Uri, edits: readonly NotebookEdit[]): void
```

### set

```typescript
set(uri: Uri, edits: readonly [NotebookEdit, WorkspaceEditEntryMetadata][]): void
```

