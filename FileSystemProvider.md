# FileSystemProvider

The filesystem provider defines what the editor needs to read, write, discover, and to manage files and folders. It allows extensions to serve files from remote places, like ftp-servers, and to seamlessly integrate those into the editor.

Note 1: The filesystem provider API works with uris and assumes hierarchical paths, e.g. foo:/my/path is a child of foo:/my/ and a parent of foo:/my/path/deeper.
Note 2: There is an activation event onFileSystem:<scheme> that fires when a file or folder is being accessed.
Note 3: The word 'file' is often used to denote all kinds of files, e.g. folders, symbolic links, and regular files.

## Events

### onDidChangeFile

```typescript
onDidChangeFile: Event<FileChangeEvent[]>
```

## Methods

### copy

```typescript
copy(source: Uri, destination: Uri, options: {overwrite: boolean}): void | Thenable<void>
```

### createDirectory

```typescript
createDirectory(uri: Uri): void | Thenable<void>
```

### delete

```typescript
delete(uri: Uri, options: {recursive: boolean}): void | Thenable<void>
```

### readDirectory

```typescript
readDirectory(uri: Uri): [string, FileType][] | Thenable<[string, FileType][]>
```

### readFile

```typescript
readFile(uri: Uri): Uint8Array | Thenable<Uint8Array>
```

### rename

```typescript
rename(oldUri: Uri, newUri: Uri, options: {overwrite: boolean}): void | Thenable<void>
```

### stat

```typescript
stat(uri: Uri): FileStat | Thenable<FileStat>
```

### watch

```typescript
watch(uri: Uri, options: {excludes: readonly string[], recursive: boolean}): Disposable
```

### writeFile

```typescript
writeFile(uri: Uri, content: Uint8Array, options: {create: boolean, overwrite: boolean}): void | Thenable<void>
```

