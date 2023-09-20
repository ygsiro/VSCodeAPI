# WorkspaceFolder

A workspace folder is one of potentially many roots opened by the editor. All workspace folders are equal which means there is no notion of an active or primary workspace folder.

## Properties

### index

```typescript
index: number
```

The ordinal number of this workspace folder.

### name

```typescript
name: string
```

The name of this workspace folder.
Defaults to the basename of its uri-path.

### uri

```typescript
uri: Uri
```

The associated ur for this workspace folder.

Note: The Uri-type was intentionally chosen such that future releases
of the editor can support workspace folders that are not stored on the
local disk, e.g.
`ftp://server/workspaces/foo`

[Uri]: Uri.md
