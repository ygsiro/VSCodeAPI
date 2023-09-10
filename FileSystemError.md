# FileSystemError

A type that filesystem providers should use to signal errors.

This class has factory methods for common error-cases, like FileNotFound when a file or folder doesn't exist, use them like so: throw vscode.FileSystemError.FileNotFound(someUri);

## Static

### FileExists

```typescript
FileExists(messageOrUri?: string | Uri): FileSystemError
```

### FileIsADirectory

```typescript
FileIsADirectory(messageOrUri?: string | Uri): FileSystemError
```

### FileNotADirectory

```typescript
FileNotADirectory(messageOrUri?: string | Uri): FileSystemError
```

### FileNotFound

```typescript
FileNotFound(messageOrUri?: string | Uri): FileSystemError
```

### NoPermissions

```typescript
NoPermissions(messageOrUri?: string | Uri): FileSystemError
```

### Unavailable

```typescript
Unavailable(messageOrUri?: string | Uri): FileSystemError
```

## Constructors

```typescript
new FileSystemError(messageOrUri?: string | Uri): FileSystemError
```

## Properties

### code

```typescript
code: string
```

[Uri]: Uri.md
