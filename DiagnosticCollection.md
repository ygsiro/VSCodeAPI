# DiagnosticCollection

A diagnostics collection is a container that manages a set of diagnostics. Diagnostics are always scopes to a diagnostics collection and a resource.

To get an instance of a DiagnosticCollection use createDiagnosticCollection.

## Properties

### name

```typescript
name: string
```

## Methods

### clear

```typescript
clear(): void
```

### delete

```typescript
delete(uri: Uri): void
```

### dispose

```typescript
dispose(): void
```

### forEach

```typescript
forEach(callback: (uri: Uri, diagnostics: readonly Diagnostic[], collection: DiagnosticCollection) => any, thisArg?: any): void
```

### get

```typescript
get(uri: Uri): readonly Diagnostic[]
```

### has

```typescript
has(uri: Uri): boolean
```

### set

```typescript
set(uri: Uri, diagnostics: readonly Diagnostic[]): void
```

### set

```typescript
set(entries: readonly [Uri, readonly Diagnostic[]][]): void
```

