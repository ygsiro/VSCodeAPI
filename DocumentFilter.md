# DocumentFilter

A document filter denotes a document by different properties like the language, the scheme of its resource, or a glob-pattern that is applied to the path.

example - A language filter that applies to typescript files on disk
`{ language: 'typescript', scheme: 'file' }`
example - A language filter that applies to all package.json paths
`{ language: 'json', pattern: '**/package.json' }`

## Properties

### language

```typescript
language?: string
```

### notebookType

```typescript
notebookType?: string
```

### pattern

```typescript
pattern?: GlobPattern
```

### scheme

```typescript
scheme?: string
```

[GlobPattern]: GlobPattern.md
