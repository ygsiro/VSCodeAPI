# ExtensionContext

An extension context is a collection of utilities private to an extension.

An instance of an ExtensionContext is provided as the first parameter to the activate-call of an extension.

## Properties

### environmentVariableCollection

```typescript
environmentVariableCollection: GlobalEnvironmentVariableCollection
```

### extension

```typescript
extension: Extension<any>
```

### extensionMode

```typescript
extensionMode: ExtensionMode
```

### extensionPath

```typescript
extensionPath: string
```

### extensionUri

```typescript
extensionUri: Uri
```

### globalState

```typescript
globalState: Memento & {setKeysForSync}
```

### globalStoragePath

```typescript
globalStoragePath: string
```

### globalStorageUri

```typescript
globalStorageUri: Uri
```

### logPath

```typescript
logPath: string
```

### logUri

```typescript
logUri: Uri
```

### secrets

```typescript
secrets: SecretStorage
```

### storagePath

```typescript
storagePath: string
```

### storageUri

```typescript
storageUri: Uri
```

### subscriptions

```typescript
subscriptions: {dispose}[]
```

### workspaceState

```typescript
workspaceState: Memento
```

## Methods

### asAbsolutePath

```typescript
asAbsolutePath(relativePath: string): string
```

