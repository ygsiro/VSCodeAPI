# SecretStorage

Represents a storage utility for secrets, information that is sensitive.

## Events

### onDidChange

```typescript
onDidChange: Event<SecretStorageChangeEvent>
```

## Methods

### delete

```typescript
delete(key: string): Thenable<void>
```

### get

```typescript
get(key: string): Thenable<string>
```

### store

```typescript
store(key: string, value: string): Thenable<void>
```

