# RelativePattern

A relative pattern is a helper to construct glob patterns that are matched relatively to a base file path. The base path can either be an absolute file path as string or uri or a workspace folder, which is the preferred way of creating the relative pattern.

## Constructors

```typescript
new RelativePattern(base: string | Uri | WorkspaceFolder, pattern: string): RelativePattern
```

## Properties

### base

```typescript
base: string
```

### baseUri

```typescript
baseUri: Uri
```

### pattern

```typescript
pattern: string
```

[WorkspaceFolder]: WorkspaceFolder.md
[Uri]: Uri.md
