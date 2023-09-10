# FileSystem

The file system interface exposes the editor's built-in and contributed file system providers. It allows extensions to work with files from the local disk as well as files from remote places, like the remote extension host or ftp-servers.

Note that an instance of this interface is available as fs.

## Methods

### copy

```typescript
copy(source: Uri, target: Uri, options?: {overwrite: boolean}): Thenable<void>
```

### createDirectory

```typescript
createDirectory(uri: Uri): Thenable<void>
```

### delete

```typescript
delete(uri: Uri, options?: {recursive: boolean, useTrash: boolean}): Thenable<void>
```

### isWritableFileSystem

```typescript
isWritableFileSystem(scheme: string): boolean
```

### readDirectory

```typescript
readDirectory(uri: Uri): Thenable<[string, FileType][]>
```

### readFile

```typescript
readFile(uri: Uri): Thenable<Uint8Array>
```

### rename

```typescript
rename(source: Uri, target: Uri, options?: {overwrite: boolean}): Thenable<void>
```

### stat

```typescript
stat(uri: Uri): Thenable<FileStat>
```

### writeFile

```typescript
writeFile(uri: Uri, content: Uint8Array): Thenable<void>
```

[Uri]: Uri.md
[FileStat]: FileStat.md
[FileType]: FileType.md
