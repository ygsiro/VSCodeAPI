# DocumentSelector

A language selector is the combination of one or many language identifiers and language filters.

Note that a document selector that is just a language identifier selects all documents, even those that are not saved on disk. Only use such selectors when a feature works without further context, e.g. without the need to resolve related 'files'.

example

```typescript
let sel:DocumentSelector = { scheme: 'file', language: 'typescript' };
```

```typescript
DocumentSelector: DocumentFilter | string | ReadonlyArray<DocumentFilter | string>
```

[DocumentFilter]: DocumentFilter.md
