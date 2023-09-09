# NotebookSerializer

The notebook serializer enables the editor to open notebook files.

At its core the editor only knows a notebook data structure but not how that data structure is written to a file, nor how it is read from a file. The notebook serializer bridges this gap by deserializing bytes into notebook data and vice versa.

## Methods

### deserializeNotebook

```typescript
deserializeNotebook(content: Uint8Array, token: CancellationToken): NotebookData | Thenable<NotebookData>
```

### serializeNotebook

```typescript
serializeNotebook(data: NotebookData, token: CancellationToken): Uint8Array | Thenable<Uint8Array>
```

